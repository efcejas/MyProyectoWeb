from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sedes/', views.sedes, name='sedes'),
    path('agregarsede/', views.agregarsede, name='agregarsede'),
    path('agregar_residente/', views.agregar_residente, name='agregar_residente'),
]