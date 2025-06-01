from django.core.exceptions import ImproperlyConfigured
from core.models import Account, Domain
from ecommerce.models import Shop
from blog.models import Eblog
from website.models import Website

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

class HostRouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        host = request.META.get('HTTP_HOST', '').lower()
        print('HOST',host)
        domainName = domain_name(host)
        print('Domain Name str',domainName)
        urlconf = 'core.urls'
        if domainName is not None:
            domain = Domain.objects.filter(domain=domainName).first()
            print('Domain',domain)
            if domain:
                shop = Shop.objects.filter(domains = domain).first()
                print('Shop',shop)
                if shop:
                    urlconf = 'ecommerce.urls'
                blog = Eblog.objects.filter(domains = domain).first()
                if blog:
                    urlconf = 'blog.urls'
                website = Website.objects.filter(domains = domain).first()
                if website:
                    urlconf = 'website.urls'
        request.urlconf = urlconf
        return self.get_response(request)