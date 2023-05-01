from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from social_core.exceptions import AuthCanceled, AuthFailed
from django.contrib.auth import login, authenticate
from social_core.backends.oauth import BaseOAuth2
from social_django.models import UserSocialAuth
from django.contrib.auth import login
from social_core.backends.facebook import FacebookOAuth2
from social_core.backends.google import GoogleOAuth2
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView






def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def logout(request):
    return redirect('/')

@login_required
def home(request):
    return render(request, 'home.html')

def auth_exception_handler(request, exception):
    return render(request, 'login.html', {'error': exception})

def social_register(request, backend):
    user = authenticate(request=request, backend=backend)
    if user:
        login(request, user)
        return redirect('home')
    else:
        return redirect('register')

def save_profile(backend, user, response, *args, **kwargs):
    if isinstance(backend, BaseOAuth2):
        profile = user.profile
        if backend.name == 'facebook':
            profile.avatar = f'https://graph.facebook.com/{response["id"]}/picture?type=large'
        elif backend.name == 'google-oauth2':
            profile.avatar = response.get('picture', '')
        profile.save()


@login_required
def social_auth(request, provider):
    try:
        user_social_auth = UserSocialAuth.objects.get(provider=provider, user=request.user)
    except UserSocialAuth.DoesNotExist:
        user_social_auth = None

    if user_social_auth:
        return redirect('/')
    else:
        return render(request, 'register.html', {'provider': provider})

@login_required
def social_auth_complete(request, provider):
    social_user = request.user.social_auth.filter(provider=provider).first()

    if social_user:
        login(request, social_user.user)
        return redirect('/')
    else:
        return redirect('/social-auth/' + provider)

def social_auth_complete(request, backend):
    if isinstance(request.backend, FacebookOAuth2) or isinstance(request.backend, GoogleOAuth2):
        if request.user.is_authenticated:
            # Pengguna sudah masuk, tambahkan koneksi ke akun sosialnya.
            request.backend.auth_complete(request.user.social_auth.first())
            messages.success(request, 'Koneksi akun sosial berhasil ditambahkan.')
        else:
            # Pengguna belum masuk, coba masuk dengan akun sosialnya.
            user = request.backend.do_auth(request)
            auth_login(request, user)
            messages.success(request, 'Anda berhasil masuk dengan akun sosial.')
        return redirect('/')
    else:
        # Provider autentikasi sosial yang digunakan tidak didukung.
        return HttpResponseBadRequest('Provider tidak didukung.')


def social_auth_complete(request, provider):
    return redirect('home')


def get_user_profile(request):
    user = request.user
    user_social = UserSocialAuth.objects.get(user=user)
    user_profile = user_social.extra_data

    
    user_id = user_social.uid
    user_name = user_profile['name']
    user_email = user_profile['email']
    user_picture = user_profile['picture']

    return render(request, 'profile.html', {
        'user_id': user_id,
        'user_name': user_name,
        'user_email': user_email,
        'user_picture': user_picture,
    })


class FacebookOAuth2LoginView(OAuth2LoginView):
    adapter_class = FacebookOAuth2Adapter


# def home(request):
#     context = {
#     }
        
#     return render(request,'index.html',context)
