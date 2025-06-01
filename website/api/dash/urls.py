from django.urls import path

from .views import *

urlpatterns = [
    path('website', website),
    path('themes', themes),
    path('websitethemes', websitethemes),
]