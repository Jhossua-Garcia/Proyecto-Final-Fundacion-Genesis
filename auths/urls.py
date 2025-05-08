from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activar_cuenta/<uidb64>/<token>/', views.activar_cuenta, name='activar_cuenta'),
    path('olvidar_password/', views.olvidar_password, name='olvidar_password'),
    path('valida_cuenta_recuperada/<uidb64>/<token>/', views.validar_cuenta_recuperada, name='valida_cuenta_recuperada'), 
    path('recuperar_password/', views.recuperar_password, name='recuperar_password'),
]
