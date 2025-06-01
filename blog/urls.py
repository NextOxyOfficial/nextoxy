from django.contrib import admin
from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + []


urlpatterns = urlpatterns + [
    path('', home),
    path('blog_details', blog_details),
    path('categories/<int:category_id>/', categories),
    path('page', pages),
    path('search', search),
    path('about', about),
    path('account', account),
    path('contact', contact),
]
