# product/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin
from django.forms import Textarea
from .models import Segment, ProdLevel, TypeProduction

@admin.register(ProdLevel)
class ProdLevelAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)


@admin.register(TypeProduction)
class TypeProductionAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)


class SegmentResource(resources.ModelResource):

    class Meta:
        model = Segment
        exclude = ('id',)  # Caso queira ignorar o campo 'id'


@admin.register(Segment)
class SegmentAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = [SegmentResource]
    list_display = ('title', 'prod_level', 'type_prod', 'possible_segment', 'created', 'modified')
    search_fields = ('title', 'description', 'possible_segment')
    list_filter = ('prod_level', 'type_prod', 'possible_segment', 'created', 'modified')
    fields = ('title', 'description', 'prod_level', 'type_prod', 'possible_segment', 'slug')
    prepopulated_fields = {'slug': ('title',)}  # Automatiza a criação do slug

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Exemplo: adiciona ajuda ao campo possible_segment
        form.base_fields['possible_segment'].help_text = (
            "Insira os valores separados por vírgula (Exemplo: Cápsula, Comprimido, Suspensão)"
        )
        return form
    # readonly_fields = ('slug',)
    # list_display = (
    #     'id',
    #     'title',
    #     'description',
    #     'possible_segment',
    #     'prod_level',
    #     'type_prod',
    #     'created',
    #     'modified',
    # )
    # list_filter = ('prod_level', 'type_prod', 'created', 'modified')
    # search_fields = ('title', 'description', 'possible_segment')
    # ordering = ('-created',)
    # # prepopulated_fields = {'slug': ('title',)}
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'description', 'possible_segment', 'prod_level',
    #                    'type_prod', 'slug')
    #     }),

    # )

# @admin.register(Segment)
# class SegmentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'prod_level', 'type_prod', 'created', 'modified')
#     search_fields = ('title', 'description', 'possible_segment')
#     list_filter = ('prod_level', 'type_prod', 'created', 'modified')
#     fields = ('title', 'description', 'prod_level', 'type_prod', 'possible_segment', 'slug')
#     prepopulated_fields = {'slug': ('title',)}  # Automatiza a criação do slug

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         # Exemplo: adiciona ajuda ao campo possible_segment
#         form.base_fields['possible_segment'].help_text = (
#             "Insira os valores separados por vírgula (Exemplo: Cápsula, Comprimido, Suspensão)"
#         )
#         return form
    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        obj.save()
