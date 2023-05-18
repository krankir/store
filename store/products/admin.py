from django.contrib import admin

from products.models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    ...


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'price', 'quantity', 'image', 'category',
    )
    empty_value_display = 'Не выбрано.'
