from django.contrib import admin
from .models import Website, Theme, WebsiteTheme
# Register your models here.

admin.site.register(Website)
admin.site.register(Theme)
admin.site.register(WebsiteTheme)
