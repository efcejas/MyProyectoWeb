from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from .views import CustomPasswordChangeView, PreinformeView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('sedes/', views.sedes, name='sedes'),
    path('agregarsede/', views.agregarsede, name='agregarsede'),
    path('agregar_residente/', views.agregar_residente, name='agregar_residente'),
    path('residentes/', views.residentes, name='residentes'),
    path('supervision_residentes/', views.supervision_residentes,
         name='supervision_residentes'),  # nuevas rutas de autenticación
    # abajo están las rutas de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name="registration/cambiar_contraseña_confir.html"), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
         template_name='registration/restablecer_contraseña.html',
         email_template_name='registration/restablecer_contraseña_email.html',
         subject_template_name='registration/restablecer_contraseña_objeto.txt',
         success_url='/password_reset/done/',
         from_email='soporte.residentesdm@hotmail.com',
         ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name="registration/restablecer_contraseña_confir.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/confirmar_restablecimiento_contraseña.html',
         success_url='/password_reset_complete/',), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name="registration/restablecimiento_contraseña_completado.html"), name='password_reset_complete'),
    # abajo están las rutas de las actividades de los residentes
    path('preinforme/', PreinformeView.as_view(), name='preinforme'),
]
