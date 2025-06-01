from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Account)
admin.site.register(Notification)
admin.site.register(Domain)
admin.site.register(Dns)
admin.site.register(Invoice)
admin.site.register(Coupon)
admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(Service_order)
admin.site.register(Settings)
admin.site.register(Ticket)
admin.site.register(TicketMessage)

