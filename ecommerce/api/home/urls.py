from django.urls import path
from .views import *

urlpatterns = [
    path('packages', packages),
    path('themes', themes),
    path('plugins', plugins),
]