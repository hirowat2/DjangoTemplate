from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin
from .models import Product, Category, UnEstoque, Photo, TipoEmbalagem
from backend.segment.models import Segment
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from django.utils.text import slugify
from django.http import HttpResponse

@admin.register(UnEstoque)
class un_estoqueAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)
@admin.register(TipoEmbalagem)
class tipo_embalagemAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)

class ProductResource(resources.ModelResource):
    segmentation = Field(
        column_name='segmentation',
        attribute='segment__title',  # Referência para o campo 'segmentation' no modelo 'Segment'
        widget=ForeignKeyWidget(Segment, 'title')  # Ajustar conforme o nome do campo no Segment
    )
    type_production = Field(
        column_name='type_production',
        attribute='segment__type_prod',  # Referência para 'type_prod' no Segment
        widget=ForeignKeyWidget(Segment, 'type_prod')
    )
    nivel_produto = Field(
        column_name='nivel_produto',
        attribute='segment__prod_level',  # Referência para 'prod_level' no Segment
        widget=ForeignKeyWidget(Segment, 'prod_level')
    )

    class Meta:
        model = Product
        import_id_fields = ['id']
        fields = ('id', 'segment', 'title', 'description', 'price', 'category',
                  'un_estoque', 'tipo_embalagem',
                  'segmentation', 'type_production', 'nivel_produto', 'slug',
                  'planta', 'codigo', 'novo_codigo',
                  'data_validade', 'quantidade_un_embalagem',
                  'quantidade_embalagem_un_armazenamento',
                  'codigo_predecessor')
        export_order = ('segment', 'title', 'description', 'price', 'category',
                        'un_estoque', 'tipo_embalagem',
                        'segmentation', 'type_production', 'nivel_produto',
                        'slug', 'planta', 'codigo', 'novo_codigo',
                        'data_validade', 'quantidade_un_embalagem',
                        'quantidade_embalagem_un_armazenamento',
                        'codigo_predecessor')


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [ProductResource]
    inlines = (PhotoInline,)
    readonly_fields = ('slug',)

    list_display = ('segment', 'title', 'category', 'un_estoque', 'tipo_embalagem', 'codigo', 'novo_codigo',
                    'data_validade', 'quantidade_un_embalagem', 'quantidade_embalagem_un_armazenamento',
                    'price', 'planta', 'slug', 'seg_name', 'type_prod', 'prod_level')

    list_filter = ('category', 'data_validade', 'planta', 'un_estoque')
    search_fields = ('title', 'codigo')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'un_estoque', 'tipo_embalagem', 'price')
        }),
        ('Informações adicionais', {
            'fields': ('planta', 'codigo', 'novo_codigo', 'data_validade',
                       'quantidade_un_embalagem', 'quantidade_embalagem_un_armazenamento',
                       'codigo_predecessor')
        }),
        ('Segmento', {
            'fields': ('segment', 'seg_name', 'type_production', 'nivel_produto', 'possible_segment')
        }),
    )

    # Métodos customizados para exibir os campos do Segmento
    def seg_name(self, obj):
        return obj.segment.segmentation if obj.segment and obj.segment.segmentation else None
    seg_name.admin_order_field = 'segment__segmentation'

    def type_prod(self, obj):
        return obj.segment.type_prod if obj.segment and obj.segment.type_prod else None
    type_prod.admin_order_field = 'segment__type_prod'

    def prod_level(self, obj):
        return obj.segment.prod_level if obj.segment and obj.segment.prod_level else None
    prod_level.admin_order_field = 'segment__prod_level'


    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        if obj and obj.segment:
            segment_fields = []

            # Coletar os campos dinâmicos baseados nas propriedades do Segmento
            for field in obj.segment._meta.fields:
                field_name = field.name
                if hasattr(obj.segment, field_name):  # Verificar se o campo existe
                    # Usar o valor de cada campo de forma dinâmica
                    field_value = getattr(obj.segment, field_name)
                    if field_name == 'segmentation':
                        obj.seg_name = field_value
                    # elif field_name == 'type_prod':
                    #     obj.type_prod = field_value
                    # elif field_name == 'prod_level':
                    #     obj.prod_level = field_value
                    elif field_name == 'possible_segment':
                        obj.possible_segment = field_value

                    # Adicionar os campos ao fieldset
                    segment_fields.append(field_name)

            # Adicionar o fieldset de Segmento se existirem campos dinâmicos
            if segment_fields:
                segment_fieldset = ('Segmento', {'fields': segment_fields})
                fieldsets = list(fieldsets)  # Tornar o fieldsets mutável
                fieldsets.append(segment_fieldset)

        return fieldsets


    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        obj.save()
