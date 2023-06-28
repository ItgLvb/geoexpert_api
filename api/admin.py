from django.contrib import admin
from .models import CadastralPlot


@admin.register(CadastralPlot)
class CadastralPlotAdmin(admin.ModelAdmin):
    search_fields = ['cadastral_number']
