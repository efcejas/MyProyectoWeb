# Importaciones de Django
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# Importaciones locales
from . import views
from .views import CustomPasswordChangeView, register

urlpatterns = [
    # Ruta de inicio
    path('', views.inicio, name='inicio'),

    # Rutas de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'), # No se necesita una vista personalizada para el login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Rutas para cambio de contraseña
    path('password_change/', CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name="registration/cambiar_contraseña_confir.html"), name='password_change_done'),

    # Rutas para restablecimiento de contraseña
    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/restablecer_contraseña.html',
        email_template_name='registration/restablecer_contraseña_email.html',
        subject_template_name='registration/restablecer_contraseña_objeto.txt',
        success_url='/password_reset/done/',
        from_email='soporte.residentesdm@hotmail.com',
    ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name="registration/restablecer_contraseña_confir.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/confirmar_restablecimiento_contraseña.html',
        success_url='/password_reset_complete/',), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name="registration/restablecimiento_contraseña_completado.html"), name='password_reset_complete'),

    # Rutas de las actividades de los residentes
    # (añade aquí las rutas correspondientes)
]
