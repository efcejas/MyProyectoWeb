from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('sedes/', views.sedes, name='sedes'),
    path('agregarsede/', views.agregarsede, name='agregarsede'),
    path('agregar_residente/', views.agregar_residente, name='agregar_residente'),
    path('residentes/', views.residentes, name='residentes'),
    path('supervision_residentes/', views.supervision_residentes, name='supervision_residentes'),
    path('accounts/', include('django.contrib.auth.urls')), # nuevas rutas de autenticación
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]