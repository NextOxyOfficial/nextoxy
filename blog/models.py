from django.db import models
from django.contrib.auth.models import User
from core.models import Account, Domain
from .utils import compressImage
import requests, json

# Create your models here.


class Eblog(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='blog_owner', null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    domains = models.ManyToManyField(Domain)
    title = models.CharField(max_length=100, blank = True, verbose_name='Blog Title')
    logo = models.FileField(upload_to='blog/',null = True, blank = True )
    favicon = models.FileField(upload_to='blog/',null = True, blank = True )
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

class Category(models.Model):
    blog = models.ForeignKey(Eblog, on_delete=models.CASCADE, related_name='blog_category')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    def __str__(self):
        return "{} - {}".format(self.blog.name, self.name)

class Post(models.Model):
    blog = models.ForeignKey(Eblog, on_delete=models.CASCADE, related_name='blog_post')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_category')
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    image = models.FileField(upload_to='blog/',null = True, blank = True )
    content = models.TextField()
    meta = models.TextField()
    trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} - {}".format(self.blog.name, self.title)

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image, 720, 720)
        super().save(*args, **kwargs)

class MediaFile(models.Model):
    blog = models.ForeignKey(Eblog, null=True,  blank=True, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    def save(self, *args, **kwargs):
        self.file = compressImage(self.file, 1280, 720)
        super(MediaFile, self).save(*args, **kwargs)


class Theme(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="Theme Description here...")
    image = models.ImageField(upload_to='themes/', null=True, blank=True)
    feature_image = models.ImageField(upload_to='themes/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class BlogTheme(models.Model):
    blog = models.ForeignKey(Eblog, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    purchased_on = models.DateTimeField(auto_now_add=True)
    valid_till = models.DateTimeField(null=True, blank=True)
    activated = models.BooleanField(default=False)
    class Meta:
        unique_together = ('blog','theme')
    def __str__(self):
        return self.blog.name+' '+self.theme.name
