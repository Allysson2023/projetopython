from django.contrib import admin
from contact import models

@admin.register(models.Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = 'data', 'apt', 'nome', 'receberam',
    ordering = '-id',
    search_fields = 'data', 'apt', 'nome', 'receberam',
    list_per_page = 20
    list_display_links ='data', 'nome',
    list_editable = 'receberam',

@admin.register(models.Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = 'data', 'nomeResp',
    ordering = '-id',
    search_fields = 'data', 'nomeResp',
    list_per_page = 20
    list_display_links ='data', 'nomeResp',
    