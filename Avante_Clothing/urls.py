
from django.contrib import admin
from django.urls import path,include
from .views import social_auth, social_auth_complete
from social_django import urls as social_django_urls
from django.views.generic import TemplateView
from social_django.urls import urlpatterns as social_django_urls
from allauth.socialaccount.views import SignupView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2CallbackView
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView
from allauth.account.views import LoginView

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
    path('profile/', views.get_user_profile),
    path('accounts/', LoginView.as_view(), name='account_login'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    
    path('accounts/', include('allauth.urls')),
    # path('accounts/social/signup/', socialaccount_views.signup, name='socialaccount_signup'), 
    # path('accounts/facebook/login/', OAuth2LoginView.as_view(adapter=FacebookOAuth2Adapter), name='fb_login'),
    # path('accounts/facebook/login/callback/', OAuth2CallbackView.as_view(adapter=FacebookOAuth2Adapter), name='fb_callback'),
    path('Produk/',include('Produk.urls')),
    path('Pelanggan/',include('Pelanggan.urls')),
    path('Pengiriman/',include('Pengiriman.urls')),
    path('Ulasan/',include('Ulasan.urls')),
]
urlpatterns += social_django_urls
