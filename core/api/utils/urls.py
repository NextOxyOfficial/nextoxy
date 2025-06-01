from django.urls import path, include
from .views import *
urlpatterns = [
    path('cities/', cities),
    path('states/', states),
    path('countries/', countries),
]

# /api/utils/countries/
# /api/utils/states/?country=bangladesh
# /api/utils/cities/?country=bangladesh
# /api/utils/cities/?country=bangladesh&state=khulna