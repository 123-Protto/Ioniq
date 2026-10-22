from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Product
from .forms import EnquiryForm

def home(request):
    products = Product.objects.filter(is_active=True, featured=True)[:6]
    return render(request, 'website/home.html', {'products': products, 'form': EnquiryForm()})

def products(request):
    items = Product.objects.filter(is_active=True)
    category = request.GET.get('category', '')
    if category in dict(Product.CATEGORY_CHOICES): items = items.filter(category=category)
    return render(request, 'website/products.html', {'products': items, 'categories': Product.CATEGORY_CHOICES, 'active_category': category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'website/product_detail.html', {'product': product, 'form': EnquiryForm(initial={'product_interest': product.category})})

@require_http_methods(['GET','POST'])
def contact(request):
    form = EnquiryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Thank you! Your enquiry has been received. Our team will contact you soon.')
        return redirect('contact')
    return render(request, 'website/contact.html', {'form': form})

def about(request): return render(request, 'website/about.html')
