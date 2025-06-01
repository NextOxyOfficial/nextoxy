from django.contrib.auth.models import User
from ecommerce.models import *
from ecommerce.tools.scripts import generateCode, generateNavCode

def domain_name(input_str):
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
    
def shopData(request):
    host = request.META.get('HTTP_HOST', '').lower()
    domainName = domain_name(host)
    shop = Shop.objects.filter(domains__domain=domainName).first()

    main_menu, ct = Menu.objects.get_or_create(shop = shop, name="Main Menu")
    footer_menu, ct = Menu.objects.get_or_create(shop = shop, name="Footer Menu")
    main_menu_items = MenuItem.objects.filter(menu=main_menu)
    footer_menu_items = MenuItem.objects.filter(menu=footer_menu)
    sections = Section.objects.filter(shop=shop)
    socials = Social.objects.filter(shop=shop)
    edit = request.GET.get('edit', None)
    context = {
        'main_menu': main_menu_items,
        'footer_menu': footer_menu_items,
        'socials': socials,
        'shop': shop,
        'sections': sections,
        'scripts': generateCode(shop),
        'scripts2': generateNavCode(shop),
        'edit': edit,
    }
    return context