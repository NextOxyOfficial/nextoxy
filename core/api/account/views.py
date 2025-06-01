from django.contrib.auth.models import User
from core.models import Account, Invoice, Service_order
from ecommerce.models import *
from blog.models import *
# from website.models import *
from .serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .paypal import makePaypalPayment
from .stripe import makeStripePayment
from .sp import makeSpPayment, verifySpPayment

from datetime import datetime, timedelta
from rest_framework.pagination import PageNumberPagination
from core.notification.notif import notify
import base64
from django.core.files.base import ContentFile
import requests, json, xmltodict

from core.models import Blog, BlogCategory, MediaFile, Notification
from core.mailing import send_mail
from core.mail_templates import shop_added_message, profile_updated_message, billing_message



@api_view(['GET', 'POST'])
def ecommerce(request):
    user = request.user
    delete = request.GET.get('delete', None)
    if delete is not None:
        shop = Shop.objects.get(id=int(delete), account=user.account)
        shop.domains.all().delete()
        shop.delete()
        # try:
        # except Exception as ex:
        #     print(ex)
    check = request.GET.get('check', None)
    if check:
        if Shop.objects.filter(name=check).exists():
            return Response('exists', status=status.HTTP_200_OK)
        return Response('not exists', status=status.HTTP_200_OK)

    if request.method == 'GET':
        shops = Shop.objects.filter(account=user.account).order_by('-id')
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        shop = Shop (
            account = user.account,
            name = data['shopName']
        )
        shop.save()
        shop_added_message2 = shop_added_message.replace('[myshop]', shop.name)
        send_mail('New Shop Created!', shop_added_message2, [user.email])
        return Response(200)
@api_view(['GET', 'POST'])
def business(request):
    user = request.user
    delete = request.GET.get('delete', None)
    if delete is not None:
        shop = Shop.objects.get(id=int(delete), account=user.account)
        shop.domains.all().delete()
        shop.delete()
        # try:
        # except Exception as ex:
        #     print(ex)
    check = request.GET.get('check', None)
    if check:
        if Shop.objects.filter(name=check).exists():
            return Response('exists', status=status.HTTP_200_OK)
        return Response('not exists', status=status.HTTP_200_OK)

    if request.method == 'GET':
        shops = Shop.objects.filter(account=user.account).order_by('-id')
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        shop = Shop (
            account = user.account,
            name = data['shopName']
        )
        shop.save()
        shop_added_message2 = shop_added_message.replace('[myshop]', shop.name)
        send_mail('New Shop Created!', shop_added_message2, [user.email])
        return Response(200)
    
@api_view(['GET', 'POST'])
def eblog(request):
    user = request.user
    if request.method == 'GET':
        shops = Eblog.objects.filter(account=user.account)
        serializer = EblogSerializer(shops, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        shop = Eblog (
            account = user.account,
            name = data['blogName']
        )
        shop.save()
        return Response(200)
@api_view(['GET', 'POST'])
def website(request):
    user = request.user
    if request.method == 'GET':
        shops = Website.objects.filter(account=user.account)
        serializer = WebsiteSerializer(shops, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        shop = Website (
            account = user.account,
            name = data['websiteName']
        )
        shop.save()
        return Response(200)

@api_view(['GET', 'POST'])
def blog(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        if data['image'] and ';base64,' in data['image']:
            base64_data = data['image']
            format, imgstr = base64_data.split(';base64,')
            ext = format.split('/')[-1]
            data['image'] = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        elif data['image']:
            data['image'] = 'unchanged'
        else:
            data['image'] = None
        if data['id']:
            bl = Blog.objects.get(id=data['id'])
            bl.title = data['title']
            bl.content = data['content']
            bl.type = data['type']
            bl.author = data['author']
            bl.category = BlogCategory.objects.filter(name=data['category__name']).first()
            if data['image'] != 'unchanged':
                bl.image = data['image']
            bl.save()
            return Response(200)

        else:
            bl = Blog (
                title = data['title'],
                content = data['content'],
                category = BlogCategory.objects.filter(name=data['category__name']).first(),
                image = data['image'],
                type = data['type'],
                author = data['author']
            )
            bl.save()
            return Response(200)
    
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            qs = Blog.objects.get(id=id)
            data = BlogDetailsSerializer(qs).data
            return Response(data)
        delete = request.GET.get('delete', None)
        if delete:
            Blog.objects.get(id=delete).delete()
            
        qs = Blog.objects.all().order_by('-id')
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(title__icontains=search)
        cid = request.GET.get('cid', None)
        if cid:
            qs = qs.filter(category__id=cid)
        type = request.GET.get('type', None)
        if type and type == 'new':
            qs = qs.order_by('-id')
        elif type:
            qs = qs.filter(type=type)
        paginator = PageNumberPagination()
        limit = request.GET.get('limit', 16)
        paginator.page_size = limit
        result_page = paginator.paginate_queryset(qs, request)
        data= BlogSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    
@api_view(['GET', 'POST'])
def blog_category(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        data = [{'name': category.name} for category in categories]

    return Response(data)

@api_view(['GET', 'POST'])
def profile(request):
    user = request.user
    print(user.account)
    if request.method == 'GET':
        serializer = AccountSerializer(user.account)
        print(serializer.data)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        instance = user.account
        serializer = AccountSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            Notification.objects.create(type="account", content="Your profile information has been updated", account=user.account)
            send_mail('Profile updated!', profile_updated_message, [user.account.email])
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(200)

@api_view(['GET', 'POST'])
def password(request):
    user = request.user
    if request.method == 'POST':
        data = request.data
        if user.check_password(data['old']):
            user.set_password(data['new'])
            user.save()
            return Response('success',status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def invoices(request):
    user = request.user
    cancel = request.GET.get('cancel', None)
    if cancel:
        inv = Invoice.objects.get(id=cancel, account=user.account)
        inv.cancelled = True
        inv.save()
    invId = request.GET.get('id', None)
    if request.method == 'POST':
        data = request.data
        invoice = Invoice.objects.get(id=invId, account=user.account)
        invoice.payment_method = data['method']
        invoice.order_id = ''
        invoice.save()
        account =request.user.account
        account.billing_first_name = data['billing_first_name']
        account.billing_last_name = data['billing_last_name']
        account.billing_email = data['billing_email']
        account.billing_phone_number = data['billing_phone_number']
        account.billing_address = data['billing_address']
        account.billing_city = data['billing_city']
        account.billing_state = data['billing_state']
        account.billing_country = data['billing_country']
        account.save()
        data= InvoiceSerializer(invoice).data
        return Response(data)
    if request.method == 'GET':
        if invId:
            invoice = Invoice.objects.get(id=invId, account=user.account)
            data= InvoiceSerializer(invoice).data
            return Response(data)
        filter = request.GET.get('filter', None)
        if filter == 'due':
            invoices = Invoice.objects.filter(account=user.account, due=True)
        elif filter == 'settled':
            invoices = Invoice.objects.filter(account=user.account, due=False)
        else:
            invoices = Invoice.objects.filter(account=user.account)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(invoices.order_by('-id'), request)
        data= InvoiceSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    return Response(200)

# for stripe

@api_view(['GET', 'POST'])
def stripePay(request, id):
    user = request.user
    if request.method == 'GET':
        invoice = Invoice.objects.get(id=id, account=user.account)
        res = makeStripePayment(invoice)
        return Response(res)
    return Response(200)
@api_view(['GET', 'POST'])
def paypalPay(request, id):
    user = request.user
    if request.method == 'GET':
        invoice = Invoice.objects.get(id=id, account=user.account)
        status, payment_id, approval_url = makePaypalPayment(invoice)
        return Response({
            'url': approval_url
        })
    return Response(200)

def handlePaidAction(inv):
    Notification.objects.create(type="other", content="Payment successful!", account=inv.account)
    send_mail('Payment successful', billing_message, [inv.account.email])
    if inv.action == 'shopTheme': #should be removed
        # action="shopTheme", action_ref1=shop.id, action_ref2=theme.id
        shop = Shop.objects.get(id = inv.action_ref1)
        theme = Theme.objects.get(id = inv.action_ref2)
        st, ct = ShopTheme.objects.get_or_create(shop=shop, theme=theme)
        st.valid_till = datetime.now() + timedelta(days=30)
        st.save()
    if inv.action == 'shopPackage':
        shop = Shop.objects.get(id = inv.action_ref1)
        package = ThemePackage.objects.get(id = inv.action_ref2)
        shop.package = package
        shop.package_validity = datetime.now() + timedelta(days=30)
        shop.save()
    if inv.action == 'service':
        service = Service_order.objects.get(id = inv.action_ref1)
        service.paid = True
        service.save()
        

@api_view(['GET', 'POST'])
def stripeVerify(request):
    # {'id': 'evt_1MsNzkCOzgULzFM39mLckz3C', 'object': 'event', 'api_version': '2022-11-15', 'created': 1680430722, 'data': {'object': {'id': 'sub_1MsNziCOzgULzFM3ahrFiAhs', 'object': 'subscription', 'application': None, 'application_fee_percent': None, 'automatic_tax': {'enabled': False}, 'billing_cycle_anchor': 1680430722, 'billing_thresholds': None, 'cancel_at': None, 'cancel_at_period_end': False, 'canceled_at': None, 
    # 'cancellation_details': {'comment': None, 'feedback': None, 'reason': None}, 'collection_method': 'charge_automatically', 'created': 1680430722, 'currency': 'usd', 'current_period_end': 1683022722, 'current_period_start': 1680430722, 'customer': 'cus_NdfKuJWG1SaILY', 'days_until_due': None, 'default_payment_method': None, 'default_source': None, 'default_tax_rates': [], 'description': None, 'discount': None, 'ended_at': None, 'items': {'object': 'list', 'data': [{'id': 'si_NdfKjCCLLwwSox', 'object': 'subscription_item', 'billing_thresholds': None, 'created': 1680430722, 'metadata': {}, 'plan': {'id': 'price_1MsNyHCOzgULzFM3ZGAGqSHr', 'object': 'plan', 'active': False, 'aggregate_usage': None, 'amount': 1000, 'amount_decimal': '1000', 'billing_scheme': 'per_unit', 'created': 1680430633, 'currency': 'usd', 'interval': 'month', 'interval_count': 1, 'livemode': False, 'metadata': {}, 'nickname': None, 'product': 'prod_NLHAY2GANX56vC', 
    # 'tiers_mode': None, 'transform_usage': None, 'trial_period_days': None, 'usage_type': 'licensed'}, 'price': {'id': 'price_1MsNyHCOzgULzFM3ZGAGqSHr', 'object': 'price', 'active': False, 'billing_scheme': 'per_unit', 'created': 1680430633, 'currency': 'usd', 'custom_unit_amount': None, 'livemode': False, 'lookup_key': None, 'metadata': {}, 'nickname': None, 'product': 'prod_NLHAY2GANX56vC', 'recurring': {'aggregate_usage': None, 'interval': 'month', 'interval_count': 1, 'trial_period_days': None, 'usage_type': 'licensed'}, 'tax_behavior': 'unspecified', 'tiers_mode': None, 'transform_quantity': None, 'type': 'recurring', 'unit_amount': 1000, 'unit_amount_decimal': '1000'}, 'quantity': 1, 'subscription': 'sub_1MsNziCOzgULzFM3ahrFiAhs', 'tax_rates': []}], 'has_more': False, 'total_count': 1, 'url': '/v1/subscription_items?subscription=sub_1MsNziCOzgULzFM3ahrFiAhs'}, 'latest_invoice': 'in_1MsNziCOzgULzFM3VYmRnOkO', 'livemode': False, 'metadata': {}, 'next_pending_invoice_item_invoice': None, 'on_behalf_of': None, 'pause_collection': None, 
    # 'payment_settings': {'payment_method_options': None, 'payment_method_types': None, 'save_default_payment_method': 'off'}, 'pending_invoice_item_interval': None, 'pending_setup_intent': None, 'pending_update': None, 'plan': {'id': 'price_1MsNyHCOzgULzFM3ZGAGqSHr', 'object': 'plan', 'active': False, 'aggregate_usage': None, 'amount': 1000, 'amount_decimal': '1000', 'billing_scheme': 'per_unit', 'created': 1680430633, 'currency': 'usd', 'interval': 'month', 'interval_count': 1, 'livemode': False, 'metadata': {}, 'nickname': None, 'product': 'prod_NLHAY2GANX56vC', 'tiers_mode': None, 'transform_usage': None, 'trial_period_days': None, 'usage_type': 'licensed'}, 'quantity': 1, 'schedule': None, 'start_date': 1680430722, 'status': 
    # 'incomplete', 'test_clock': None, 'transfer_data': None, 'trial_end': None, 'trial_settings': {'end_behavior': {'missing_payment_method': 'create_invoice'}}, 'trial_start': None}}, 'livemode': False, 'pending_webhooks': 3, 'request': {'id': 'req_KHxL8loqHLu6yv', 'idempotency_key': '3d355beb-5fa6-4cef-8a2f-f4f2869435e0'}, 'type': 'customer.subscription.created'}
    if request.method == 'POST':
        form_data = request.data
        print(form_data)
        status = form_data['data']['object']['payment_status']
        total = form_data['data']['object']['amount_total']
        invId = form_data['data']['object']['client_reference_id']
        subId = form_data['data']['object']['id']
        if status == 'paid':
            inv = Invoice.objects.get(id = invId, paid = False, completed = False)
            inv.paid = True
            inv.subscription_id = subId
            inv.completed = True
            print(inv.action, inv.action_ref1)
            inv.save()
            handlePaidAction(inv)
    return Response(200)

@api_view(['GET', 'POST'])
def spPay(request, id):
    user = request.user
    if request.method == 'GET':
        invoice = Invoice.objects.get(id=id, account=user.account)
        if not invoice.order_id:
            print('making payment link')
            res = makeSpPayment(invoice)
            if 'checkout_url' in res:
                order_id = res['sp_order_id']
                invoice.order_id = order_id
                invoice.save()
                return Response({'url' : res['checkout_url']}, status=status.HTTP_200_OK)
        else:
            res = verifySpPayment(invoice.order_id)
            print(res)
            print(res['sp_code'])
            if res['sp_code'] == '1000' or res['sp_code'] == 1000:
                print(res['sp_code'])
                invoice.paid = True
                invoice.completed = True
                invoice.save()
                handlePaidAction(invoice)
                return Response({'url' : invoice.redirect}, status=status.HTTP_200_OK)
            return Response(300)
    return Response(210)

@api_view(['GET', 'DELETE','POST'])
def MediaFiles(request):
    if request.method == 'GET':
        qs = MediaFile.objects.all().order_by('-id')
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
            new = MediaFile.objects.create(file=data)
            uploads.append(new.id)
        qs = MediaFile.objects.filter(id__in=uploads)
        data = MediaFileSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST'])
def service(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        ns = Service_order.objects.create(
            account = request.user.account,
            data = data,
            amount = data['amount'],
            type = data['type'],
            title = data['title'],
        )
        inv = Invoice.objects.create(type='payment', account = request.user.account, payment_method=data['method'], amount=data['amount'], note=data['title'], action="service", redirect='/account', action_ref1=ns.id)
        ns.invoice_id = inv.id
        ns.invoice_method = inv.payment_method
        ns.save()
        notify(request.user.account,None,None,2)
        return Response(inv.id)
    qs = Service_order.objects.filter(account = request.user.account).order_by('-id')
    type = request.GET.get('type', None)
    if type:
        qs = qs.filter(type=type)
    paginator = PageNumberPagination()
    paginator.page_size = 16
    result_page = paginator.paginate_queryset(qs, request)
    data= Service_orderSerializer(result_page, many=True).data
    return paginator.get_paginated_response(data)



@api_view(['GET', 'DELETE','POST'])
def domains(request):
    account = request.user.account
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        # {'domain': 'adsfasvsdg.com', 'duration': '4', 'amount': '52.22'}
        inv = Invoice.objects.create(type='payment', account = account, amount=data['amount'], note="Domain Purchase", action="domain", redirect='/account/services/domains', action_ref1=data['domain'])
        return Response(inv.id)
    priceUrl = 'https://api.namecheap.com/xml.response?ApiUser=nextoxy&ApiKey=629c2b3065af49289e813b4bf5074378&UserName=nextoxy&ClientIp=118.179.34.243&Command=namecheap.users.getPricing&ProductType=DOMAIN&ProductName='
    checkUrl = 'https://api.namecheap.com/xml.response?ApiUser=nextoxy&ApiKey=629c2b3065af49289e813b4bf5074378&UserName=nextoxy&ClientIp=118.179.34.243&Command=namecheap.domains.check&DomainList='
    tld = request.GET.get('tld')
    domain = request.GET.get('domain')
    if tld and domain:
        response = requests.get(checkUrl+domain)
        xml_data = response.text
        data_dict = xmltodict.parse(xml_data)['ApiResponse']['CommandResponse']['DomainCheckResult']
        if not '@Available' in data_dict or data_dict['@Available'] == 'false':
            return Response(404)
        response2 = requests.get(priceUrl+tld)
        xml_data2 = response2.text
        data_dict2 = xmltodict.parse(xml_data2)
        resp = {
            'check': data_dict,
            'rates': data_dict2['ApiResponse']['CommandResponse']['UserGetPricingResult']['ProductType']['ProductCategory']
        }
        return JsonResponse(resp, safe=False)
    else:
        return Response(404)

@api_view(['GET', 'POST'])
def fb_tokens(request):
    account = request.user.account
    if request.method == 'POST':
        token = request.data['token']
        tokens = account.fb_tokens
        if not token in tokens:
            tokens.append(token)
            account.fb_tokens = tokens
            account.save()
    
    return Response(200)