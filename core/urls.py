from django.urls import path, include
from core.views import *
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + [
    path('admin/', admin.site.urls),
    path('firebase-messaging-sw.js',showFirebaseJS,name="show_firebase_js"),
    path('api/auth/', include('core.api.auth.urls')),
    path('api/utils/', include('core.api.utils.urls')),
    path('api/account/', include('core.api.account.urls')),
    path('api/ecommerce/dash/', include('ecommerce.api.dash.urls')),
    path('api/ecommerce/home/', include('ecommerce.api.home.urls')),
    path('api/blog/dash/', include('blog.api.dash.urls')),
    path('api/website/dash/', include('website.api.dash.urls')),
    path('api/office/home/', include('office.api.home.urls')),
    path('api/office/ai/', include('office.api.ai.urls')),
    path('api/office/manage/', include('office.api.manage.urls')),
    path('api/affiliate/', include('affiliate.api.urls')),
    path('', index, name='index'),
    path('test', test),
    path('test1', test1),
    path('test2', test2),
    path('editor/', include('editor.urls')),
    path('<str:param>', index, name='index'),
    path('<str:param>/', index, name='index'),
    path('<str:param>/<str:param2>', index, name='index'),
    path('<str:param>/<str:param2>/', index, name='index'),
    path('<str:param>/<str:param2>/<str:param3>', index, name='index'),
    path('<str:param>/<str:param2>/<str:param3>/', index, name='index'),
    path('<str:param>/<str:param2>/<str:param3>/<str:param4>', index, name='index'),
    path('<str:param>/<str:param2>/<str:param3>/<str:param4>/', index, name='index'),
] 