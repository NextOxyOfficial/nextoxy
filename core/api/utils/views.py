from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

from cities_light.models import Country, City, Region
from .serializers import CitySerializer, CountrySerializer, RegionSerializer

@api_view(['GET','POST', 'OPTIONS'])
def cities(request):
    country = Country.objects.filter(name__iexact = request.GET.get('country')).first()
    cityList = City.objects.filter(country = country)
    if request.GET.get('state', None) and Region.objects.filter(name__iexact = request.GET.get('state')).first():
        cityList = cityList.filter(region = Region.objects.filter(name__iexact = request.GET.get('state')).first().id)
    serializer = CitySerializer(cityList, many=True)
    return Response(serializer.data)

@api_view(['GET','POST', 'OPTIONS'])
def states(request):
    country = Country.objects.filter(name__iexact = request.GET.get('country')).first()
    stateList = Region.objects.filter(country = country)
    serializer = RegionSerializer(stateList, many=True)
    return Response(serializer.data)

@api_view(['GET','POST', 'OPTIONS'])
def countries(request):
    countryList = Country.objects.all()
    serializer = CountrySerializer(countryList, many=True)
    return Response(serializer.data)
        