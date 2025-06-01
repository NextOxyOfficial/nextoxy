from django.db import models
from django.contrib.auth.models import User

# sales and employee start 
class Staff(models.Model):
    STAFF_TYPE_CHOICES = (
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('employee', 'employee'),
    )
    type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES, default='employee')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Basic information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # Address information
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    # Employment information
    job_title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Additional fields if needed
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Additional fields if needed
    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('cancelled', 'Cancelled'),
        ('delivered', 'Delivered'),
        ('cashed_in', 'Cashed In'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='processing')
    shipping_id = models.CharField(max_length=100, blank=True, null=True)
    customer_full_name = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()
    salesperson = models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True)
    order_note_1 = models.TextField(blank=True, null=True)
    order_note_2 = models.TextField(blank=True, null=True)
    order_note_3 = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Order #{self.id} - {self.customer_full_name}"


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name

class Contact_reply(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    reply = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.contact.name

class Custom_order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    f_name = models.CharField(max_length=100, null=True, blank=True)
    l_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    type = models.CharField(null=True, blank=True, max_length=50)
    def __str__(self):
        return self.f_name