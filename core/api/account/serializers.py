from rest_framework import serializers
from django.contrib.auth.models import User
from ecommerce.models import Shop
from blog.models import Eblog
from website.models import Website
from core.models import Account, Invoice, Blog, BlogCategory, MediaFile, Service_order

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        depth = 1

class EblogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eblog
        fields = '__all__'

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        depth = 1
        exclude = ['content']

class BlogCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        depth = 1
        fields = '__all__'
class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'
        depth=1


class Service_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_order
        fields = '__all__'