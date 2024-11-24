# Consume/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

from .models import Consume

from import_export.fields import Field
from backend.product.models import Product  # Ajuste o caminho para o modelo Product
from django.utils.text import slugify
from django.http import HttpResponse
import csv

@admin.action(description="Exportar consumos selecionados como CSV")
def export_selected_as_csv(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="consumes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Produto', 'Consumo Histórico', 'CV Diário',
                     'Demanda Dia Prev'])
    for consume in queryset:
        writer.writerow([
            consume.product.title, consume.consumo_historico,
            consume.cv_diario, consume.demanda_dia_prev
        ])

    return response


class ConsumeResource(resources.ModelResource):
    product = Field(attribute='product', column_name='product_title')

    class Meta:
        model = Consume
        fields = ('product', 'consumo_historico', 'cv_diario', 'cv_periodo_lt',
                  'demanda_dia_prev', 'fator_k')
        export_order = ('product', 'consumo_historico', 'cv_diario',
                        'cv_periodo_lt', 'demanda_dia_prev', 'fator_k')

    def before_import_row(self, row, **kwargs):
        # Buscar o produto pelo título antes de salvar
        product_title = row.get('product_title')
        row['product'] = Product.objects.filter(title=product_title).first()



@admin.register(Consume)
class ConsumeAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [ConsumeResource]

    readonly_fields = ('slug',)
    list_display = ("product_title", "consumo_historico", "cv_diario",
                    "cv_periodo_lt", "demanda_dia_prev", "fator_k")

    def product_title(self, obj):
        return obj.product.title

    product_title.short_description = 'Produto'

    list_filter = ('product',)

    fieldsets = (
        ('Produto', {
            'fields': ('product',)
        }),
        ('Informações adicionais', {
            'fields': (
                "consumo_historico", "cv_diario", "cv_periodo_lt",
                "demanda_dia_prev", "fator_k"
            )
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
