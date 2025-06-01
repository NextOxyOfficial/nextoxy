from ecommerce.models import Shop, ShopTheme
from django.shortcuts import redirect
from rest_framework.response import Response
def domain_name(input_str):
    input_str = input_str.replace('www.', '')
    split_input = input_str.split('.')
    output = split_input[0]
    if len(split_input) > 2:
        domain = split_input[1] + '.' + split_input[2]
        if domain == 'nextoxy.com':
            return output
        else:
            return input_str
    elif split_input[1] == 'localhost:8000':
        return output
    else:
        return input_str


# for api
def get_shop(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        id = request.GET.get('ecommerce')
        if not user.is_authenticated or not user.account:
            return Response({
                "navigate": "/auth/login"
            })
        shop = Shop.objects.filter(account=user.account, id=id).first()
        if not shop:
            return Response({
                "navigate": "/account/ecommerce"
            })
        return view_func(request, shop, *args, **kwargs)
    return wrapper

# for ecommerce
def get_shop2(view_func):
    def wrapper(request, *args, **kwargs):
        host = request.META.get('HTTP_HOST', '').lower()
        domainName = domain_name(host)
        shop = Shop.objects.filter(domains__domain=domainName).first()
        theme = ShopTheme.objects.filter(shop=shop, activated=True).first()
        if not theme:
            return redirect('/activate-nextoxy-theme')
        return view_func(request, shop, theme.theme.path+'/', *args, **kwargs)
    
    return wrapper