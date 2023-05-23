from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import index, products, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path(
        'baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
