from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_login, name='login'),
    path('barbearia/', views.pagina_barbearia, name='barbearia'),
]