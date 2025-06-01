from django.contrib import admin
from .models import Eblog, Category, Post, MediaFile, Theme, BlogTheme
# Register your models here.

admin.site.register(Eblog)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(MediaFile)
admin.site.register(Theme)
admin.site.register(BlogTheme)

