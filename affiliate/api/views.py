from ecommerce.models import Theme, Plugin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from affiliate.models import *
from django.db.models import Sum
from datetime import date, timedelta
import calendar
from core.models import Settings

@api_view(['GET', 'DELETE','POST', 'PUT'])
def overview(request):
    user = request.user
    qs, ct = Affiliate.objects.get_or_create(user = request.user)
    if request.method == 'POST':
        data = request.data
        print(data)
        qs.bank_name = data['bank_name']
        qs.bank_account = data['bank_account']
        qs.bank_routing = data['bank_routing']
        qs.bank_address = data['bank_address']
        qs.save()
    data = AffiliateSerializer(qs).data
    q = request.GET.get('q', 'all')
    if q == 'today':
        today = date.today()
        coms = Commission.objects.filter(affiliate=qs, date__date=today)
    elif q == 'yesterday':
        yesterday = date.today() - timedelta(days=1)
        coms = Commission.objects.filter(affiliate=qs, date__date=yesterday)
    elif q == 'month':
        today = date.today()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])
        coms = Commission.objects.filter(affiliate=qs, date__date__range=[first_day_of_month, last_day_of_month])
    else:
        coms = Commission.objects.filter(affiliate = qs)
    st,ct = Settings.objects.get_or_create()
    data['affiliate_commission'] = st.affiliate_commission
    data['com_count'] = coms.count()
    data['com_amount'] = coms.aggregate(Sum('commission'))['commission__sum'] or 0
    return Response(data)
@api_view(['GET', 'DELETE','POST', 'PUT'])
def click(request):
    code = request.GET.get('ref', None)
    if code:
        qs = Affiliate.objects.filter(affiliate_code = code)
        print(qs.exists())
        if qs.exists():
            qs = qs.first()
            qs.click += 1
            qs.save()
    return Response({'success': True})
@api_view(['GET', 'DELETE','POST', 'PUT'])
def withdraw(request):
    user = request.user
    aff, ct = Affiliate.objects.get_or_create(user = request.user)
    if request.method == 'POST':
        data = request.data
        if float(data['amount']) <= aff.current_balance:
            nw = Withdraw.objects.create(affiliate = aff, amount=data['amount'])
            nw.save()
    
    qs = Withdraw.objects.filter(affiliate=aff)
    paginator = PageNumberPagination()
    paginator.page_size = 16
    result_page = paginator.paginate_queryset(qs, request)
    data= WithdrawSerializer(result_page, many=True).data
    return paginator.get_paginated_response(data)
@api_view(['GET', 'DELETE','POST', 'PUT'])
def commission(request):
    user = request.user
    aff, ct = Affiliate.objects.get_or_create(user = request.user)
    qs = Commission.objects.filter(affiliate=aff)
    paginator = PageNumberPagination()
    paginator.page_size = 16
    result_page = paginator.paginate_queryset(qs, request)
    data= CommissionSerializer(result_page, many=True).data
    return paginator.get_paginated_response(data)