from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.models import Product, ProductCategory, Basket

User = get_user_model()


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


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.last()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
