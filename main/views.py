from django.shortcuts import render
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'main/category_detail.html', {'category': category, 'products': products})
