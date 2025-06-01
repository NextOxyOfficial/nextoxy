from django.contrib import admin
from .models import Shop, Banner, Blog, Menu, MenuItem, Section, Category, Brand, Social, Tag, ShippingProfile, Product, ProductImage, VariantSuggestion, ProductVariant, Review, Subscriber, Customer, Address, Order_status, Order, MediaFile
from .models import Page, Staff, ThemePackage, Theme, ShopTheme, Contact, ContactReply, EmailTemplate, EmailMessage, Plugin, ShopPlugin, Seo, Edit
from .models import Leads
from django.utils.html import format_html
admin.site.register(MediaFile)

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'account', 'email', 'phone', 'created_at']
    list_filter = ['country']
    search_fields = ['name', 'email']
    list_per_page = 20

admin.site.register(Shop, ShopAdmin)
admin.site.register(Banner)
admin.site.register(Blog)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Social)
admin.site.register(Brand)
admin.site.register(Tag)
admin.site.register(ShippingProfile)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(VariantSuggestion)
admin.site.register(ProductVariant)
admin.site.register(Review)
admin.site.register(Customer)
admin.site.register(Leads)
admin.site.register(Subscriber)
admin.site.register(Address)
admin.site.register(Order_status)
admin.site.register(Order)
admin.site.register(Page)
admin.site.register(Staff)
class ThemePackageAdmin(admin.ModelAdmin):
    list_display = ['level', 'name', 'price']

admin.site.register(ThemePackage, ThemePackageAdmin)
class ThemeAdmin(admin.ModelAdmin):
    def preview(self, obj):
        if obj.image:
            return format_html('<a href="{}" style="cursor: pointer;" target="_blank"><img style="width:80px;height:120px;object-fit:cover" src="{}" /></a>'.format(obj.image.url, obj.image.url))
        else:
            return 'No Preview'
    list_display = ['name', 'package', 'preview', 'active']
    list_filter = ['package', 'active']
admin.site.register(Theme, ThemeAdmin)

class ShopThemeAdmin(admin.ModelAdmin):
    list_display = ['shop', 'theme', 'purchased_on', 'valid_till', 'activated']
    list_filter = ['activated']
    list_per_page = 20

admin.site.register(ShopTheme, ShopThemeAdmin)
admin.site.register(Contact)
admin.site.register(ContactReply)
admin.site.register(EmailTemplate)
admin.site.register(EmailMessage)
admin.site.register(Plugin)
admin.site.register(ShopPlugin)
admin.site.register(Seo)
admin.site.register(Edit)




