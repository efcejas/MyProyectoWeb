# Importaciones de Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Importaciones de aplicaciones locales
from .models import MyUsuario

# Configuración de administrador para MyUsuario
class MyUsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'fecha_nacimiento', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (('Información personal'), {'fields': ('fecha_nacimiento',)}),
    )

# Registrar MyUsuario con MyUsuarioAdmin
admin.site.register(MyUsuario, MyUsuarioAdmin)





