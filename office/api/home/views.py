from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from office.models import Custom_order

@api_view(['GET', 'DELETE','POST', 'PUT'])
def contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(888)

@api_view(['GET', 'DELETE','POST', 'PUT'])
def customOrder(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        new = Custom_order.objects.create(
            f_name = data['fname'],
            l_name = data['lname'],
            email = data['email'],
            phone = data['phone'],
            message = data['message'],
            data = data
        )
    qs = Custom_order.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 16
    result_page = paginator.paginate_queryset(qs, request)
    data= Custom_orderSerializer(result_page, many=True).data
    return paginator.get_paginated_response(data)