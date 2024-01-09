from django.contrib import admin
from .models import Sede, Residente, MedicoResidente, MedicoStaff, CuerpoAdmin, Preinforme

admin.site.register(Sede,)
admin.site.register(Residente,)
admin.site.register(MedicoResidente,)
admin.site.register(MedicoStaff,)
admin.site.register(CuerpoAdmin,)
admin.site.register(Preinforme,)




