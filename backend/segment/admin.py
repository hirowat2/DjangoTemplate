# product/admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

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
    # readonly_fields = ('slug',)
    list_display = (
        'id',
        'title',
        'description',
        'possible_segment',
        'prod_level',
        'type_prod',
        'created',
        'modified',
    )
    list_filter = ('prod_level', 'type_prod', 'created', 'modified')
    search_fields = ('title', 'description', 'possible_segment')
    ordering = ('-created',)
    # prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'possible_segment', 'prod_level',
                       'type_prod', 'slug')
        }),

    )

    # Personalizando como os campos são exibidos no formulário de edição
    def save_model(self, request, obj, form, change):
        obj.save()
