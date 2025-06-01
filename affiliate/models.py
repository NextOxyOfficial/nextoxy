from django.db import models
from django.contrib.auth.models import User
import random
import string
# Create your models here.


class Affiliate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliate_code = models.CharField(max_length=100, unique=True)
    views = models.IntegerField(default=0)
    click = models.IntegerField(default=0)
    registrations = models.IntegerField(default=0)
    total_earning = models.FloatField(default=0.00)
    current_balance = models.FloatField(default=0.00)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    PAYMENT_CHOICES = (
        ('BANK', 'BANK'),
    )
    payment_method = models.CharField(choices=PAYMENT_CHOICES, max_length=50, default='BANK')
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    bank_account = models.CharField(max_length=200, blank=True, null=True)
    bank_routing = models.CharField(max_length=200, blank=True, null=True)
    bank_address = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return str(self.user)
    def save(self, *args, **kwargs):
        if not self.affiliate_code:
            rt = ''.join(random.choice(string.ascii_lowercase) for x in range(6))
            self.affiliate_code = rt
        super(Affiliate, self).save(*args, **kwargs)

class AffProduct(models.Model):
    name = models.CharField(max_length=100)
    commission = models.FloatField(default=0.00)
    description = models.TextField()
    image = models.ImageField(upload_to='affiliate', null=True, blank=True)
    def __str__(self):
        return self.name

class Commission(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    product = models.ForeignKey(AffProduct, on_delete=models.SET_NULL, null=True, blank=True, related_name='aff_product')
    commission = models.FloatField(default=0.00)
    def __str__(self):
        return self.title+ ' - ' + str(self.commission)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.affiliate.current_balance += self.commission
            self.affiliate.save()
    
        super(Commission, self).save(*args, **kwargs)

class Withdraw(models.Model):
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0.00)
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='PENDING')
    def __str__(self):
        return self.affiliate
    def save(self, *args, **kwargs):
        super(Withdraw, self).save(*args, **kwargs)