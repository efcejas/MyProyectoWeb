from django.contrib import admin
from .models import Sede, Residente, MedicoResidente, MedicoStaff

admin.site.register(Sede,)
admin.site.register(Residente,)
admin.site.register(MedicoResidente,)
admin.site.register(MedicoStaff,)



