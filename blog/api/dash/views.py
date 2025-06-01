from blog.models import Eblog, Category, Post, MediaFile, Theme, BlogTheme
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

from blog.decorators import get_blog

def strToFile(base64_str):
    format, imgstr = base64_str.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

@api_view(['GET', 'POST', 'PUT'])
@get_blog
def blog(request, blog):
    domain, created = Domain.objects.get_or_create(account=blog.account, subdomain=True, domain=blog.name.strip())
    blog.domains.add(domain)
    blog.save()
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'newLogo' in data:
            blog.logo = strToFile(data['newLogo'])
        if 'newFavicon' in data:
            blog.favicon = strToFile(data['newFavicon'])
        blog.title = data['title']
        blog.name = data['name']
        blog.email = data['email']
        blog.phone = data['phone']
        blog.street = data['street']
        blog.city = data['city']
        blog.state = data['state']
        blog.zip_code = data['zip_code']
        blog.country = data['country']
        blog.currency = data['currency']
        blog.save()
        return Response(200, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST'])
@get_blog
def posts(request, blog):
    if request.method == 'GET':
        detail = request.GET.get('detail', None)
        if detail:
            post = Post.objects.get(id=detail)
            data = PostSerializer(post).data
            return Response(data)
        posts = Post.objects.filter(blog=blog).order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 15
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        Post.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'POST':
        data = request.data
        if 'id' in data and data['id']:
            post = Post.objects.get(id=data['id'])
            post.title = data['title']
            post.content = data['content']
            post.meta = data['meta']
            post.highlight = data['highlight']
            post.trending = data['trending']
        else:
            post = Post.objects.create(blog=blog, title=data['title'], content=data['content'], meta=data['meta'], trending=data['trending'])
        cat = Category.objects.get(id=data['category'])
        post.category = cat
        post.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE','POST'])
@xframe_options_exempt
@get_blog
def MediaFiles(request, blog):
    if request.method == 'GET':
        qs = MediaFile.objects.filter(blog=blog).order_by('-id')
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
            new = MediaFile.objects.create(file=data, blog=blog)
            uploads.append(new.id)
        qs = MediaFile.objects.filter(id__in=uploads)
        data = MediaFileSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_blog
def themes(request, blog):
    if request.method == 'GET':
        qs = Theme.objects.all().order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ThemeSerializer(result_page, many=True, context={'blog': blog}).data
        return paginator.get_paginated_response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_blog
def blogthemes(request, blog):
    activate = request.GET.get('activate', None)
    if activate:
        currents = BlogTheme.objects.filter(activated=True,blog=blog)
        for current in currents:
            current.activated = False
            current.save()
        new = BlogTheme.objects.get(id=activate)
        new.activated = True
        new.save()
    purchase = request.GET.get('purchase', None)
    if purchase:
        theme = Theme.objects.get(id=purchase)
        inv = Invoice.objects.create(type='subscription', account = shop.account, payment_method=shop.account.payment_method, amount=theme.price, note="theme purchase", action="shopTheme", redirect='/ecommerce/settings/themes', action_ref1=shop.id, action_ref2=theme.id)
        if inv.payment_method == 'sp':
            return Response('/account/sp/'+str(inv.id),status=status.HTTP_201_CREATED)
        else:
            return Response('/account/stripe/'+str(inv.id),status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        qs = BlogTheme.objects.filter(blog=blog).order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= BlogThemeSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        theme = Theme.objects.get(id=data['id'])
        shoptheme = BlogTheme.objects.create(theme=theme, shop=shop)
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        shoptheme = BlogTheme.objects.get(id=data['id'])
        shoptheme.active = data['active']
        shoptheme.save()
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)
        BlogTheme.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'DELETE','POST', 'PUT'])
@get_blog
def categories(request, blog):
    if request.method == 'GET':
        qs = Category.objects.filter(blog=blog).order_by('-id')
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= CategorySerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)