from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [('automotive','Automotive'),('pasted','Pasted / Flat Plate'),('solar','Solar'),('tubular','Tubular & Stationary'),('ups','UPS & Inverter')]
    name = models.CharField(max_length=140)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    capacity_ah = models.PositiveIntegerField(blank=True, null=True, help_text='Capacity in Ah, if applicable')
    short_description = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['sort_order', 'name']
    def __str__(self): return self.name

class Enquiry(models.Model):
    PRODUCT_CHOICES = [('', 'Select a product'), *Product.CATEGORY_CHOICES]
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    product_interest = models.CharField(max_length=20, choices=PRODUCT_CHOICES, blank=True)
    location = models.CharField(max_length=160, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at']
    def __str__(self): return f'{self.name} — {self.created_at:%d %b %Y}'
