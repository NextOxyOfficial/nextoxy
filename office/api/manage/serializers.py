from rest_framework import serializers
from ecommerce.models import Shop
from django.contrib.auth.models import User
from office.models import Staff, Product, Order
from core.models import Account, Service_order, Ticket, TicketMessage
class ShopSerializer(serializers.ModelSerializer):
    theme_active = serializers.SerializerMethodField()
    class Meta:
        model = Shop
        fields = '__all__'
        depth=1
    def get_theme_active(self, obj):
        return obj.theme_active()

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        depth = 1
class Service_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_order
        fields = '__all__'
        depth = 1

class TicketSerializer(serializers.ModelSerializer):
    message_count = serializers.SerializerMethodField()
    class Meta:
        model = Ticket
        fields = '__all__'
    def get_message_count(self, obj):
        return obj.ticketmessage_set.count()
class TicketMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = '__all__'