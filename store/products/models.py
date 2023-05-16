from django.db import models


class ProductCategory(models.Model):
    """Категории продуктов."""

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)


class Product(models.Model):
    """Продукты."""

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
