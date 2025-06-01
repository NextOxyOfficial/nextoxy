from rest_framework import serializers
from .models import Product, ProductVariant, Review


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    currency = serializers.SerializerMethodField()
    def get_currency(self, obj):
        currency = obj.shop.currency
        return currency
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        images = obj.productimage_set.all()
        images = [image.image.url for image in images]
        if images:
            return images[0]
        return None
    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    variations = serializers.SerializerMethodField()
    def get_variations(self, obj):
        variations = ProductVariantSerializer(obj.productvariant_set.all(), many=True).data
        return variations
    currency = serializers.SerializerMethodField()
    def get_currency(self, obj):
        currency = obj.shop.currency
        return currency
    productimage_set = serializers.SerializerMethodField()
    def get_productimage_set(self, obj):
        images = obj.productimage_set.all()
        if images:
            return [image.image.url for image in images]
        else:
            return None

    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'