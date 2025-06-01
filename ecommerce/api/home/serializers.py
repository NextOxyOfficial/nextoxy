from ecommerce.models import Theme, Plugin, ThemePackage
from rest_framework import serializers

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
        depth= 1

class PluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plugin
        fields = '__all__'
class ThemePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemePackage
        fields = '__all__'