from django.contrib import admin
from core.models import *

@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao','tipo_validacao', 'peso']



@admin.register(Analista)
class AnalistaAdmin(admin.ModelAdmin):
    list_display = ['id', 'matricula', 'nome']
