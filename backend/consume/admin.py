# Consume/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

from .models import Consume


class ConsumeResource(resources.ModelResource):

    class Meta:
        model = Consume


@admin.register(Consume)
class ConsumeAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [ConsumeResource]

    readonly_fields = ('slug',)

    list_display = ( "planta", "codigo", "description", "consumo_historico",
                    "cv_diario", "cv_periodo_lt", "demanda_dia_prev", "fator_k")


    list_filter = ('planta', 'codigo')
    search_fields = ('planta', 'codigo')
    fieldsets = (
        (None, {
            'fields': ('planta', 'codigo')
        }),
        ('Informações adicionais', {
            'fields': ("description", "consumo_historico",
                    "cv_diario", "cv_periodo_lt", "demanda_dia_prev", "fator_k")
        }),
    )

    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        obj.save()
