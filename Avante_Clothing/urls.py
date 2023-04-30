
from django.contrib import admin
from django.urls import path,include
from .views import social_auth, social_auth_complete
from social_django import urls as social_django_urls

from . import views

app_name = 'social_django'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('social-auth/<provider>/', social_auth, name='social_auth'),
    path('social_auth-complete/<provider>/', social_auth_complete, name='social_auth_complete'),
    path('social/', include('social_django.urls', namespace='social')),
    # path('accuonts/',include('django.contrib.auth.urls')),
    # path('Sigup',include('Akun.urls')),
    path('Produk/',include('Produk.urls')),
    path('Pelanggan/',include('Pelanggan.urls')),
    path('Pengiriman/',include('Pengiriman.urls')),
    path('Ulasan/',include('Ulasan.urls')),
    path('social*auth/', include('social_django.urls', namespace='social')),
]
