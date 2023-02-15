import django.contrib.auth.views
from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('entrar/', django.contrib.auth.views.LoginView.as_view(), {
        'template_name': 'registration/login.html'
    }, name='login'),
    path('sair/', django.contrib.auth.views.LogoutView.as_view(), {
        'next_page': 'core:home'
    }, name='logout'),
    path('cadastre-se/', views.register, name='register')
]
