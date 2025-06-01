from ecommerce.models import Shop, Banner, Blog, Menu, MenuItem, Section, Category, Brand, Social, Tag, ShippingProfile, Product, ProductImage, VariantSuggestion, ProductVariant, Review, Customer, Address, Order_status, Order, MediaFile
from ecommerce.models import Page, Staff, ThemePackage, Theme, ShopTheme, Contact, Review, EmailMessage, EmailTemplate, Plugin, ShopPlugin, Subscriber, Coupon
from ecommerce.models import Leads
from core.models import Invoice
from .serializers import *
from django.db.models import Count, Q, Sum
from django.db.models.functions import TruncDate
import json, requests
import time
import base64
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from datetime import datetime, timedelta
from ecommerce.decorators import get_shop
from django.utils.timezone import make_aware, now

from core.models import Domain, Dns, Settings, Account, Notification
from core.mailing import send_mail
from core.mail_templates import domain_add_message

def strToFile(base64_str):
    format, imgstr = base64_str.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
def urlToFile(img_url):
    response = requests.get(img_url)
    return ContentFile(response.content, name='temp.jpg')


@api_view(['GET', 'POST', 'PUT'])
@get_shop
def shop(request, shop):
    domain, created = Domain.objects.get_or_create(account=shop.account, subdomain=True, domain=shop.name.strip())
    shop.domains.add(domain)
    shop.save()
    if not shop.package:
        shop.package = ThemePackage.objects.filter(price = 0.00).order_by('level').first()
    if request.method == 'GET':
        st, ct = Settings.objects.get_or_create()
        serializer = ShopSerializer(shop)
        data = serializer.data
        data['shop_message'] = st.shop_message
        data['shop_message_link'] = st.shop_message_link
        return Response(data)
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'newLogo' in data:
            shop.logo = strToFile(data['newLogo'])
        if 'newFavicon' in data:
            shop.favicon = strToFile(data['newFavicon'])
        if 'newPayment_image' in data:
            shop.payment_image = strToFile(data['newPayment_image'])
        shop.title = data['title']
        shop.name = data['name']
        shop.email = data['email']
        shop.phone = data['phone']
        shop.street = data['street']
        shop.city = data['city']
        shop.state = data['state']
        shop.zip_code = data['zip_code']
        shop.country = data['country']
        shop.currency = data['currency']
        shop.android_app_link = data['android_app_link']
        shop.ios_app_link = data['ios_app_link']
        
        if 'warehouse' in data:
            shop.warehouse = data['warehouse']
        if 'room' in data:
            shop.room = data['room']
        if 'sec' in data:
            shop.sec = data['sec']
        if 'shelf' in data:
            shop.shelf = data['shelf']
        if 'rack' in data:
            shop.rack = data['rack']
        if 'drawer' in data:
            shop.drawer = data['drawer']
        if 'file' in data:
            shop.file = data['file']

        shop.save()
        return Response(200, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@get_shop
def steps(request, shop):
    data = []
    completes = 0
    st1 = { "name": 'Provide General Info', "description": 'Add Logo, Brands & Category', "href": '/ecommerce/settings/', 'status': 'current' }
    if shop.logo and Brand.objects.filter(shop=shop).exists() and Category.objects.filter(section__shop=shop).exists():
        st1['status'] = 'complete'
        completes += 1
    data.append(st1)
    st2 = { "name": 'Setup Shop Settings', "description": 'Add Personal & Billing Info', "href": '/ecommerce/settings/', 'status': 'current' }
    if shop.account.first_name and shop.account.last_name and shop.account.email and shop.account.phone_number and shop.account.address and shop.account.city and shop.account.state and shop.account.zip_code and shop.account.country and shop.account.billing_first_name and shop.account.billing_last_name and shop.account.billing_address and shop.account.billing_city and shop.account.billing_state and shop.account.billing_zip_code and shop.account.billing_country:
        st2['status'] = 'complete'
        completes += 1
    data.append(st2)
    st3 = { "name": 'Purchase A Theme', "description": 'Purchase A Theme', "href": '/ecommerce/themes', 'status': 'current' }
    if ShopTheme.objects.filter(shop=shop).exists():
        st3['status'] = 'complete'
        completes += 1
    data.append(st3)
    st4 = { "name": 'Setup Shipping & Charges Profile', "description": 'Add Shipping & Charges Profile', "href": '/ecommerce/shipping', 'status': 'current' }
    if ShippingProfile.objects.filter(shop=shop).exists():
        st4['status'] = 'complete'
        completes += 1
    data.append(st4)
    st5 = { "name": 'Add Custom Domain', "description": '....', "href": '/ecommerce/domain', 'status': 'current' }
    if shop.domains.filter(subdomain=False).exists():
        st5['status'] = 'complete'
        completes += 1
    data.append(st5)
    st6 = { "name": 'Add Your First Product', "description": '....', "href": '/ecommerce/products', 'status': 'current' }
    if Product.objects.filter(shop=shop).exists():
        st6['status'] = 'complete'
        completes += 1
    data.append(st6)
    percentage = (completes / len(data)) * 100
    return Response({'data': data, 'percentage': int(percentage)})

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def chart(request, shop):
    today = datetime.today()
    labels = [(today - timedelta(days=i)) for i in range(6, -1, -1)]
    number_of_sales = []
    pending_sales = []
    complete_sales = []
    for i in range(6, -1, -1):
        # Get the date for this day
        date = today - timedelta(days=i)

        # Filter the Order model by the created_at field for this day
        orders = Order.objects.filter(created_at__date=date)

        # Count the number of orders and sum the total sales for this day
        number_of_sales.append(orders.count())
        pending_sales.append(orders.filter(status = 'Pending').count())
        complete_sales.append(orders.filter(is_completed = True).count())
    data = {
        'labels': labels,
        'number_of_sales': number_of_sales,
        'pending_sales': pending_sales,
        'complete_sales': complete_sales,
    }
    return Response(data)

def get_order_data(orders, startDate, endDate):
    # Initialize an empty list to store the result
    startDate = make_aware(startDate)
    endDate = make_aware(endDate)
    data1 = []
    data2 = []
    data3 = []

    # Iterate through the date range
    current_date = startDate
    while current_date <= endDate:
        # Calculate the next date
        next_date = current_date + timedelta(days=1)

        # Query the database to get the desired data for the current date
        data = orders.filter(
            created_at__gte=current_date,
            created_at__lt=next_date
        ).aggregate(
            num_orders=Count('id'),
            total_amount=Sum('total'),
            profit_amount=Sum('profit'),
        )

        # Append the result to the list
        chart_date = str(current_date.strftime('%Y-%m-%d %H:%M')) + ' GMT'
        data1.append([
            chart_date,
            data['num_orders'] if data['num_orders'] else 0,
        ])
        data2.append([
            chart_date,
            data['total_amount'] if data['total_amount'] else 0
        ])
        data3.append([
            chart_date,
            data['profit_amount'] if data['profit_amount'] else 0
        ])
        # Move to the next date
        current_date = next_date

    return data1, data2, data3

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def overview(request, shop):
    allP = Product.objects.filter(shop=shop)
    allC = Customer.objects.filter(shop=shop)
    allO = Order.objects.filter(shop=shop).order_by('id')

    overviewType = request.data['overviewType']
    fromDate = request.data['fromDate']
    toDate = request.data['toDate']
    # print(overviewType, fromDate, toDate)
    current_date = datetime.today().replace(hour=0, minute=1, second=0, microsecond=0)
    if overviewType == 'Today':
        end_date = current_date + timedelta(days=1)
        start_date = current_date
        filteredOrders = allO.filter(created_at__date=start_date)
        stats = {
            'products': allP.filter(created_at__date=start_date).count(),
            'customers': allC.filter(created_at__date=start_date).count(),
        }
    elif overviewType == 'Yesterday':
        end_date = current_date
        start_date = current_date - timedelta(days=1)
        filteredOrders = allO.filter(created_at__date=start_date)
        stats = {
            'products': allP.filter(created_at__date=start_date).count(),
            'customers': allC.filter(created_at__date=start_date).count(),
        }
    elif overviewType == 'This Week':
        end_date = current_date
        start_date = current_date - timedelta(days=current_date.weekday())
        filteredOrders = allO.filter(created_at__date__gte=start_date)
        stats = {
            'products': allP.filter(created_at__date__gte=start_date).count(),
            'customers': allC.filter(created_at__date__gte=start_date).count(),
        }
    elif overviewType == 'Last Week':
        end_date = current_date - timedelta(days=current_date.weekday() + 7)
        start_date = end_date - timedelta(days=6)
        filteredOrders = allO.filter(created_at__date__range=(start_date, end_date))
        stats = {
            'products': allP.filter(created_at__date__range=(start_date, end_date)).count(),
            'customers': allC.filter(created_at__date__range=(start_date, end_date)).count(),
        }
    elif overviewType == 'This Month':
        end_date = current_date
        start_date = current_date.replace(day=1)
        filteredOrders = allO.filter(created_at__date__gte=start_date)
        stats = {
            'products': allP.filter(created_at__date__gte=start_date).count(),
            'customers': allC.filter(created_at__date__gte=start_date).count(),
        }
    elif overviewType == 'Last Month':
        end_date = current_date.replace(day=1) - timedelta(days=1)
        start_date = end_date.replace(day=1)
        filteredOrders = allO.filter(created_at__date__range=(start_date, end_date))
        stats = {
            'products': allP.filter(created_at__date__range=(start_date, end_date)).count(),
            'customers': allC.filter(created_at__date__range=(start_date, end_date)).count(),
        }
    elif overviewType == 'Custom Date' and fromDate and toDate:
        print(fromDate)
        end_date = datetime.strptime(toDate, "%Y-%m-%d")
        start_date = datetime.strptime(fromDate, "%Y-%m-%d")
        filteredOrders = allO.filter(created_at__date__range=[fromDate, toDate])
        stats = {
            'products': allP.filter(created_at__date__range=[fromDate, toDate]).count(),
            'customers': allC.filter(created_at__date__range=[fromDate, toDate]).count(),
        }
    else:
        end_date = current_date
        start_date = current_date - timedelta(days=1825)
        filteredOrders = allO
        stats = {
            'products': allP.count(),
            'customers': allC.count(),
        }
    stats['orders'] = filteredOrders.count()
    stats['total'] = filteredOrders.aggregate(Sum('total'))['total__sum'] or 0
    stats['pending_orders'] = filteredOrders.filter(is_completed = False, is_cancelled = False).count()
    stats['pending_total'] = filteredOrders.filter(is_completed = False, is_cancelled = False).aggregate(Sum('total'))['total__sum'] or 0
    stats['complete_orders'] = filteredOrders.filter(is_completed = True, is_cancelled = False).count()
    stats['complete_total'] = filteredOrders.filter(is_completed = True, is_cancelled = False).aggregate(Sum('total'))['total__sum'] or 0
    stats['cancelled_orders'] = filteredOrders.filter(is_completed = False, is_cancelled = True).count()
    stats['cancelled_total'] = filteredOrders.filter(is_completed = False, is_cancelled = True).aggregate(Sum('total'))['total__sum'] or 0

    # for char series 
    data1, data2, data3 = get_order_data(allO, start_date, end_date)
    series = [
		{
			'name': 'Total Sales',
			'data': data1,
		},
		{
			'name': "Sales Value",
			'data': data2,
		},
		{
			'name': "Est. Profit",
			'data': data3,
		},
	]
    data = {
        'stats': stats,
        'series': series,
    }
    return Response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def categories(request, shop):
    if request.method == 'GET':
        categories = Section.objects.filter(shop=shop).order_by('-id')
        data = SectionSerializer(categories, many=True)
        return Response(data.data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Section.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['type'] == 'section':
            new = Section.objects.create(name = data['name'], shop=shop)
            format, imgStr = data['image'].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
            new.image = data
            new.save()
            return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        section = Section.objects.get(id=data['id'])
        section.name = data['name']
        if 'newimage' in data:
            format, imgStr = data['newimage'].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
            section.image = data
        section.save()
        for cat in data['category_set']:
            if 'id' in cat:
                category = Category.objects.get(id=cat['id'])
                if 'deleted' in cat:
                    category.delete()
                    continue
                category.name = cat['name']
                if 'newimage' in cat:
                    format, imgStr = cat['newimage'].split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
                    category.image = data
                category.save()
            else:
                new = Category.objects.create(name = cat['name'], section=section)
                if 'newimage' in cat and cat['newimage'] != '':
                    format, imgStr = cat['newimage'].split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
                    new.image = data
                    new.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def menus(request, shop):
    main_menu, ct = Menu.objects.get_or_create(shop = shop, name="Main Menu")
    footer_menu, ct = Menu.objects.get_or_create(shop = shop, name="Footer Menu")
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        main_menu_json = data['main_menu']
        footer_menu_json = data['footer_menu']
        for item in main_menu_json:
            if not 'new' in item:
                menu_item = MenuItem.objects.get(id=item['id'])
                if 'deleted' in item:
                    menu_item.delete()
                    continue
                menu_item.name = item['name']
                menu_item.link = item['link']
                menu_item.save()
            else:
                MenuItem.objects.create(name = item['name'], link=item['link'], menu=main_menu)
        for item in footer_menu_json:
            if not 'new' in item:
                menu_item = MenuItem.objects.get(id=item['id'])
                if 'deleted' in item:
                    menu_item.delete()
                    continue
                menu_item.name = item['name']
                menu_item.link = item['link']
                menu_item.save()
            else:
                MenuItem.objects.create(name = item['name'], link=item['link'], menu=footer_menu)

    main_menu_items = MenuItem.objects.filter(menu=main_menu)
    footer_menu_items = MenuItem.objects.filter(menu=footer_menu)
    data = {
        'main_menu': MenuItemSerializer(main_menu_items, many=True).data,
        'footer_menu': MenuItemSerializer(footer_menu_items, many=True).data
    }
    return Response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def brands(request, shop):
    if request.method == 'GET':
        brands = Brand.objects.filter(shop=shop)
        data = BrandSerializer(brands, many=True)
        return Response(data.data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        print(id,66666)
        Brand.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        new = Brand.objects.create(name = data['name'], shop=shop)
        format, imgStr = data['image'].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
        new.image = data
        new.save()
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        brand = Brand.objects.get(id=data['id'])
        brand.name = data['name']
        if 'newimage' in data:
            format, imgStr = data['newimage'].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
            brand.image = data
        brand.save()
        return Response(status=status.HTTP_201_CREATED)
@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def socials(request, shop):
    if request.method == 'GET':
        socials = Social.objects.filter(shop=shop)
        data = SocialSerializer(socials, many=True)
        return Response(data.data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        print(id,66666)
        Social.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        new = Social.objects.create(name = data['name'],link = data['link'], shop=shop)
        format, imgStr = data['image'].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
        new.image = data
        new.save()
        print(6666666666666666666, new)
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        social = Social.objects.get(id=data['id'])
        social.name = data['name']
        if 'newimage' in data:
            format, imgStr = data['newimage'].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
            social.image = data
        social.save()
        return Response(status=status.HTTP_201_CREATED)
    


@api_view(['GET', 'DELETE','POST'])
@xframe_options_exempt
@get_shop
def tags(request, shop):
    if request.method == 'GET':
        qs = Tag.objects.filter(shop=shop).order_by('-qty')
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(name__icontains=search)
        data = TagSerializer(qs, many=True)
        return Response(data.data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Tag.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        new = Tag.objects.create(name = data['name'], shop=shop)
        return Response(status=status.HTTP_201_CREATED)
@api_view(['GET', 'DELETE','POST'])
@xframe_options_exempt
@get_shop
def MediaFiles(request, shop):
    if request.method == 'GET':
        qs = MediaFile.objects.filter(shop=shop).order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= MediaFileSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        MediaFile.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        uploads = []
        for newImg in data:
            format, imgStr = newImg.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
            new = MediaFile.objects.create(file=data, shop=shop)
            uploads.append(new.id)
        qs = MediaFile.objects.filter(id__in=uploads)
        data = MediaFileSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST'])
@xframe_options_exempt
@get_shop
def products(request, shop):
    if request.method == 'GET':
        delete = request.GET.get('del', None)
        if delete:
            Product.objects.filter(id=delete).delete()
        detail = request.GET.get('detail', None)
        if detail:
            product = Product.objects.get(id=detail)
            data = ProductSerializer(product).data
            return Response(data)
        products = Product.objects.filter(shop=shop).order_by('-id')
        search = request.GET.get('search', None)
        if search:
            products = products.filter(Q(id__iexact=search) | Q(name__icontains=search) | Q(short_description__icontains=search))
        paginator = PageNumberPagination()
        paginator.page_size = 15
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Product.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'POST':
        data = request.data
        if not data['buy_price']:
            data['buy_price'] = 0
        if not data['sale_price']:
            data['sale_price'] = 0
        if not data['discount_p']:
            data['discount_p'] = 0
        if not data['discount_f']:
            data['discount_f'] = 0
        # data['video'] = None
        # 'data:video/webm;base64,GkXfowEAAAAA
        try:
            if 'video' in data and data['video'] and data['video'] != 'null':
                format, imgStr = data['video'].split(';base64,')
                ext = format.split('/')[-1]
                data['video'] = ContentFile(base64.b64decode(imgStr), name='temp.' + ext)
        except:
            del data['video']
            pass
        
        if not 'id' in data:
            serializer = ProductSerializer(data=data)
        else:
            product = Product.objects.get(id=data['id'])
            serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            product = serializer.save(shop_id=shop.id)
        
            current_categories = product.categories.all()
            new_category_ids = set(data['categories']) 
            for cid in new_category_ids:
                category = Category.objects.get(id=cid)
                product.categories.add(category)
                for category in current_categories:
                    if category.id not in new_category_ids:
                        product.categories.remove(category)
            for tg in data['tags']:
                tag = Tag.objects.get(id=tg['id'])
                if 'deleted' in tg:
                    product.tags.remove(tag)
                else:
                    product.tags.add(tag)
            product.shipping = ShippingProfile.objects.filter(id=data['shipping']).first()
            if not product.shipping:
                product.draft = True
                product.active = False
            if 'brandname' in data and data['brandname']:
                product.brand = Brand.objects.get(id=data['brandname'])

            # variation
            if data['has_variants']:
                for variant in data['productvariant_set']:
                    # {'buy_price': 462346, 'sale_price': 2, 'stock': 34623, 'color': '34256', 'size': '3462', 'weight': '', 'model': '', 'material': '', 'id': 'u0jyhw0k3bznbt4ae63sj', 'new': True}
                    if 'deleted' in variant:
                        print(variant['deleted'])
                        ProductVariant.objects.filter(id=variant['id']).delete()
                    elif 'new' in variant:
                        new = ProductVariant.objects.create(product=product, buy_price=variant['buy_price'], sale_price=variant['sale_price'], stock=variant['stock'], color=variant['color'], size=variant['size'], weight=variant['weight'], model=variant['model'], material=variant['material'])
                    else:
                        new = ProductVariant.objects.get(id=variant['id'])
                        new.buy_price = variant['buy_price']
                        new.sale_price = variant['sale_price']
                        new.stock = variant['stock']
                        new.color = variant['color']
                        new.size = variant['size']
                        new.weight = variant['weight']
                        new.model = variant['model']
                        new.material = variant['material']
                        new.save()
            if 'productimage_set' in data:
                for img in data['productimage_set']:
                    if 'deleted' in img:
                        ProductImage.objects.filter(id=img['id']).delete()
            if 'newImages' in data:
                for img in data['newImages']:
                    mediaFile = MediaFile.objects.get(id=img['id'])
                    ProductImage.objects.create(product = product, image = mediaFile.file)
            if 'newUrlImages' in data:
                for url in data['newUrlImages']:
                    file = urlToFile(url)
                    new_media = MediaFile.objects.create(file=file, shop=shop)
                    ProductImage.objects.create(product = product, image = new_media.file)
            product.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def shipping(request, shop):
    if request.method == 'GET':
        shipping = ShippingProfile.objects.filter(shop=shop)
        data = ShippingProfileSerializer(shipping, many=True)
        return Response(data.data)
    if request.method == 'PUT':
        data = json.loads(request.body)
        shipping = ShippingProfile.objects.get(id=data['id'])
        shipping.name = data['name']
        shipping.save()
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        sp = ShippingProfile.objects.filter(id=id).first()
        sp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        shipping = ShippingProfile.objects.create(name=data['name'], shop=shop)
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def shippingData(request, shop):
    if request.method == 'GET':
        id = request.GET.get('id')
        profile = ShippingProfile.objects.get(id=id, shop=shop)
        data = ShippingProfileDataSerializer(profile).data
        return Response(data)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        profile = ShippingProfile.objects.get(id=request.GET.get('id'))
        profile.data = data['data']
        profile.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def customers(request, shop):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        cus = Customer.objects.get(id=data['id'])
        cus.email = data['email']
        cus.phone = data['phone']
        cus.save()
        res = {
            'class': 'success',
            'message': 'Customer updated successfully!',
        }
        if 'new_pass' in data and data['new_pass'] != '':
            user = cus.user
            user.set_password(data['new_pass'])
            user.save()
        return Response(res)
    if request.method == 'DELETE':
        cus = Customer.objects.get(id=request.GET.get('id'))
        cus.user.delete()
        res = {
            'class': 'success',
            'message': 'Customer deleted successfully!',
        }
        return Response(res)
    qs = Customer.objects.filter(shop=shop)
    search = request.GET.get('search', None)
    if search:
        qs = qs.filter(Q(id__iexact=search) | Q(name__icontains=search) | Q(email__icontains=search))
    paginator = PageNumberPagination()
    paginator.page_size = 16
    result_page = paginator.paginate_queryset(qs, request)
    data= CustomerSerializer(result_page, many=True).data
    return paginator.get_paginated_response(data)
@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def leads(request, shop):
    if request.method == 'DELETE':
        Leads.objects.get(id=request.GET.get('id')).delete()
        res = {
            'class': 'success',
            'message': 'The Lead deleted successfully!',
        }
        return Response(res)
    id = request.GET.get('id', None)
    status = request.GET.get('status', None)
    if id and status:
        lead = Leads.objects.get(id=id)
        lead.status = status
        lead.save()
    qs = Leads.objects.filter(shop=shop).order_by('-id')
    search = request.GET.get('search', None)
    if search:
        qs = qs.filter(Q(id__iexact=search) | Q(name__icontains=search) | Q(email__icontains=search))
    paginator = PageNumberPagination()
    paginator.page_size = 16
    result_page = paginator.paginate_queryset(qs, request)
    data= LeadsSerializer(result_page, many=True).data
    return paginator.get_paginated_response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def subscribers(request, shop):
    if request.method == 'GET':
        qs = Subscriber.objects.filter(shop=shop)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= SubscriberSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Subscriber.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def contacts(request, shop):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            contact = Contact.objects.get(id=id)
            replies = ContactReply.objects.filter(contact=contact)
            data = ContactReplySerializer(replies, many=True).data
            return Response(data)
        qs = Contact.objects.filter(shop=shop)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ContactSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Contact.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        ContactReply.objects.create(contact=Contact.objects.get(id=data['id']), message=data['reply'])
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def coupons(request, shop):
    if request.method == 'GET':
        qs = Coupon.objects.filter(shop=shop)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= CouponSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Coupon.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        #  { "code": "asdfgasdg", "amount": 23, "type": "fixed", "valid_till": "2023-04-07", "error": "Please enter a coupon valid till date" }
        valid_till = None
        if data['valid_till']:
            valid_till = datetime.strptime(data['valid_till'], '%Y-%m-%d')
        print(valid_till)
        Coupon.objects.create(code=data['code'], amount=data['amount'], type=data['type'], valid_till=valid_till, shop=shop)
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        coupon = Coupon.objects.get(id=data['id'])
        coupon.code = data['code']
        coupon.discount = data['discount']
        coupon.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def orders(request, shop):
    if request.method == 'GET':
        oid = request.GET.get('oid', None)
        if oid:
            order = Order.objects.get(id=oid)
            data = OrderSerializer(order).data
            items = data['items']
            product_ids = [item['id'] for item in items]
            products = Product.objects.filter(pk__in=product_ids).order_by('-id')
            for product in products:
                item = next(item for item in items if item['id'] == product.pk)
                product.quantity = item['quantity']
            data['items'] = ProductSerializer(products, many=True).data
            statuses = Order_status.objects.filter(order=order).order_by('-id')
            data['statuses'] = OrderStatusSerializer(statuses, many=True).data
            print(data['statuses'])
            return Response(data)
        qs = Order.objects.filter(shop=shop).order_by('-id')
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(Q(id__iexact=search) | Q(address__first_name__icontains=search)| Q(address__last_name__icontains=search) | Q(address__email__icontains=search))
        paginator = PageNumberPagination()
        paginator.page_size = request.GET.get('limit', 16)
        result_page = paginator.paginate_queryset(qs, request)
        data= OrderSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)



@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def orderStatus(request, shop):
    if request.method == 'GET':
        unique_names = []
        unique_statuses = []
        all_statuses = Order_status.objects.filter(order__shop=shop)
        for status in all_statuses:
            if status.name not in unique_names:
                unique_names.append(status.name)
                unique_statuses.append(status)
        serializer = OrderStatusSerializer(unique_statuses, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        order=Order.objects.get(id=data['order_id'])
        Order_status.objects.create(name=data['name'], note=data['note'], order=order)
        if data['review'] and order.customer:
            print(order.items)
            reviewables = []
            for item in order.items:
                reviewables.append(item['id'])
            print(reviewables)
            order.customer.reviewables = list(set(order.customer.reviewables+reviewables))
            order.customer.save()
            if not order.is_completed:
                order.is_completed = True
                order.save()
                data = OrderSerializer(order).data
                items = data['items']
                print(55555555555)
                for item in items:
                    product = Product.objects.filter(id=item['id']).first()
                    if product:
                        product.sales += item['quantity']
                        product.save()
                        om = ShopPlugin.objects.filter(shop=shop, plugin__code='oxymanager', activated=True).first()
                        if product.oxymanager_id and om:
                            key = om.data['fields']['Key']['value']
                            url = 'https://www.oxymanager.com/nextoxy/api/product/'+str(product.oxymanager_id)+'?qty='+str(item['quantity'])+"&key="+key
                            headers = {
                                'Content-Type': 'application/json',
                            }
                            response = requests.request("GET", url, headers=headers)
                            print(response.text)

        return Response(200)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def reviews(request, shop):
    if request.method == 'GET':
        qs = Review.objects.filter(product__shop=shop)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ReviewSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Review.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = request.data
        review = Review.objects.get(id=data['id'])
        review.status = data['status']
        review.save()
        return Response(200)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def pages(request, shop):
    if request.method == 'GET':
        name = request.GET.get('name')
        if name:
            if name == 'privacy':
                page,ct = Page.objects.get_or_create(title='Privacy Policy', mandatory=True, slug='privacy-policy', shop=shop)
            elif name == 'terms':
                page,ct = Page.objects.get_or_create(title='Terms & Conditions', mandatory=True, slug='terms-and-conditions', shop=shop)
            elif name == 'refund':
                page,ct = Page.objects.get_or_create(title='Refund Policy', mandatory=True, slug='refund-policy', shop=shop)
            else:
                page = Page.objects.get(shop = shop, title=name)
            data = PageSerializer(page)
            return Response(data.data)
        qs = Page.objects.filter(shop=shop).order_by('-mandatory')
        paginator = PageNumberPagination()
        paginator.page_size = 20
        result_page = paginator.paginate_queryset(qs, request)
        data= PageSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Page.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'id' in data:
            page = Page.objects.get(id=data['id'])
        else:
            page = Page.objects.create(shop=shop)
        page.title = data['title']
        page.content = data['content']
        page.slug = data['slug']
        page.save()
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        page = Page.objects.get(id=data['id'])
        page.title = data['title']
        page.content = data['content']
        page.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def staffs(request, shop):
    if request.method == 'GET':
        staffs = Staff.objects.filter(shop=shop)
        data = StaffSerializer(staffs, many=True)
        return Response(data.data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Staff.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = json.loads(request.body)
        new = Staff.objects.create(name = data['name'], email = data['email'], phone = data['phone'], shop=shop)
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        staff = Staff.objects.get(id=data['id'])
        staff.name = data['name']
        staff.email = data['email']
        staff.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def packages(request, shop):
    qs = ThemePackage.objects.all().order_by('price')
    data= ThemePackageSerializer(qs, many=True, context={'shop': shop}).data
    return Response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def themes(request, shop):
    if request.method == 'GET':
        qs = Theme.objects.filter(active = True).order_by('-id')
        package = request.GET.get('package', None)
        if package and package.isnumeric():
            qs = qs.filter(package__id=package)
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(Q(name__icontains=search)| Q(description__icontains=search))
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ThemeSerializer(result_page, many=True, context={'shop': shop}).data
        return paginator.get_paginated_response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def shopthemes(request, shop):
    activate = request.GET.get('activate', None)
    if activate:
        currents = ShopTheme.objects.filter(activated=True,shop=shop)
        for current in currents:
            current.activated = False
            current.save()
        new, ct = ShopTheme.objects.get_or_create(theme_id=activate, shop=shop)
        new.activated = True
        new.save()
    # purchase = request.GET.get('purchase', None)
    # if purchase:
    #     theme = Theme.objects.get(id=purchase)
    #     inv = Invoice.objects.create(type='subscription', account = shop.account, payment_method=shop.account.payment_method, amount=theme.price, note="theme purchase", action="shopTheme", redirect='/ecommerce/settings/themes', action_ref1=shop.id, action_ref2=theme.id)
    #     if inv.payment_method == 'sp':
    #         return Response('/account/sp/'+str(inv.id),status=status.HTTP_201_CREATED)
    #     else:
    #         return Response('/account/stripe/'+str(inv.id),status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        qs = Theme.objects.filter(package=shop.package).order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ThemeSerializer(result_page, many=True, context={'shop': shop}).data
        return paginator.get_paginated_response(data)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        plan = ThemePackage.objects.get(id=data['planId'])
        if data['period'] == 'monthly':
            amount = plan.price
        else:
            amount = plan.yearly
        inv = Invoice.objects.create(type='subscription', account = shop.account, payment_method=data['method'], amount=amount, note="theme purchase", action="shopPackage", redirect='/ecommerce/subscription', action_ref1=shop.id, action_ref2=data['planId'])
        return Response(inv.id)
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     print(data)
    #     theme = Theme.objects.get(id=data['id'])
    #     shoptheme = ShopTheme.objects.create(theme=theme, shop=shop)
    #     return Response(status=status.HTTP_201_CREATED)
    # if request.method == 'PUT':
    #     data = json.loads(request.body)
    #     print(data)
    #     shoptheme = ShopTheme.objects.get(id=data['id'])
    #     shoptheme.active = data['active']
    #     shoptheme.save()
    #     return Response(status=status.HTTP_201_CREATED)
    # if request.method == 'DELETE':
    #     id = request.GET.get('id', None)
    #     ShopTheme.objects.filter(id=id).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def domains(request, shop):
    if request.method == 'GET':
        qs = shop.domains.all()
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= DomainSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        try:
            domain = Domain.objects.create(domain=data['domain'].strip(), account=shop.account)
            shop.domains.add(domain)
            record = Dns.objects.create(name='@', type='A', content='203.161.48.22', domain=domain, proxied = True)
            record2 = Dns.objects.create(name='www', type='CNAME', content=domain.domain, domain=domain, proxied = True)
            record3 = Dns.objects.create(name='@', type='MX', content='mail.nextoxy.com', domain=domain, proxied = False)
            Notification.objects.create(type="other", content="New domain has been added to your shop!", account=shop.account)
            send_mail('New domain has been added to your shop!', domain_add_message, [shop.account.email])
        except Exception as e:
            return Response({
                'code': 400,
                'msg': str(e)
            })
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Domain.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def records(request, shop):
    domain = request.GET.get('domain', None)
    domain=Domain.objects.get(id=domain)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        try:
            record = Dns.objects.create(name=data['name'], type=data['type'], content=data['value'], domain=domain)
        except Exception as e:
            return Response({
                'code': 400,
                'msg': str(e)
            })
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        record = Dns.objects.get(id=data['id'])
        record.name = data['name']
        record.type = data['type']
        record.content = data['content']
        record.save()
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Dns.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    qs = Dns.objects.filter(domain=domain)
    data = DnsSerializer(qs, many=True)
    return Response(data.data)


@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def templates(request, shop):
    if request.method == 'GET':
        template_actions = ['registration', 'forget_password', 'new_order', 'order_status', 'ticket_reply']
        for action in template_actions:
            if not EmailTemplate.objects.filter(shop=shop, action=action).exists():
                default = EmailTemplate.objects.get(shop__isnull=True, action=action)
                EmailTemplate.objects.create(shop=shop, action=action, subject=default.subject, body=default.body, variables = default.variables)
        action = request.GET.get('action')
        if action:
            template = EmailTemplate.objects.get(shop=shop, action=action)
            data = EmailTemplateSerializer(template)
            return Response(data.data)
        qs = EmailTemplate.objects.filter(shop=shop)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= EmailTemplateSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        template = EmailTemplate.objects.get(id=data['id'])
        template.subject = data['subject']
        template.body = data['body']
        template.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def plugins(request, shop):
    if request.method == 'GET':
        qs = Plugin.objects.filter()
        featured = request.GET.get('featured', None)
        if featured:
            installed = ShopPlugin.objects.filter(shop=shop)
            installed = [i.plugin.id for i in installed]
            print(installed)
            qs = qs.order_by('-featured').exclude(id__in=installed)
            if qs.count() < 5:
                qs = qs | Plugin.objects.filter()[:5-qs.count()]
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(name__icontains=search)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= PluginSerializer(result_page, many=True, context={'shop': shop}).data
        return paginator.get_paginated_response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def ShopPlugins(request, shop):
    pid = request.GET.get('install', None)
    if pid:
        ShopPlugin.objects.create(shop=shop, plugin=Plugin.objects.get(id=pid))
    spi = request.GET.get('uninstall', None)
    if spi:
        ShopPlugin.objects.filter(id=spi).delete()
    deactivate = request.GET.get('deactivate', None)
    if deactivate:
        sp = ShopPlugin.objects.get(id=deactivate)
        sp.activated = False
        sp.save()
    if request.method == 'GET':
        qs = ShopPlugin.objects.filter(shop=shop)
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(plugin__name__icontains=search)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ShopPluginSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'PUT':
        data = request.data
        print(data)
        sp = ShopPlugin.objects.get(id=data['id'])
        sp.data = data['data']
        sp.activated = True
        sp.save()
        if sp.activated:
            return Response(200)
        return Response(400)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def cjimport(request, shop):
    sku = request.GET.get('sku', None)
    cj = ShopPlugin.objects.get(shop=shop, plugin__code='cj', activated=True)
    accessToken = cj.data['accessToken']
    url = "https://developers.cjdropshipping.com/api2.0/v1/product/query?productSku="+sku
    header = {
        'Content-Type': 'application/json',
        'CJ-Access-Token': accessToken
    }
    res = requests.request("GET", url, headers=header)
    res = res.json()
    return Response(res)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def oxymanagerimport(request, shop):
    sku = request.GET.get('sku', None)
    om = ShopPlugin.objects.get(shop=shop, plugin__code='oxymanager', activated=True)
    key = om.data['fields']['Key']['value']
    url = "https://www.oxymanager.com/nextoxy/api/product/"+sku+"?key="+key
    header = {
        'Content-Type': 'application/json'
    }
    res = requests.request("GET", url, headers=header)
    try:
        res = res.json()
        res['success'] = True
        return Response(res)
    except:
        return Response({
            'message': 'Product not found'
        })

# http://127.0.0.1:8000/api/ecommerce/dash/oxymanagerupdate?pid=305&qty=4
@api_view(['GET', 'DELETE','POST', 'PUT'])
def oxymanagerupdate(request):
    pid = request.GET.get('pid', None)
    qty = request.GET.get('qty', None)
    if pid and qty:
        product = Product.objects.get(oxymanager_id=pid)
        if product and product.stock > int(qty):
            product.stock -= int(qty)
            product.save()
    return Response(200)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def ndsimport(request, shop):
    sku = request.GET.get('sku', None)
    om = ShopPlugin.objects.get(shop=shop, plugin__code='nds', activated=True)
    url = "https://nextdropshipping.com/api/product-details/"+sku
    header = {
        'Content-Type': 'application/json'
    }
    res = requests.request("GET", url, headers=header)
    print(res)
    try:
        res = res.json()
        res['success'] = True
        return Response(res)
    except:
        return Response({
            'message': 'Product not found'
        })
@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_shop
def onepage(request, shop):
    theme = ShopTheme.objects.filter(shop=shop, activated=True).first()
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        theme.data1 = data['data1']
        theme.data2 = data['data2']
        theme.save()
    data = {
        'data1': theme.data1,
        'data2': theme.data2
    }
    return Response(data)