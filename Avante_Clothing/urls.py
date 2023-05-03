
from django.contrib import admin
from django.urls import path,include

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('Produk/',include('Produk.urls')),
    path('Pelanggan/',include('Pelanggan.urls')),
    path('Pengiriman/',include('Pengiriman.urls')),
    path('Ulasan/',include('Ulasan.urls')),
]

