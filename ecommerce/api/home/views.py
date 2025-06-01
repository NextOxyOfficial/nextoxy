from ecommerce.models import Theme, Plugin, ThemePackage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import *


@api_view(['GET', 'DELETE','POST', 'PUT'])
def packages(request):
    qs = ThemePackage.objects.all().order_by('price')
    data= ThemePackageSerializer(qs, many=True).data
    return Response(data)

@api_view(['GET', 'DELETE','POST', 'PUT'])
def themes(request):
    if request.method == 'GET':
        qs = Theme.objects.filter(active = True).order_by('-id')
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(name__icontains=search)
        package = request.GET.get('package', None)
        if package and package.isnumeric():
            qs = qs.filter(package__id=package)
        
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= ThemeSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)


@api_view(['GET', 'DELETE','POST', 'PUT'])
def plugins(request):
    if request.method == 'GET':
        qs = Plugin.objects.filter()
        featured = request.GET.get('featured', None)
        if featured:
            qs = qs.order_by('-featured')
        search = request.GET.get('search', None)
        if search:
            qs = qs.filter(name__icontains=search)
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= PluginSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)