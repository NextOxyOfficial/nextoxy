from blog.models import Eblog, Post, Category, MediaFile, Theme, BlogTheme
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eblog
        fields = '__all__'
        depth=1

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth=1

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'
        depth=1

class ThemeSerializer(serializers.ModelSerializer):
    installed = serializers.SerializerMethodField()
    def get_installed(self, obj):
        blog = self.context.get("blog")
        spl = BlogTheme.objects.filter(blog=blog, theme=obj)
        if spl:
            return True
        else:
            return False
    class Meta:
        model = Theme
        fields = '__all__'

class BlogThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTheme
        fields = '__all__'
        depth=1
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'