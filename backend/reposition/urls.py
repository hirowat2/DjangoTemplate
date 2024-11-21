# Reposition/urls.py
from django.urls import include, path

from backend.reposition import views as v

app_name = 'reposition'

# A ordem das urls é importante por causa do slug, quando existir.
reposition_patterns = [
    # path('', v.repositionListView.as_view(), name='reposition_list'),  # noqa E501
    path('', v.reposition_list, name='reposition_list'),  # noqa E501
    path('create/', v.reposition_create, name='reposition_create'),  # noqa E501
    path('<int:pk>/', v.reposition_detail, name='reposition_detail'),  # noqa E501
    path('<int:pk>/update/', v.reposition_update, name='reposition_update'),  # noqa E501
    path('<int:pk>/delete/', v.reposition_delete, name='reposition_delete'),  # noqa E501
    path('import/', v.import_view, name='import_view'),  # noqa E501
    path('export/csv/', v.export_csv, name='export_csv'),  # noqa E501
    path('export/xlsx/', v.export_xlsx, name='export_xlsx'),  # noqa E501
]

urlpatterns = [
    path('', include(reposition_patterns)),
]
