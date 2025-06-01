from website.models import Website, WebsiteTheme
from django.shortcuts import redirect

def domain_name(input_str):
    split_input = input_str.split('.')
    output = split_input[0]
    if len(split_input) > 2:
        domain = split_input[1] + '.' + split_input[2]
        if domain == 'nextoxy.com':
            return output
        else:
            return None
    elif split_input[1] == 'localhost:8000':
        return output
    else:
        return None

# for api
def get_website(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        id = request.GET.get('website')
        website = Website.objects.get(account=user.account, id=id)
        return view_func(request, website, *args, **kwargs)
    return wrapper

# for website
def get_website2(view_func):
    def wrapper(request, *args, **kwargs):
        host = request.META.get('HTTP_HOST', '').lower()
        domainName = domain_name(host)
        website = Website.objects.filter(domains__domain=domainName).first()
        theme = WebsiteTheme.objects.filter(website=website, activated=True).first()
        if not theme:
            return redirect('/activate-nextoxy-theme')
        return view_func(request, website, theme.theme.path+'/', *args, **kwargs)
    
    return wrapper