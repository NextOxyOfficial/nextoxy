from django.contrib import admin
from django.urls import path, include
from .views import *
from . import shop_api

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + [
    path('api/products', shop_api.products),
    path('api/detail', shop_api.detail),
    path('api/cart', shop_api.cart),
    path('api/wish', shop_api.wish),
    path('api/subscribe', shop_api.subscribe),
    path('api/checkout', shop_api.checkout),
    path('api/coupon', shop_api.coupon),
    path('api/shipping', shop_api.shipping),
    path('api/review', shop_api.review),
    path('api/editor', shop_api.editor),
    path('api/filter_products', shop_api.filter_products),
]


urlpatterns = urlpatterns + [
    
    # ecommerce 
    path('', home),
    path('details/<int:id>', details),
    path('checkout', checkout),
    path('cart', cart),
    path('wishlist', wishlist),
    path('signin', signin),
    path('search_page', search_page),
    path('my_account', my_account, name='my_account'),
    path('contact_us', contact_us),
    path('tracking', tracking),
    path('not_found', not_found, name='not_found'),
    path('page/<str:name>', page),
    path('pages/<str:name>', pages),

    # blog 
    
    path('submit-lead-form', submitLeadForm),

    # 
    path('blog_details', blogDetails),
    path('categories', category),
    path('contact', contact),
    path('about', about),
    # other
    path('activate-nextoxy-theme', activateNextoxyTheme),
    path('sitemap.xml', sitemap),
    path('robots.txt', robots),
]
