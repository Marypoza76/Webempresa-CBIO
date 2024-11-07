# urls.py
# cbiolab/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('register/', views.register, name='register'),  # Registro
    path('contact/', views.contact, name='contact'),  # Contacto
    path('login/', auth_views.LoginView.as_view(template_name='cbiolab/login.html'), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('services/', views.services, name='services'),  # Servicios
]