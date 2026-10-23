from django.contrib import admin
from .models import Product, Enquiry
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','capacity_ah','featured','is_active','sort_order')
    list_filter = ('category','featured','is_active')
    search_fields = ('name','short_description','description')
    list_editable = ('featured','is_active','sort_order')
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','phone','product_interest','location','created_at','is_contacted')
    list_filter = ('product_interest','is_contacted','created_at')
    search_fields = ('name','phone','email','location','message')
    list_editable = ('is_contacted',)
    readonly_fields = ('created_at',)
