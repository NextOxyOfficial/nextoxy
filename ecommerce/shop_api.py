from ecommerce.models import Shop, Banner, Blog, Menu, MenuItem, Section, Category, Brand, Tag, ShippingProfile, Product, ProductImage, VariantSuggestion, ProductVariant, Review, Customer, Address, Order_status, Order, MediaFile
from ecommerce.models import Page, Staff, Subscriber, Coupon, Edit, ShopPlugin
from django.contrib.auth.models import User
from .serializers import *
from core.models import Domain
import requests
import json
import stripe
import base64
from django.core.files.base import ContentFile

from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from ecommerce.decorators import get_shop2
from core.notification.notif import notify

from core.models import Account, Notification


@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def products(request, shop, theme):
    highlight = request.GET.get('highlight')
    if highlight:
        products = Product.objects.filter(highlight=highlight, shop=shop)
    else:
        products = Product.objects.filter(shop=shop)
    for product in products:
        product.quantity = 1
    paginator = PageNumberPagination()
    paginator.page_size = 1
    result_page = paginator.paginate_queryset(products, request)
    data= ProductSerializer(result_page, many=True).data
    return paginator.get_paginated_response(data)


@api_view(['GET'])
@get_shop2
def detail(request, shop, theme):
    id = request.GET.get('id')
    product = Product.objects.get(id=id, shop=shop)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)
@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def cart(request, shop, theme):
    print(shop)
    if request.method == 'POST':
        cart_items = request.data
        print(cart_items)
        product_ids = [item['id'] for item in cart_items]
        products = Product.objects.filter(pk__in=product_ids)
        for product in products:
            item = next(item for item in cart_items if item['id'] == product.pk)
            product.quantity = item['quantity']
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    return Response({'shop': shop.name})

@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def wish(request, shop, theme):
    print(shop)
    if request.method == 'POST':
        cart_items = request.data
        print(cart_items)
        product_ids = [item['id'] for item in cart_items]
        products = Product.objects.filter(pk__in=product_ids)
        for product in products:
            item = next(item for item in cart_items if item['id'] == product.pk)
            product.quantity = 1
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    return Response({'shop': shop.name})


@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def subscribe(request, shop, theme):
    if request.method == 'POST':
        data = request.data
        print(data)
        new_sub, ct = Subscriber.objects.get_or_create(
            email=data['email'],
            shop=shop,
        )
        if ct:
            Notification.objects.create(type="other", content="New subscriber in your shop "+shop.name, account=shop.account)
        return Response(200)
    return Response({'shop': shop.name})

@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def review(request, shop, theme):
    if request.method == 'POST':
        # product = Product.objects.get(pk=pk)
        data = request.data
        print(data)
        prd = Product.objects.get(id=data['product'])
        customer = Customer.objects.get(user= User.objects.get(id =data["customer"]))
        new_review = Review.objects.create(product = prd, customer= customer, review=data["review"])
        Notification.objects.create(type="review", content="New review in your shop "+shop.name, account=shop.account)
        return Response(200)
    return Response({'shop': shop.name})

@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def checkout(request, shop, theme):
    if request.method == 'POST':
        data = request.data
        userid = request.GET.get('userid', None)
        customer = None
        if userid and userid != 'None':
            customer = Customer.objects.get(user__id=userid)
        new_adr = Address.objects.create(
            customer=customer,
            first_name=data['shipping']['first_name'],
            last_name=data['shipping']['last_name'],
            email=data['shipping']['email'],
            phone=data['shipping']['phone'],
            street_address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zip_code=data['shipping']['zip_code'],
            country=data['shipping']['country'],
        )
        new_ord = Order.objects.create(
            customer=customer,
            shop=shop,
            items=data['cart'],
            shipping = data['delivery'],
            total = data['total'],
            address=new_adr,
        )
        notify(shop.account,None,None,3)
        Notification.objects.create(type="order", content="New order in your shop "+shop.name, account=shop.account)
        print(new_adr, new_ord, 5555)
        coupon = data['coupon']
        if coupon:
            coupon = Coupon.objects.filter(code=coupon).first()
            if coupon:
                if coupon.type == 'fixed':
                    new_ord.discount = coupon.amount
                elif coupon.type == 'percent':
                    new_ord.discount = new_ord.total * coupon.amount / 100
                new_ord.save()
        payment_plugin_id = data['method']
        success_url = '/tracking?tracking='+str(new_ord.id)
        if payment_plugin_id:
            payment_plugin = ShopPlugin.objects.get(id=payment_plugin_id)
            if payment_plugin.plugin.code == 'stripe':
                stripe.api_key = payment_plugin.data['fields']['key']['value']
                domain = payment_plugin.data['fields']['domain']['value']
                if domain.find('http') == -1:
                    domain = 'https://' + domain
                
                rounded_amount = round(new_ord.total, 2)
                formatted_amount = "{:.2f}".format(rounded_amount)
                stripe_price = int(str(formatted_amount).replace('.', ''))
                print(stripe_price)
                checkout_session = stripe.checkout.Session.create(
                    success_url=domain+success_url,
                    cancel_url=domain+'/',
                    client_reference_id=str(new_ord.id),
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'price_data': {
                                'currency': 'usd',
                                'product_data': {
                                    'name': 'Stubborn Attachments',
                                    'images': ['https://i.imgur.com/EHyR2nP.png'],
                                },
                                'unit_amount': stripe_price,
                            },
                            'quantity': 1,
                        },
                    ]
                )
                return Response(checkout_session.url)
            elif payment_plugin.plugin.code == 'paypal':
                print('paypal', 88888)
                # url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
                url = "https://api-m.paypal.com/v1/oauth2/token"
                client_id = payment_plugin.data['fields']['cid']['value']
                client_secret = payment_plugin.data['fields']['secret']['value']
                domain = payment_plugin.data['fields']['domain']['value']
                if domain.find('http') == -1:
                    domain = 'https://' + domain
                headers = {"Content-Type": "application/x-www-form-urlencoded"}
                data = {"grant_type": "client_credentials"}

                response = requests.post(url, auth=(client_id, client_secret), headers=headers, data=data)
                access_token = response.json()['access_token']
                print(access_token)

                headers = {
                    'Content-Type': 'application/json',
                    'PayPal-Request-Id': 'nx'+str(new_ord.id),
                    'Authorization': 'Bearer '+access_token,
                }

                data = {
                    "intent": "CAPTURE",
                    "purchase_units": [
                        {
                            "reference_id": "nx-"+str(new_ord.id),
                            "amount": {
                                "currency_code": "USD",
                                "value": str(new_ord.total),
                            },
                        },
                    ],
                    "application_context": {
                        "brand_name": domain,
                        "locale": "en-US",
                        "landing_page": "LOGIN",
                        "shipping_preference": "NO_SHIPPING",
                        "user_action": "PAY_NOW",
                        "return_url": domain+success_url,
                        "cancel_url": domain+'/',
                    },
                }
                jsonData = json.dumps(data)
                print(jsonData)
                # url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
                url = "https://api-m.paypal.com/v2/checkout/orders"
                response = requests.post(url, headers=headers, data=jsonData)
                print(response.json())
                checkout_link = response.json()['links'][1]['href']
                return Response(checkout_link)
            elif payment_plugin.plugin.code == 'sp':
                # url = 'https://sandbox.shurjopayment.com/api/get_token'
                # url2 = 'https://sandbox.shurjopayment.com/api/secret-pay'
                url = 'https://engine.shurjopayment.com/api/get_token'
                url2 = 'https://engine.shurjopayment.com/api/secret-pay'
                username = payment_plugin.data['fields']['Username']['value']
                password = payment_plugin.data['fields']['xPassword']['value']
                domain_url = request.META['HTTP_HOST']
                print(username, password, domain_url)
                result  = requests.post(url, data={ "username":username, "password":password })
                result = result.json()
                token = result['token']
                store_id = result['store_id']
                print(token)
                hed = {'Authorization': 'Bearer ' + token}

                data = {
                    "token": token,
                    "store_id": store_id,
                    "prefix": "LST",
                    "currency": "USD",
                    "return_url": 'https://'+ domain_url+success_url,
                    "cancel_url": 'https://'+ domain_url+'/',
                    "amount": str(new_ord.total),
                    "order_id": "order-"+str(new_ord.id),
                    "discsount_amount": "0",
                    "disc_percent": "0",
                    "client_ip": "118.179.34.243",
                    "customer_name": 'Unknown',
                    "customer_phone": '01711123456',
                    "customer_email": 'support@nextoxy.com',
                    "customer_address": 'Unknown',
                    "customer_city": 'Unknown',
                    "customer_state": 'Unknown',
                    "customer_postcode": '12345',
                    "customer_country": 'Unknown',
                }

                result = requests.post(url2, json=data, headers=hed)
                return Response(result.json()['checkout_url'])
            else:
                return Response(success_url)
    return Response({'shop': shop.name})

@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def shipping(request, shop, theme):
    country = request.GET.get('country', None)
    state = request.GET.get('state', None)
    city = request.GET.get('city', None)
    if request.method == 'POST':
        products = request.data
        charges = []
        for product in products:
            shipping_data = {'to': 0, 'from': 0, 'charge': 0}
            product = Product.objects.get(id=product['id'])
            if product.shipping and product.shipping.data:
                data = product.shipping.data
                print(data)
                # set default as fallback 
                shipping_data['to'] = data['default'].get('to', shipping_data['to'])
                shipping_data['from'] = data['default'].get('from', shipping_data['from'])
                shipping_data['charge'] = data['default'].get('charge', shipping_data['charge'])
                # check if country is in shipping data
                if country and country in data:
                    shipping_data['to'] = data[country].get('to', shipping_data['to'])
                    shipping_data['from'] = data[country].get('from', shipping_data['from'])
                    shipping_data['charge'] = data[country].get('charge', shipping_data['charge'])
                    # check if state is in shipping data
                    if state and state in data:
                        shipping_data['to'] = data[state].get('to', shipping_data['to'])
                        shipping_data['from'] = data[state].get('from', shipping_data['from'])
                        shipping_data['charge'] = data[state].get('charge', shipping_data['charge'])
                        # check if city is in shipping data
                        if city and city in data:
                            shipping_data['to'] = data[city].get('to', shipping_data['to'])
                            shipping_data['from'] = data[city].get('from', shipping_data['from'])
                            shipping_data['charge'] = data[city].get('charge', shipping_data['charge'])

            charges.append(shipping_data)
            # get which has to high charge 
            highest = max(charges, key=lambda x:x['charge'])
            return Response(highest)
@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def coupon(request, shop, theme):
    response = 404
    code = request.GET.get('code')
    if code:
        coupon = Coupon.objects.filter(shop=shop, code=code).first()
        if coupon:
            response = {'amount': coupon.amount, "type": coupon.type }
    return Response(response)


@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def editor(request, shop, theme):
    edit, ct = Edit.objects.get_or_create(shop=shop)
    if request.method == 'POST':
        data = request.data
        if not edit.content:
            json_data = []
        else:
            json_data = edit.content
        if data['type'] == 'text':
            # {'id': 'home-hero-1746', 'text': 'Hello s asdfasdfa', 'type': 'text'}
            
            # check if id already exists in the list of dictionaries
            found = False
            for d in json_data:
                if d.get('id') == data.get('id'):
                    d['text'] = data.get('text')
                    d['type'] = data.get('type')
                    found = True
                    break
        
            # if id not found, append a new dictionary
            if not found:
                json_data.append(data)
        if data['type'] == 'link':
            # {'id': 'home-hero-1746', 'text': 'Hello s asdfasdfa', 'type': 'text'}
            
            # check if id already exists in the list of dictionaries
            found = False
            for d in json_data:
                if d.get('id') == data.get('id'):
                    d['text'] = data.get('text')
                    d['link'] = data.get('link')
                    found = True
                    break
        
            # if id not found, append a new dictionary
            if not found:
                json_data.append(data)
        if data['type'] == 'youtube':
            link = data.get('link')
            if link:
                link = link.replace('watch?v=', 'embed/')
                link = link.replace('youtu.be/', 'youtube.com/embed/')
                data['link'] = link
            # {'id': 'home-hero-1746', 'text': 'Hello s asdfasdfa', 'type': 'text'}
            
            # check if id already exists in the list of dictionaries
            found = False
            for d in json_data:
                if d.get('id') == data.get('id'):
                    d['link'] = data.get('link')
                    found = True
                    break
        
            # if id not found, append a new dictionary
            if not found:
                json_data.append(data)
        elif data['type'] == 'image' and data['image']:
            base64_str = data['image']
            format, imgstr = base64_str.split(';base64,')
            ext = format.split('/')[-1]
            new_media = MediaFile.objects.create(
                shop=shop,
                file=ContentFile(base64.b64decode(imgstr), name=f'{data["id"]}.{ext}'),
            )
            url = new_media.file.url
            data['image'] = url
            # check if id already exists in the list of dictionaries
            found = False
            for d in json_data:
                if d.get('id') == data.get('id'):
                    d['type'] = data.get('type')
                    d['image'] = url
                    found = True
                    break
        
            # if id not found, append a new dictionary
            if not found:
                json_data.append(data)
        
        edit.content = json_data
        edit.save()
        return Response(edit.content)
    return Response(edit.content)

@api_view(['GET', 'POST', 'PUT'])
@get_shop2
def filter_products(request, shop, theme):
    highlight = request.GET.get('highlight')
    if highlight:
        products = Product.objects.filter(highlight=highlight, shop=shop)
    else:
        products = Product.objects.filter(shop=shop)
    for product in products:
        product.quantity = 1
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)