# Consume/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

from .models import Consume

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from backend.product.models import Product  # Ajuste o caminho para o modelo Product
from django.utils.text import slugify
from django.http import HttpResponse

import csv

@admin.action(description="Exportar consumos selecionados como CSV")
def export_selected_as_csv(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="consumes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Produto', 'Consumo Histórico', 'CV Diário', 'Demanda Dia Prev'])
    for consume in queryset:
        writer.writerow([
            consume.product.title, consume.consumo_historico,
            consume.cv_diario, consume.demanda_dia_prev
        ])

    return response


class ConsumeResource(resources.ModelResource):
    # product = Field(attribute='product', column_name='product_title')
    product = Field(attribute='product', column_name='codigo', widget=ForeignKeyWidget(Product, 'codigo'))

    class Meta:
        model = Consume
        import_id_fields = ['id']
        fields = ('id','product', 'consumo_historico', 'cv_diario', 'cv_periodo_lt',
                  'demanda_dia_prev', 'fator_k', 'menor_lote_consumo')
        export_order = ('product', 'consumo_historico', 'cv_diario',
                        'cv_periodo_lt', 'demanda_dia_prev', 'fator_k', 'menor_lote_consumo')

    # def before_import_row(self, row, **kwargs):
    #     # Buscar o produto pelo título antes de salvar
    #     # product_title = row.get('product_title')
    #     product_title = row.get('codigo')
    #     row['product'] = Product.objects.filter(title=product_title).first()

    # def before_import_row(self, row, **kwargs):
    #     # Pegando o código do produto da linha
    #     product_codigo = str(row.get('codigo', '').strip())  # Garantir que o código seja uma string
    #     print(f"Processando produto com código: {product_codigo}")

    #     # Buscar o produto no banco de dados com base no código
    #     product = Product.objects.filter(codigo=product_codigo).first()
    #     print(f"Get produto com código: {product}")
    #     # Criar uma instância de Consume associando o produto
    #     consume_instance = Consume.objects.create(product=product)

    #     # Verificar se o produto foi associado corretamente
    #     print(consume_instance.product)  # Deve imprimir a instância do produto, algo como <Product: 19225>


    #     if product:
    #         # Atribuir a instância do produto ao campo 'product' (não o código)
    #         # Verifique se product é uma instância de Product]
    #         # consume_instance.product = product

    #         print(f"Produto encontrado: {product}, Tipo de produto: {type(product)}")
    #         row['product'] = product  # Aqui você está atribuindo a instância do Product
    #         print(f"Produto encontrado: {product}")
    #         return row
    #     else:
    #         print(f"Produto com código '{product_codigo}' não encontrado. Linha ignorada.")
    #         row['product'] = None  # A linha será ignorada, pois o produto não foi encontrado

    #         # Se você preferir interromper a importação ao não encontrar o produto:
    #         raise ValueError(f"Produto com código '{product_codigo}' não encontrado.")

@admin.register(Consume)
class ConsumeAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [ConsumeResource]

    readonly_fields = ('slug',)

    # list_display = ( "consumo_historico",
    #                 "cv_diario", "cv_periodo_lt", "demanda_dia_prev", "fator_k")

    list_display = ("product_title", "consumo_historico", "cv_diario", "cv_periodo_lt", "demanda_dia_prev", "fator_k", "menor_lote_consumo")
    # list_display = ("product", "consumo_historico", "cv_diario", "cv_periodo_lt", "demanda_dia_prev", "fator_k", "menor_lote_consumo")

    def product_title(self, obj):
        # return obj.product
        return obj.product.title

    product_title.short_description = 'Produto'



    # list_filter = ('planta', 'codigo')
    # search_fields = ('planta', 'codigo')
    # fieldsets = (
    #     # (None, {
    #     #     'fields': ('planta', 'codigo')
    #     # }),
    #     ('Informações adicionais', {
    #         'fields': ("consumo_historico",
    #                 "cv_diario", "cv_periodo_lt", "demanda_dia_prev", "fator_k")
    #     }),
    # )
    list_filter = ('product',)

    fieldsets = (
        ('Produto', {
            'fields': ('product',)
        }),
        ('Informações adicionais', {
            'fields': (
                "consumo_historico", "cv_diario", "cv_periodo_lt",
                "demanda_dia_prev", "fator_k", "menor_lote_consumo"
            )
        }),
        ('Slug', {
            'fields': ('slug',),
            'classes': ('collapse',),  # Torna o campo colapsável
        }),
    )

    # search_fields = ('product__title',)
    search_fields = ('product__title', 'product__codigo')

    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        if not obj.slug:  # Gerar slug apenas se não existir
            obj.slug = slugify(obj.product.title)
        obj.save()