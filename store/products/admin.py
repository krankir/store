from django.contrib import admin

from products.models import ProductCategory, Product, Basket


@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    ...


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'quantity', 'category',
    )
    fields = (
        'name', 'description', ('price', 'quantity'), 'image',
        'category',
    )
    empty_value_display = 'Не выбрано.'
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('price',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
