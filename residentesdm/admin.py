# Importaciones de Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Importaciones de aplicaciones locales
from .models import MyUsuario, Residente, CuerpoAdmin

# Configuración de administrador para MyUsuario
class MyUsuarioAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'fecha_nacimiento', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (('Información personal'), {'fields': ('fecha_nacimiento',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('Información personal'), {'fields': ('fecha_nacimiento',)}),
    )


# Registrar MyUsuario con MyUsuarioAdmin
admin.site.register(MyUsuario, MyUsuarioAdmin)
admin.site.register(Residente)
admin.site.register(CuerpoAdmin)





