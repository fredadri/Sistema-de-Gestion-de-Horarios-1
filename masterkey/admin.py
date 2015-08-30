__author__ = 'david'
from django.contrib import admin
from models import *


class SeguimientoAdmin(admin.ModelAdmin):
	list_display = ('id','estudiante','comentario','estado')
	list_filter = ('estudiante',)
	search_fields = ('id',)
	list_editable = ('estado',)







admin.site.register(Contrato)
admin.site.register(Ciudad)
admin.site.register(Sede)
admin.site.register(Estudiante)
admin.site.register(Programa)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Nivel)
admin.site.register(Academic_Rank)
admin.site.register(Seguimiento,SeguimientoAdmin)
admin.site.register(Estado)
admin.site.register(Actividad)
