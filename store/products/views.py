from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from django.core.paginator import Paginator


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


def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    per_page = 6
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Mangastore - products',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,

    }

    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
