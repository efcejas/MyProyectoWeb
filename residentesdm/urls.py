from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('evaluacion/', views.evaluacion, name='evaluacion'),
    path('sedes/', views.sedes, name='sedes'),
    path('agregarsede/', views.agregarsede, name='agregarsede'),
]