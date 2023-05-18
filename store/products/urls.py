from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import index, products

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
