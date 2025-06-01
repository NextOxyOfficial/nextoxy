from django.urls import path, include
from .views import *
from .social import GoogleLogin
urlpatterns = [
    path('login/', loginUser),
    path('register/', registerUser),
    path('reset/', resetUser),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('notifications/', notifications),
    path('tickets/', tickets),
]