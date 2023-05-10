from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def about(request):
    return render(request, 'products/about.html')
def news(request):
    return render(request, 'products/news.html')

def products(request):
    return render(request, 'products/products.html')