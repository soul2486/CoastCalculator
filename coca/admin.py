# Register your models here.
from django.contrib import admin

from coca.models import Appareil, Devis, InformationsInternaute

# Register your models here.
# Appareil模型的管理器
@admin.register(Appareil)
class AppareilAdmin(admin.ModelAdmin):
    list_display = ["nom", "type", "cote"]
    search_fields = ["nom"]
    list_filter =[]

@admin.register(InformationsInternaute)
class InternauteAdmin(admin.ModelAdmin):
    list_display = ["nom", "email"]
    search_fields = ["nom"]
    list_filter =[]
@admin.register(Devis)
class DevisAdmin(admin.ModelAdmin):
    list_display = ["internaute_temp", "energie_T", 'date']
    search_fields = ["internaute_temp"]
    list_filter =[]
