from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'test title',
    }
    return render(request, 'products/index.html', context)


def products(request):
    print(request)
    object_list = Product.objects.all
    category_list = ProductCategory.objects.all()
    context = {
        'title': 'TEST TITLE',
        'object_list': object_list,
        'category': category_list,
    }
    return render(request, 'products/products.html', context)
