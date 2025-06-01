from django.contrib import admin
from .models import Contact, Contact_reply, Custom_order, Product, Staff, Order

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website', 'subject', 'message', 'created_at')

@admin.register(Contact_reply)
class Contact_replyAdmin(admin.ModelAdmin):
    list_display = ('contact', 'reply', 'created_at')

@admin.register(Custom_order)
class Custom_orderAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'email', 'phone', 'message', 'created_at')



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_in_stock', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name',)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_full_name', 'product', 'product_price', 'status', 'order_date', 'salesperson')
    list_filter = ('status', 'order_date')
    search_fields = ('customer_full_name', 'product__name', 'salesperson__first_name', 'salesperson__last_name')
    raw_id_fields = ('product', 'salesperson')

admin.site.register(Product, ProductAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Order, OrderAdmin)