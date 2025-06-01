from django.db import models
from django.contrib.auth.models import User
from affiliate.models import Commission
from .utils import compressImage, ShopSetup
import requests, json
from datetime import datetime
from django.utils import timezone

from core.models import Account, Domain, Settings, Notification
from core.mailing import send_mail
from core.mail_templates import new_order_message, new_review_message

def calcP(total, percent):
    amount = float(total) * float(percent) / 100
    return float(amount)
class ThemePackage(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    yearly = models.DecimalField(max_digits=6, decimal_places=2, default=100)
    title = models.CharField(max_length=100, default="No Title")
    description = models.CharField(max_length=400, default="No Description")
    icon = models.CharField(max_length=100, default="bx:bxs-badge-dollar")
    color = models.CharField(max_length=100, default="text-green-500")
    feature1 = models.CharField(max_length=100, default="No Feature")
    feature2 = models.CharField(max_length=100, default="No Feature")
    feature3 = models.CharField(max_length=100, default="No Feature")
    feature4 = models.CharField(max_length=100, default="No Feature")
    feature5 = models.CharField(max_length=100, default="No Feature")
    feature6 = models.CharField(max_length=100, default="No Feature")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['level']
class Theme(models.Model):
    package = models.ForeignKey(ThemePackage, null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(default=4)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="Theme Description here...")
    image = models.ImageField(upload_to='themes/', null=True, blank=True)
    feature_image = models.ImageField(upload_to='themes/', null=True, blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    onepage = models.BooleanField(default=False)
    data1 = models.TextField(null=True, blank=True)
    data2 = models.TextField(null=True, blank=True)
    data3 = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
class Shop(models.Model):
    package = models.ForeignKey(ThemePackage, null=True, blank=True, on_delete=models.SET_NULL)
    package_validity = models.DateTimeField(null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    staffs = models.ManyToManyField(Account, related_name='staffs', blank=True)
    domains = models.ManyToManyField(Domain)
    title = models.CharField(max_length=100, blank = True, verbose_name='Site Title')
    logo = models.FileField(upload_to='shop/',null = True, blank = True )
    favicon = models.FileField(upload_to='shop/',null = True, blank = True )
    payment_image = models.FileField(upload_to='shop/',null = True, blank = True )
    email = models.CharField(max_length=50, blank = True)
    phone = models.CharField(max_length=30, blank = True)
    street = models.CharField(max_length=300, blank = True)
    city = models.CharField(max_length=50, blank = True)
    state = models.CharField(max_length=50, blank = True)
    zip_code = models.CharField(max_length=50, blank = True)
    country = models.CharField(max_length=50, blank = True)
    currency = models.CharField(max_length=50, blank = False, null=False, default='USD $')
    android_app_link = models.CharField(max_length=400, blank = True)
    ios_app_link = models.CharField(max_length=400, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # location settings
    warehouse = models.BooleanField(default=True)
    room = models.BooleanField(default=True)
    sec = models.BooleanField(default=True)
    shelf = models.BooleanField(default=True)
    rack = models.BooleanField(default=True)
    drawer = models.BooleanField(default=True)
    file = models.BooleanField(default=True)
    def package_validity_days(self):
        if self.package_validity:
            return (self.package_validity - timezone.now()).days
        else:
            return 0
    def cj_active(self):
        pl = ShopPlugin.objects.filter(shop=self, plugin__code='cj', activated=True)
        if pl:
            return True
        else:
            return False
    def nds_active(self):
        pl = ShopPlugin.objects.filter(shop=self, plugin__code='nds', activated=True)
        if pl:
            return True
        else:
            return False
    def theme_active(self):
        th = ShopTheme.objects.filter(shop=self, valid_till__gte=datetime.today())
        if th:
            return True
        else:
            return False
    def is_onepage_active(self):
        th = ShopTheme.objects.filter(shop=self, activated = True)
        if th:
            return True
        else:
            return False
    def oxymanager_active(self):
        pl = ShopPlugin.objects.filter(shop=self, plugin__code='oxymanager', activated=True)
        if pl:
            return True
        else:
            return False
    def local_active(self):
        pl = ShopPlugin.objects.filter(shop=self, plugin__code='local', activated=True)
        if pl:
            return True
        else:
            return False
    def barcode_active(self):
        pl = ShopPlugin.objects.filter(shop=self, plugin__code='barcode', activated=True)
        if pl:
            return True
        else:
            return False
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.pk is None:
            super(Shop, self).save(*args, **kwargs)  
            ShopSetup(self, Banner, Blog, Section, Category, Menu, Order_status, Product, ProductImage, Tag)
        else:
            super(Shop, self).save(*args, **kwargs)

class Edit(models.Model):
    shop = models.OneToOneField(Shop, null=False, blank=False, on_delete=models.CASCADE)
    content = models.JSONField(default=list, null=True, blank=True)
    def __str__(self):
        return self.shop.name

class MediaFile(models.Model):
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    def save(self, *args, **kwargs):
        self.file = compressImage(self.file, 1280, 720)
        super(MediaFile, self).save(*args, **kwargs)

class Banner(models.Model):
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner/',null = True, blank = True)
    title = models.CharField(max_length=100, blank = True)
    content = models.TextField(max_length=500, blank = True)
    button_link = models.CharField(max_length=100, blank = True)
    button_text = models.CharField(max_length=100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.image = compressImage(self.image, 1280, 720)
        super(Banner, self).save(*args, **kwargs)

class Blog(models.Model):
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/',null = True, blank = True)
    title = models.CharField(max_length=100, blank = True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image, 720, 720)
        super(Blog, self).save(*args, **kwargs)

class Menu(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)+ ' '+ str(self.shop.name)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# category And Product 

class Section(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='section/',null = True, blank = True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image, 520, 520)
        super(Section, self).save(*args, **kwargs)

class Category(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/',null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image, 520, 520)
        super(Category, self).save(*args, **kwargs)

class Brand(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand/',null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image, 520, 520)
        super(Brand, self).save(*args, **kwargs)

class Social(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    link = models.CharField(max_length=600)
    name = models.CharField(max_length=100, default='No Name')
    image = models.ImageField(upload_to='social/',null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image, 120, 120)
        super(Social, self).save(*args, **kwargs)


class Tag(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ShippingProfile(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(null=False, blank=False, default=dict)
    def __str__(self):
        return self.name

class Product(models.Model):
    # basic 
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)
    name = models.CharField(max_length=1200, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    buy_price = models.FloatField(null=True, blank=True)
    sale_price = models.FloatField(null=True, blank=True)
    discount_type = models.CharField(default='no', max_length=20)
    discount_f = models.FloatField(default=0) # flat
    discount_p = models.FloatField(default=0) # percentage
    discount_amount = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    stock = models.IntegerField(default=1)
    sales = models.IntegerField(default=0)
    sku = models.CharField(max_length=50, blank=True, null =True)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    highlight_choices = (
        ('none', 'None'),
        ('new', 'New'),
        ('hot', 'Hot'),
        ('sale', 'Sale'),
        ('offer', 'Offer'),
        ('featured', 'Featured'),
        ('discount', 'Discount'),
        ('old', 'Old'),
        ('promo', 'Promo'),
        ('flash', 'Flash'),
    )
    highlight = models.CharField(max_length=80, choices=highlight_choices, default='none')
    material = models.CharField(max_length=200, blank=True, null =True)
    origin = models.CharField(max_length=200, blank=True, null =True)
    model = models.CharField(max_length=200, blank=True, null =True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    productWeight = models.CharField(max_length=200, blank=True, null =True)
    packingWeight = models.CharField(max_length=200, blank=True, null =True)
    shipping = models.ForeignKey(ShippingProfile, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)
    has_variants = models.BooleanField(default=False)
    color_variant = models.BooleanField(default=True)
    size_variant = models.BooleanField(default=True)
    weight_variant = models.BooleanField(default=False)
    model_variant = models.BooleanField(default=False)
    material_variant = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    video = models.FileField(null=True, blank=True)
    # other
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # physical store location
    warehouse = models.CharField(max_length=20, default='N/A', null=True, blank=True)
    room = models.CharField(max_length=20, default='N/A', null=True, blank=True)
    section = models.CharField(max_length=20, default='N/A', null=True, blank=True)
    shelf = models.CharField(max_length=20, default='N/A', null=True, blank=True)
    rack = models.CharField(max_length=20, default='N/A', null=True, blank=True)
    drawer = models.CharField(max_length=20, default='N/A', null=True, blank=True)
    file = models.CharField(max_length=20, default='N/A', null=True, blank=True)
    # more
    cj_pid = models.CharField(max_length=300, blank=True, null =True)
    oxymanager_id = models.CharField(max_length=300, blank=True, null =True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.pk and not self.shipping:
            self.draft = True
            self.active = False
        # discount calculation 
        if self.discount_type == 'flat':
            self.discount_amount = self.discount_f
        elif self.discount_type == 'percentage':
            self.discount_amount = self.sale_price * (self.discount_p / 100)
        else:
            self.discount_amount = 0
        if self.discount_amount > self.sale_price:
            self.discount_amount = self.sale_price
        if self.discount_amount:
            self.discounted_price = self.sale_price - self.discount_amount
        else:
            self.discounted_price = 0
        super(Product, self).save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')
    thumbnail = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name
    def save(self, *args, **kwargs):
        self.image = compressImage(self.image, 900, 900)
        self.thumbnail = compressImage(self.image, 300, 300)
        super(ProductImage, self).save(*args, **kwargs)

class VariantSuggestion(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, null=True,  blank=True, on_delete=models.CASCADE)
    buy_price = models.DecimalField(blank = True, null =True, decimal_places=2, max_digits=10)
    sale_price = models.DecimalField(blank = True, null =True, decimal_places=2, max_digits=10)
    stock = models.IntegerField(blank = True, default= 1, null =True)
    # variation attributes 
    color = models.CharField(max_length=100, blank = True, null =True)
    size = models.CharField(max_length=100, blank = True, null =True)
    weight = models.CharField(max_length=100, blank = True, null =True)
    model = models.CharField(max_length=100, blank = True, null =True)
    material = models.CharField(max_length=100, blank = True, null =True)
    def __str__(self):
        return self.product.name
    def save(self, *args, **kwargs):
        if not self.pk:
            section = self.product.categories.first().section
            if self.color:
                VariantSuggestion.objects.get_or_create(name='color', value=self.color, section=section)
            if self.size:
                VariantSuggestion.objects.get_or_create(name='size', value=self.size, section=section)
            if self.weight:
                VariantSuggestion.objects.get_or_create(name='weight', value=self.weight, section=section)
            if self.model:
                VariantSuggestion.objects.get_or_create(name='model', value=self.model, section=section)
            if self.material:
                VariantSuggestion.objects.get_or_create(name='material', value=self.material, section=section)
        super(ProductVariant, self).save(*args, **kwargs)

class Review(models.Model):
    product = models.ForeignKey(Product, null=False,  blank=False, on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", null=True,  blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank = False, null =False, default='No Name')
    rating = models.FloatField(max_length=7, blank=True, null =True)
    review = models.TextField(max_length=500, blank = True, null =True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product)
    def save(self, *args, **kwargs):
        if self.by_admin:
            Notification.objects.create(type="review", content="Your shop got a new review", account=self.product.shop.account)
            send_mail('Your shop got a new review', new_review_message, [self.product.shop.account.email])
        super(Review, self).save(*args, **kwargs)

# Product end 

# customer and order 
    
class Customer(models.Model):
    CUS_STATUS = (
        ('Level 1', 'Level 1'),
        ('Level 2', 'Level 2'),
        ('Level 3', 'Level 3'),
        ('Level 4', 'Level 4'),
        ('Suspended', 'Suspended'),
    )
    shop = models.ForeignKey(Shop, null=False,  blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank = False, null =False, default = '')
    user = models.OneToOneField(User, null=True,  blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank = True)
    email = models.EmailField(max_length=100, blank = True)
    status = models.CharField(max_length=20, choices = CUS_STATUS, default='Level 1')
    created_at = models.DateTimeField(auto_now_add=True)
    reviewables = models.JSONField(default=list)
    def __str__(self):
        return self.user.username

class Leads(models.Model):
    shop = models.ForeignKey(Shop, null=False,  blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank = True, null =True)
    phone = models.CharField(max_length=20, blank = True, null =True)
    email = models.EmailField(max_length=100, blank = True, null =True)
    whatsapp = models.EmailField(max_length=100, blank = True, null =True)
    skype = models.EmailField(max_length=100, blank = True, null =True)
    website = models.EmailField(max_length=100, blank = True, null =True)
    facebook = models.EmailField(max_length=100, blank = True, null =True)
    message = models.EmailField(max_length=100, blank = True, null =True)
    note = models.EmailField(max_length=100, blank = True, null =True)
    label = models.EmailField(max_length=100, blank = True, null =True)
    extra = models.EmailField(max_length=100, blank = True, null =True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="No Status")
    def __str__(self):
        return self.shop.name + ' ' + str(self.id)

class Subscriber(models.Model):
    shop = models.ForeignKey(Shop, null=False,  blank=False, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    
class Address(models.Model):
    type_choice = (
        ('billing', 'billing'),
        ('shipping', 'shipping'),
    )
    customer = models.ForeignKey(Customer, null=True,  blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank = True, null=True)
    last_name = models.CharField(max_length=100, blank = True, null=True)
    email = models.CharField(max_length=100, blank = True, null=True)
    phone = models.CharField(max_length=100, blank = True, null=True)
    primary = models.BooleanField(default = False, blank = False)
    street_address = models.CharField(max_length=500, blank = True)
    city = models.CharField(max_length=500, blank = True)
    state = models.CharField(max_length=500, blank = True)
    zip_code = models.CharField(max_length=500, blank = True)
    type = models.CharField(max_length=20, choices = type_choice, default='billing')
    country  = models.CharField(max_length=100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    shop = models.ForeignKey(Shop, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank = False, null =False, default = '')
    email = models.EmailField(max_length=100, blank = False, null =False, default = '')
    phone = models.CharField(max_length=20, blank = False, null =False, default = '')
    message = models.TextField(max_length=500, blank = False, null =False, default = '')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class ContactReply(models.Model):
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=500, blank = False, null =False, default = '')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.contact.name

# Order start

class Coupon(models.Model):
    COUPON_TYPE = (
        ('fixed', 'fixed'),
        ('percent', 'percent'),
    )
    shop = models.ForeignKey(Shop, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=100, blank = False, null =False, default = '')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    type = models.CharField(max_length=20, choices = COUPON_TYPE, default='fixed')
    created_at = models.DateTimeField(auto_now_add=True)
    valid_till = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.code

class Order(models.Model):
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True,  blank=True, on_delete=models.SET_NULL)
    items = models.JSONField(null=True, blank=True)
    address = models.ForeignKey(Address, null=True,  blank=True, on_delete=models.SET_NULL)
    method = models.CharField(max_length=30, null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    advance_paid = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.00)
    status = models.CharField(max_length=100, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    def __str__(self):
        return self.shop.name + ' ' + str(self.id)
    def save(self, *args, **kwargs):
        if not self.pk:
            super(Order, self).save(*args, **kwargs)
            pending = Order_status.objects.create(name = 'Pending', note = "Order is pending", order = self)
            self.status = 'Pending'
            Notification.objects.create(type="order", content="New order received", account=self.shop.account)
            send_mail('New order received', new_order_message, [self.shop.account.email])
        else:
            super(Order, self).save(*args, **kwargs)
        

class Order_status(models.Model):
    order = models.ForeignKey(Order, null=True,  blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank = False, null =False, default='')
    note = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.pk:
            self.order.status = self.name
            self.order.save()
        super(Order_status, self).save(*args, **kwargs)

# other 


class ShopTheme(models.Model): #will be removed
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    purchased_on = models.DateTimeField(auto_now_add=True)
    valid_till = models.DateTimeField(null=True, blank=True)
    activated = models.BooleanField(default=False)
    data1 = models.TextField(null=True, blank=True)
    data2 = models.TextField(null=True, blank=True)
    data3 = models.TextField(null=True, blank=True)
    class Meta:
        unique_together = ('shop','theme')
    def __str__(self):
        return self.shop.name+' '+self.theme.name
    def save(self, *args, **kwargs):
        if not self.data1 and self.theme.data1:
            self.data1 = self.theme.data1
        if not self.data2 and self.theme.data2:
            self.data2 = self.theme.data2
        if not self.data3 and self.theme.data3:
            self.data3 = self.theme.data3
        print(self.shop.account,self.shop.account.affiliate, 66)
        if not self.pk and self.shop.account and self.shop.account.affiliate:
            st, ct = Settings.objects.get_or_create()
            com = Commission(affiliate = self.shop.account.affiliate, title='Theme Purchase', commission=calcP(self.theme.price, st.affiliate_commission))
            com.save()
        super(ShopTheme, self).save(*args, **kwargs)

class Page(models.Model):
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank = False, null =False, default='')
    slug = models.SlugField(max_length=100, blank = True, null =True, default='')
    mandatory = models.BooleanField(default=False)
    content = models.TextField(blank = True, null =True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Staff(models.Model):
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank = False, null =False, default='')
    phone = models.CharField(max_length=20, blank = True)
    email = models.EmailField(max_length=100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


# Email
class EmailTemplate(models.Model):
    ACTION_CHOICES = (
        ('registration', 'registration'),
        ('forget_password', 'forget_password'),
        ('new_order', 'new_order'),
        ('order_status', 'order_status'),
        ('ticket_reply', 'ticket_reply'),
    )
    # ['registration', 'forget_password', 'new_order', 'order_status', 'ticket_reply']
    action = models.CharField(max_length=100, blank = False, null =False, choices=ACTION_CHOICES)
    variables = models.JSONField(default=list, blank = True, null =True)
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank = False, null =False, default='')
    body = models.TextField(blank = True, null =True)
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.action

class EmailMessage(models.Model):
    shop = models.ForeignKey(Shop, null=True,  blank=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True,  blank=True, on_delete=models.CASCADE)
    to = models.CharField(max_length=100, blank = False, null =False, default='')
    subject = models.CharField(max_length=100, blank = False, null =False, default='')
    body = models.TextField(blank = True, null =True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject





# Plugins 

class Plugin(models.Model):
    TYPE_CHOICES = (
        ('seo', 'seo'),
        ('payment', 'payment'),
        ('tools', 'tools'),
        ('dropshipping', 'dropshipping'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='tools')
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=200, null=True, blank=True)
    instruction = models.TextField(default='Plugin Instruction here')
    code = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='plugins/', null=True, blank=True)
    feature_image = models.ImageField(upload_to='plugins/', null=True, blank=True)
    extra_image_1 = models.ImageField(upload_to='plugins/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    default_data = {
        'fields': {}
    }
    data = models.JSONField(default=default_data)
    class Meta:
        unique_together = ('code',)
    def __str__(self):
        return self.name

# {
#     "fields": {
#         "Username": {
#             "help": "Cj username",
#             "required": "true",
#             "type": "text",
#             "value": ""
#         },
#         "Password": {
#             "help": "Cj password",
#             "required": "true",
#             "type": "password",
#             "value": ""
#         }
#     }
# }

class ShopPlugin(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    purchased_on = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    data = models.JSONField(null=True, blank=True)
    class Meta:
        unique_together = ('shop','plugin')
    def __str__(self):
        return self.shop.name+' '+self.plugin.name
    def save(self, *args, **kwargs):
        if not self.pk:
            self.data = self.plugin.data
        # check all required fields filled before activating
        fields = self.data['fields']
        if self.activated:
            for field in fields:
                if fields[field]['required'] == 'true' and fields[field]['value'] == '':
                    self.activated = False
                    super(ShopPlugin, self).save(*args, **kwargs)
                    break
        # cj dropshipping start code: cj
        if self.plugin.code == 'cj':
            # get access token by post request https://developers.cjdropshipping.com/api2.0/v1/authentication/getAccessToken with email and password from fields, json headers
            if self.activated:
                try:
                    url = "https://developers.cjdropshipping.com/api2.0/v1/authentication/getAccessToken"
                    header = {
                        'Content-Type': 'application/json',
                    }
                    payload = {
                        "email": fields['Email']['value'],
                        "password": fields['Password']['value']
                    }
                    res = requests.request("POST", url, headers=header, data = json.dumps(payload))
                    res = res.json()
                    if 'success' in res and 'data' in res and res['success'] == True and 'accessToken' in res['data'] and 'accessTokenExpiryDate' in res['data']:
                        self.data['accessToken'] = res['data']['accessToken']
                        self.data['accessTokenExpiryDate'] = res['data']['accessTokenExpiryDate']
                        super(ShopPlugin, self).save(*args, **kwargs)
                    else:
                        self.activated = False
                        super(ShopPlugin, self).save(*args, **kwargs)
                except:
                    self.activated = False
                    super(ShopPlugin, self).save(*args, **kwargs)

        if self.plugin.code == 'robots':
            content = fields['Content']['value']
            print(66666666666666666666, content)
            if self.activated:
                seo, ct = Seo.objects.get_or_create(shop=self.shop)
                seo.robots = content
                seo.save()


        # cj dropshipping end
        super(ShopPlugin, self).save(*args, **kwargs)

class Seo(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    sitemap = models.TextField(null=True, blank=True)
    robots = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.shop.name
