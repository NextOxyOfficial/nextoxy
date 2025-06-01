from django.urls import path, include
from .views import *



urlpatterns = [
    path('overview/', overview),
    path('click/', click),
    path('withdraw/', withdraw),
    path('commission/', commission),
] 