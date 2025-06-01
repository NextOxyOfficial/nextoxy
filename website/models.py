from django.db import models
from django.contrib.auth.models import User
from core.models import Account, Domain
from .utils import compressImage
import requests, json

# Create your models here.


class Website(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='website_owner', null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    domains = models.ManyToManyField(Domain)
    title = models.CharField(max_length=100, blank = True, verbose_name='Site Title')
    logo = models.FileField(upload_to='website/',null = True, blank = True )
    favicon = models.FileField(upload_to='website/',null = True, blank = True )
    email = models.CharField(max_length=200, blank = True)
    phone = models.CharField(max_length=200, blank = True)
    street = models.CharField(max_length=50, blank = True)
    city = models.CharField(max_length=50, blank = True)
    state = models.CharField(max_length=50, blank = True)
    zip_code = models.CharField(max_length=50, blank = True)
    country = models.CharField(max_length=50, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# other 

class Theme(models.Model):       # there is already theme present in ecommerce, need to change it
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="Theme Description here...")
    image = models.ImageField(upload_to='themes/', null=True, blank=True)
    feature_image = models.ImageField(upload_to='themes/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class WebsiteTheme(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    purchased_on = models.DateTimeField(auto_now_add=True)
    valid_till = models.DateTimeField(null=True, blank=True)
    activated = models.BooleanField(default=False)
    class Meta:
        unique_together = ('website','theme')
    def __str__(self):
        return self.website.name+' '+self.theme.name
