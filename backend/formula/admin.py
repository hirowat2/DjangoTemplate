from django.contrib import admin
from .models import Formula, DataSet

@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ('name', 'expression')

@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'a', 'b', 'c')
