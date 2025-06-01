from website.models import Website, Theme, WebsiteTheme
from core.models import Invoice
from .serializers import *
from core.models import Domain, Dns
from django.db.models import Count
import json, requests
import time
import base64
from django.core.files.base import ContentFile

from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from website.decorators import get_website

def strToFile(base64_str):
    format, imgstr = base64_str.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

@api_view(['GET', 'POST', 'PUT'])
@get_website
def website(request, website):
    domain, created = Domain.objects.get_or_create(account=website.account, subdomain=True, domain=website.name.strip())
    website.domains.add(domain)
    website.save()
    if request.method == 'GET':
        serializer = WebsiteSerializer(website)
        return Response(serializer.data)
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'newLogo' in data:
            website.logo = strToFile(data['newLogo'])
        if 'newFavicon' in data:
            website.favicon = strToFile(data['newFavicon'])
        website.title = data['title']
        website.name = data['name']
        website.email = data['email']
        website.phone = data['phone']
        website.street = data['street']
        website.city = data['city']
        website.state = data['state']
        website.zip_code = data['zip_code']
        website.country = data['country']
        website.currency = data['currency']
        website.save()
        return Response(200, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST'])
@get_website
def themes(request, website):
    if request.method == 'GET':
        qs = Theme.objects.all().order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ThemeSerializer(result_page, many=True, context={'website': website}).data
        return paginator.get_paginated_response(data)

@api_view(['GET', 'DELETE','POST'])
@get_website
def websitethemes(request, website):
    activate = request.GET.get('activate', None)
    if activate:
        currents = WebsiteTheme.objects.filter(activated=True,website=website)
        for current in currents:
            current.activated = False
            current.save()
        new = WebsiteTheme.objects.get(id=activate)
        new.activated = True
        new.save()
    purchase = request.GET.get('purchase', None)
    if purchase:
        theme = Theme.objects.get(id=purchase)
        inv = Invoice.objects.create(type='subscription', account = website.account, payment_method=website.account.payment_method, amount=theme.price, note="theme purchase", action="websiteTheme", redirect='/ecommerce/settings/themes', action_ref1=website.id, action_ref2=theme.id)
        if inv.payment_method == 'sp':
            return Response('/account/sp/'+str(inv.id),status=status.HTTP_201_CREATED)
        else:
            return Response('/account/stripe/'+str(inv.id),status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        qs = WebsiteTheme.objects.filter(website=website).order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= WebsiteThemeSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        theme = Theme.objects.get(id=data['id'])
        websitetheme = WebsiteTheme.objects.create(theme=theme, website=website)
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        websitetheme = WebsiteTheme.objects.get(id=data['id'])
        websitetheme.active = data['active']
        websitetheme.save()
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        WebsiteTheme.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
