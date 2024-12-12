# prateleira/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

from .models import Prateleira

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from backend.product.models import Product  # Ajuste o caminho para o modelo Product
from django.utils.text import slugify
from django.http import HttpResponse
import csv

@admin.action(description="Exportar prateleiras selecionados como CSV")
def export_selected_as_csv(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prateleiras.csv"'

    writer = csv.writer(response)
    writer.writerow(['Produto', 'prateleira Histórico', 'CV Diário',
                     'Demanda Dia Prev'])
    for prateleira in queryset:
        writer.writerow([
            prateleira.product.title, prateleira.prateleira_historico,
            prateleira.cv_diario, prateleira.demanda_dia_prev
        ])

    return response


class PrateleiraResource(resources.ModelResource):
    # product = Field(attribute='product', column_name='product_title')
    product = Field(attribute='product', column_name='codigo', widget=ForeignKeyWidget(Product, 'codigo'))
    class Meta:
        model = Prateleira
        import_id_fields = ['id']
        fields = ('id', 'product',
            'formula_calculo',
            'reserva_historico',
            'inicio_reserva',
            'fim_reserva',
            'reserva',
            'segurança',
            'pulmao',
            'ciclo',
            'dep_maximo',
            'dep_medio',
            'quarentena',
            'transito',
            'prateleira_total',
            'pto_reposicao',)
        exclude = ['title']
        export_order = ('product',
            'formula_calculo',
            'reserva_historico',
            'inicio_reserva',
            'fim_reserva',
            'reserva',
            'segurança',
            'pulmao',
            'ciclo',
            'dep_maximo',
            'dep_medio',
            'quarentena',
            'transito',
            'prateleira_total',
            'pto_reposicao',)

    # def before_import_row(self, row, **kwargs):
    #     # Buscar o produto pelo título antes de salvar
    #     product_title = row.get('product_title')
    #     row['product'] = Product.objects.filter(title=product_title).first()



@admin.register(Prateleira)
class PrateleiraAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [PrateleiraResource]

    readonly_fields = ('slug',)
    list_display = ("product_title",
            'formula_calculo',
            'reserva_historico',
            'inicio_reserva',
            'fim_reserva',
            'reserva',
            'segurança',
            'pulmao',
            'ciclo',
            'dep_maximo',
            'dep_medio',
            'quarentena',
            'transito',
            'prateleira_total',
            'pto_reposicao',)

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
            'formula_calculo',
            'reserva_historico',
            'inicio_reserva',
            'fim_reserva',
            'reserva',
            'segurança',
            'pulmao',
            'ciclo',
            'dep_maximo',
            'dep_medio',
            'quarentena',
            'transito',
            'prateleira_total',
            'pto_reposicao',
            )
        }),
        ('Slug', {
            'fields': ('slug',),
            'classes': ('collapse',),  # Torna o campo colapsável
        }),
    )

    search_fields = ('product__title', 'product__codigo')

    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        if not obj.slug:  # Gerar slug apenas se não existir
            obj.slug = slugify(obj.product.title)
        obj.save()
