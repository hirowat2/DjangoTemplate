from django.contrib import admin
from .models import DynamicVariable

class DynamicVariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name',)

admin.site.register(DynamicVariable, DynamicVariableAdmin)
