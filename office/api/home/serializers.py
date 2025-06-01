from office.models import Contact, Contact_reply, Custom_order
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
class Custom_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_order
        fields = '__all__'
