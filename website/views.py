from django.shortcuts import render
from .decorators import get_website2
from .models import Website
# Create your views here.
@get_website2
def home(request, website, theme):
    print(website, 78)
    return render(request, theme + 'home.html', {'website': website})
@get_website2
def test(request, website, theme):
    print(website, 78)
    return render(request, theme + 'test12.html', {'website': website})


# other 
def activateNextoxyTheme(request):
    return render(request, 'other/activateWebsiteTheme.html')