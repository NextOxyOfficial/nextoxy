from rest_framework import serializers
from ecommerce.models import Shop, Banner, Blog, Menu, MenuItem, Section, Category, Brand, Social, Tag, ShippingProfile, Product, ProductImage, VariantSuggestion, ProductVariant, Review, Customer, Address, Order_status, Order, MediaFile
from ecommerce.models import Page, Staff, ThemePackage, Theme, ShopTheme, Contact, ContactReply, EmailTemplate, EmailMessage, Plugin, ShopPlugin, Subscriber, Coupon
from ecommerce.models import Leads
from core.models import Domain, Dns

class ShopSerializer(serializers.ModelSerializer):
    package_validity_days = serializers.SerializerMethodField()
    is_onepage_active = serializers.SerializerMethodField()
    cj_active = serializers.SerializerMethodField()
    nds_active = serializers.SerializerMethodField()
    oxymanager_active = serializers.SerializerMethodField()
    local_active = serializers.SerializerMethodField()
    barcode_active = serializers.SerializerMethodField()
    class Meta:
        model = Shop
        fields = '__all__'
        depth=1
    def get_is_onepage_active(self, obj):
        return obj.is_onepage_active()
    def get_package_validity_days(self, obj):
        return obj.package_validity_days()
    def get_cj_active(self, obj):
        return obj.cj_active()
    def get_nds_active(self, obj):
        return obj.nds_active()
    def get_oxymanager_active(self, obj):
        return obj.oxymanager_active()
    def get_local_active(self, obj):
        return obj.local_active()
    def get_barcode_active(self, obj):
        return obj.barcode_active()
    

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class SectionSerializer(serializers.ModelSerializer):
    category_set = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Section
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    productimage_set = ProductImageSerializer(many=True, read_only=True)
    productvariant_set = ProductVariantSerializer(many=True, read_only=True)
    quantity = serializers.IntegerField(required=False)
    class Meta:
        model = Product
        exclude = ['shop']
        depth = 1
    
class ShippingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingProfile
        exclude = ['shop', 'data']

class ShippingProfileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingProfile
        exclude = ['shop', 'created_at']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['shop']
        depth = 1
class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        exclude = ['shop']
        depth = 1

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactReply
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['shop']
        depth = 1

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_status
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1
class ThemePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemePackage
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    installed = serializers.SerializerMethodField()
    def get_installed(self, obj):
        shop = self.context.get("shop")
        print(shop, obj)
        spl = ShopTheme.objects.filter(shop=shop, theme=obj, activated=True)
        return spl.exists()
    class Meta:
        model = Theme
        fields = '__all__'
        depth = 1

class ShopThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopTheme
        exclude = ['shop']
        depth = 1

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'

class DnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dns
        fields = '__all__'

class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = '__all__'

class PluginSerializer(serializers.ModelSerializer):
    installed = serializers.SerializerMethodField()
    def get_installed(self, obj):
        shop = self.context.get("shop")
        print(obj, 66666666666)
        spl = ShopPlugin.objects.filter(shop=shop, plugin=obj)
        if spl:
            return True
        else:
            return False
    class Meta:
        model = Plugin
        fields = '__all__'

class ShopPluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopPlugin
        exclude = ['shop']
        depth = 1

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'