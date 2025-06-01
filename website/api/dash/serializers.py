from website.models import Website, Theme, WebsiteTheme
from rest_framework import serializers

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'
        depth=1

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class WebsiteThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteTheme
        fields = '__all__'
        depth=1