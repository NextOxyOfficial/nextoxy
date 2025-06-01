from django.urls import path

from .views import *

urlpatterns = [
    path('shop', shop),
    path('steps', steps),
    path('chart', chart),
    path('overview', overview),
    path('menus', menus),
    path('categories', categories),
    path('brands', brands),
    path('socials', socials),
    path('tags', tags),
    path('products', products),
    path('coupons', coupons),
    path('orders', orders),
    path('orderstatus', orderStatus),
    path('mediafiles', MediaFiles),
    path('shipping', shipping),
    path('shipping-data', shippingData),
    path('customers', customers),
    path('subscribers', subscribers),
    path('contacts', contacts),
    path('reviews', reviews),
    path('pages', pages),
    path('staffs', staffs),
    path('packages', packages),
    path('themes', themes),
    path('shopthemes', shopthemes),
    path('domains', domains),
    path('records', records),
    path('templates', templates),
    path('shop-plugins', ShopPlugins),
    path('plugins', plugins),
    path('onepage', onepage), #for editing onepage content
    # urls just for plugins 
    path('cjimport', cjimport),
    path('oxymanagerimport', oxymanagerimport),
    path('oxymanagerupdate', oxymanagerupdate),
    path('ndsimport', ndsimport),
    path('leads', leads),
]