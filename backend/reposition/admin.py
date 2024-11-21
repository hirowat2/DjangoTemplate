# Reposition/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

from .models import Reposition


class RepositionResource(resources.ModelResource):

    class Meta:
        model = Reposition


@admin.register(Reposition)
class RepositionAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [RepositionResource]

    readonly_fields = ('slug',)

    list_display = (
        'planta',
        'codigo',
        'description',
        'lt_pre_ordem',
        'lt_ordem',
        'lt_quarentena',
        'lt_total',
        'cv_lead_time',
        'lote_minimo_rep',
        'lote_multiplo_rep',
        'intervalo_reposicao',
        'campanha_ideal')


    list_filter = ('planta', 'codigo')
    search_fields = ('planta', 'codigo')
    fieldsets = (
        (None, {
            'fields': ('planta', 'codigo')
        }),
        ('Informações adicionais', {
            'fields': ("description",
                       'lt_pre_ordem',
                       'lt_ordem',
                       'lt_quarentena',
                       'lt_total',
                       'cv_lead_time',
                       'lote_minimo_rep',
                       'lote_multiplo_rep',
                       'intervalo_reposicao',
                       'campanha_ideal')
        }),
    )

    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        obj.save()
