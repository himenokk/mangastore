from django.shortcuts import render
from products.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'tittle': 'Mangastore',
        'username': 'Sanzhar',
    }
    return render(request, 'products/index.html', context)

def about(request):
    return render(request, 'products/about.html')
def news(request):
    return render(request, 'products/news.html')

def products(request):
    context = {
        'title': 'Mangastore - products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)