# product/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

from .models import Category, Photo, Product, UnEstoque, tipo_embalagem, segmentation


@admin.register(UnEstoque)
class un_estoqueAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)

@admin.register(tipo_embalagem)
class tipo_embalagemAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)

@admin.register(segmentation)
class segmentationAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        import_id_fields = ['codigo']  # Substitua por um campo válido
        exclude = ('id',)  # Caso queira ignorar o campo 'id'


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [ProductResource]
    inlines = (PhotoInline,)
    # list_display = ('__str__', 'slug', 'category', 'price', 'stock', 'created', 'modified')
    readonly_fields = ('slug',)
    # search_fields = ('title',)
    # list_filter = ('category',)
    # date_hierarchy = 'created'
    list_display = (
        'title', 'category', 'un_estoque', 'tipo_embalagem','codigo', 'novo_codigo', 'data_validade',
        'quantidade_un_embalagem', 'quantidade_embalagem_un_armazenamento',
        'codigo_predecessor', 'custo_unitario', 'planta', 'slug', 'segmentation'
    )
    list_filter = ('category', 'data_validade', 'planta', 'un_estoque', 'tipo_embalagem', 'segmentation')
    search_fields = ('title', 'codigo', 'novo_codigo', 'codigo_predecessor')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'category', 'un_estoque', 'tipo_embalagem', 'slug', 'segmentation')
        }),
        ('Informações adicionais', {
            'fields': ('planta', 'codigo', 'novo_codigo', 'data_validade',
                       'quantidade_un_embalagem', 'quantidade_embalagem_un_armazenamento',
                       'codigo_predecessor', 'custo_unitario')
        }),
    )

    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        obj.save()
