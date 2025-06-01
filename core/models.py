from django.db import models
from django.contrib.auth.models import User
from .cloudflare import add_domain, delete_domain, add_dns, delete_dns
from .utils import compressImage
from django.conf import settings
from affiliate.models import Affiliate
from core.notification.notif import notify

from core.mailing import send_mail
from core.mail_templates import  ticket_reply_message
# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=100, unique=True)
    type = models.BooleanField(default=False)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.code

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliate = models.ForeignKey(Affiliate, null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    billing_first_name = models.CharField(max_length=100, null=True, blank=True)
    billing_last_name = models.CharField(max_length=100, null=True, blank=True)
    billing_address = models.CharField(max_length=500, null=True, blank=True)
    billing_email = models.CharField(max_length=20, null=True, blank=True)
    billing_phone_number = models.CharField(max_length=20, null=True, blank=True)
    billing_city = models.CharField(max_length=100, null=True, blank=True)
    billing_state = models.CharField(max_length=100, null=True, blank=True)
    billing_country = models.CharField(max_length=100, null=True, blank=True)
    billing_zip_code = models.CharField(max_length=100, null=True, blank=True)
    otp = models.CharField(max_length=100, null=True, blank=True)
    fb_tokens = models.JSONField(default=list, null=True, blank=True)
    PM_CHOICES = (
        ('stripe', 'stripe'),
        ('sp', 'sp'),
    )
    payment_method = models.CharField(max_length=50, choices=PM_CHOICES, default='stripe')
    coupon_used = models.ManyToManyField(Coupon, blank=True)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        if not self.pk:
            notify(self,None,None,1)
        super(Account, self).save(*args, **kwargs)

class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    type_ch = (
        ('order', 'order'),
        ('review', 'review'),
        ('ticket', 'ticket'),
        ('account', 'account'),
        ('other', 'other'),
    )
    type = models.CharField(max_length=50, choices=type_ch, default='other')
    unread = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.account.user.username
    
class Ticket(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.account.user.username
    
class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='ticket_attachments/',null = True, blank = True)
    by_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.ticket.subject
    def save(self, *args, **kwargs):
        if self.by_admin:
            Notification.objects.create(type="order", content="Your support ticket got a new reply", account=self.ticket.account)
            send_mail('Your support ticket got a new reply', ticket_reply_message, [self.ticket.account.email])
        else:
            send_mail('Support ticket got a new message', ticket_reply_message, [settings.EMAIL_HOST_USER])
        super(TicketMessage, self).save(*args, **kwargs)
class Domain(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100, unique=True)
    ns1 = models.CharField(max_length=100, null=True, blank=True)
    ns2 = models.CharField(max_length=100, null=True, blank=True)
    subdomain = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    cfid = models.CharField(max_length=800, null=True, blank=True)
    def __str__(self):
        return self.domain
    def save(self, *args, **kwargs):
        if not self.subdomain:
            res = add_domain(self.domain)
            if res['success'] != False:
                self.cfid = res['result']['id']
                self.ns1 = res['result']['name_servers'][0]
                self.ns2 = res['result']['name_servers'][1]
            else:
                raise Exception(res['errors'][0]['message'])
        super(Domain, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        print(self.cfid)
        if self.cfid:
            res = delete_domain(self)
            try:
                if res['success'] == False:
                    raise Exception(res['errors'][0]['message'])
            except:
                pass
        super(Domain, self).delete(*args, **kwargs)

# Dns.objects.create(domain=self, name=self.domain, type="A", content = "52.221.189.77")
class Dns(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    content = models.CharField(max_length=100, null=False, blank=False, default='52.221.189.77')
    ttl = models.IntegerField(default=1)
    proxied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cfid = models.CharField(max_length=800, null=True, blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.domain.subdomain:
            raise Exception('Subdomain can not have DNS')
        res = add_dns(self.domain.cfid, self.type, self.name, self.content, self.proxied)
        if res['success'] != False:
            self.cfid = res['result']['id']
        else:
            raise Exception(res['errors'][0]['message'])
        super(Dns, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if self.cfid:
            res = delete_dns(self)
            if res['success'] == False:
                raise Exception(res['errors'][0]['message'])
        super(Dns, self).delete(*args, **kwargs)

class Invoice(models.Model):
    TYPE_CHOICES = (
        ('payment', 'payment'),
        ('subscription', 'subscription'),
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='payment')
    PM_CHOICES = (
        ('stripe', 'stripe'),
        ('sp', 'sp'),
    )
    payment_method = models.CharField(max_length=50, choices=PM_CHOICES, default='stripe')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_id =  models.CharField(max_length=2000, null=True, blank=True)
    order_id =  models.CharField(max_length=2000, null=True, blank=True)
    paid = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    due = models.BooleanField(default=False)
    action =  models.CharField(max_length=50, null=True, blank=True)
    action_ref1 =  models.CharField(max_length=50, null=True, blank=True)
    action_ref2 =  models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    renewed_at = models.DateTimeField(null=True, blank=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    redirect = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.account.user.username

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.ImageField(upload_to='blog/',null = True, blank = True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, blank = True)
    author = models.CharField(max_length=100, default='NextOxy')
    meta = models.TextField(default='....')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    TYPE_CHOICES = (
        ('blog', 'blog'),
        ('documentation', 'documentation'),
        ('help_center', 'help_center'),
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='blog')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image, 720, 720)
        super(Blog, self).save(*args, **kwargs)

class MediaFile(models.Model):
    file = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    def save(self, *args, **kwargs):
        self.file = compressImage(self.file, 1280, 720)
        super(MediaFile, self).save(*args, **kwargs)


class Service_order(models.Model):
    title = models.CharField(max_length=100, blank = True, null=True)
    invoice_id = models.CharField(max_length=100, blank = True, null=True)
    invoice_method = models.CharField(max_length=100, blank = True, null=True)
    paid = models.BooleanField(default=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data = models.JSONField(null=True, blank=True)
    type_choice = (
        ('BOOSTING', 'BOOSTING'),
        ('SEO', 'SEO'),
        ('GRAPHIC', 'GRAPHIC'),
        ('FORMATION', 'FORMATION'),
    )
    type = models.CharField(max_length=50, choices=type_choice, default='BOOSTING')
    status_choice = (
        ('UNDER-REVIEW', 'UNDER-REVIEW'),
        ('PROCESSING', 'PROCESSING'),
        ('COMPLETED', 'COMPLETED'),
        ('CANCELLED', 'CANCELLED'),
        ('REFUNDED', 'REFUNDED'),
    )
    status = models.CharField(max_length=50, choices=status_choice, default='UNDER-REVIEW')
    def __str__(self):
        return str(self.created_at)
    def save(self, *args, **kwargs):
        super(Service_order, self).save(*args, **kwargs)

class Settings(models.Model):
    affiliate_commission = models.IntegerField(default=5)
    shop_message = models.CharField(max_length=500, null=True, blank=True)
    shop_message_link = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return 'Do Not Delete Or Create New'