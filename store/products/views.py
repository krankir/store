from django.shortcuts import render


def index(request):
    context = {
        'title': 'test title',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'TEST TITLE'
    }
    return render(request, 'products/products.html', context)
