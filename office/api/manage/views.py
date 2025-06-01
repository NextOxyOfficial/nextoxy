from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ecommerce.models import Shop, Product, ShopTheme
from core.models import Account, Service_order, Ticket, TicketMessage
from datetime import datetime
from office.models import Staff, Product, Order
from .serializers import *
from core.utils import strToFile

@api_view(['GET', 'DELETE','POST', 'PUT'])
def overview(request):
    data = {
        'accounts': 0,
        'shops': 0,
        'active-shops': 0,
        'products': 0,
    }
    if request.method == 'GET':
        data['accounts'] = Account.objects.all().count()
        data['shops'] = Shop.objects.all().count()
        data['products'] = Product.objects.all().count()
        # active shop which has ShopTheme child with valid_till is less then today
        data['active-shops'] = Shop.objects.distinct().filter(shoptheme__valid_till__gte=datetime.today()).count()
        return Response(data)

    return Response(533)

@api_view(['GET', 'DELETE','POST', 'PUT'])
def customers(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 1000
        qs = Account.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 16
        result_page = paginator.paginate_queryset(qs, request)
        data= AccountSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)


    return Response(533)
@api_view(['GET', 'DELETE','POST', 'PUT'])
def shops(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 1000
        shops = Shop.objects.all()
        aid = request.GET.get('aid', None)
        if aid:
            shops = shops.filter(account__id=int(aid))
        result_page = paginator.paginate_queryset(shops, request)
        serializer = ShopSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    return Response(533)
@api_view(['GET', 'DELETE','POST', 'PUT'])
def services(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 1000
        qs = Service_order.objects.all()
        aid = request.GET.get('aid', None)
        if aid:
            qs = Service_order.filter(account__id=int(aid))
        result_page = paginator.paginate_queryset(qs, request)
        serializer = Service_orderSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    return Response(533)






class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class StaffListCreateView(ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(username= 'staff-'+request.data['email'], password=request.data['phone_number'])
        except:
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['user'] = user.id
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class StaffDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPageNumberPagination

class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



@api_view(['GET','POST', 'OPTIONS'])
def tickets(request):
    if request.method == 'POST':
        data = request.data
        if 'tid' in data and 'message' in data:
            tc = Ticket.objects.get(id=data['tid'])
            tm = TicketMessage.objects.create(ticket = tc, content=data['message'], by_admin=True)
            if 'image' in data and len(data['image']) > 10:
                tm.image = strToFile(data['image'])
                tm.save()
    tid = request.GET.get('tid', None)
    if tid:
        tc = Ticket.objects.get(id=tid)
        qs = TicketMessage.objects.filter(ticket=tc)
        data = TicketMessageSerializer(qs, many=True).data
        return Response(data)
    qs = Ticket.objects.all().order_by('-id')
    data = TicketSerializer(qs, many=True).data
    return Response(data)