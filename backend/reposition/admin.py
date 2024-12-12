# Reposition/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

from .models import Reposition

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from backend.product.models import Product  # Ajuste o caminho para o modelo Product
from django.utils.text import slugify
from django.http import HttpResponse
import csv

@admin.action(description="Exportar reposições selecionados como CSV")
def export_selected_as_csv(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reposição.csv"'

    writer = csv.writer(response)
    writer.writerow(['Produto', 'Lead Time ordem', 'CV lead time'])
    for reposition in queryset:
        writer.writerow([
            reposition.product.title, reposition.lt_ordem,
            reposition.cv_lead_time
        ])

    return response

class RepositionResource(resources.ModelResource):
    # product = Field(attribute='product', column_name='product_title')
    product = Field(attribute='product', column_name='codigo', widget=ForeignKeyWidget(Product, 'codigo'))
    class Meta:
        model = Reposition
        import_id_fields = ['id']
        fields = ('id','product', 'lt_pre_ordem', 'lt_ordem', 'lt_quarentena',
                  'lt_total', 'cv_lead_time', 'lote_minimo_rep',
                  'lote_multiplo_rep', 'intervalo_reposicao', 'campanha_ideal')
        export_order = ('product', 'lt_pre_ordem', 'lt_ordem', 'lt_quarentena',
                        'lt_total', 'cv_lead_time', 'lote_minimo_rep',
                        'lote_multiplo_rep', 'intervalo_reposicao',
                        'campanha_ideal')


@admin.register(Reposition)
class RepositionAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [RepositionResource]

    readonly_fields = ('slug',)

    list_display = (
        'product_title',  # Adicionado para exibir o produto relacionado
        'lt_pre_ordem',
        'lt_ordem',
        'lt_quarentena',
        'lt_total',
        'cv_lead_time',
        'lote_minimo_rep',
        'lote_multiplo_rep',
        'intervalo_reposicao',
        'campanha_ideal',
    )
    def product_title(self, obj):
        return obj.product.title

    product_title.short_description = 'Produto'


    list_filter = ('product',)  # Filtro baseado no título do produto
    search_fields = ('product__title', 'product__codigo')  # Pesquisa pelo produto e código
    fieldsets = (
        ('Produto', {
            'fields': ('product',)
        }),
        ('Informações adicionais', {
            'fields': ('lt_pre_ordem',
                       'lt_ordem',
                       'lt_quarentena',
                       'lt_total',
                       'cv_lead_time',
                       'lote_minimo_rep',
                       'lote_multiplo_rep',
                       'intervalo_reposicao',
                       'campanha_ideal')
        }),
        ('Slug', {
            'fields': ('slug',),
            'classes': ('collapse',),  # Torna o campo colapsável
        }),
    )

    search_fields = ('product__title',)

    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        if not obj.slug:  # Gerar slug apenas se não existir
            obj.slug = slugify(obj.product.title)
        obj.save()
