# prateleira/urls.py
from django.urls import include, path

from backend.prateleira import views as v

app_name = 'prateleira'

# A ordem das urls é importante por causa do slug, quando existir.
prateleira_patterns = [
    # path('', v.prateleiraListView.as_view(), name='prateleira_list'),  # noqa E501
    path('', v.prateleira_list, name='prateleira_list'),  # noqa E501
    path('create/', v.prateleira_create, name='prateleira_create'),  # noqa E501
    path('<int:pk>/', v.prateleira_detail, name='prateleira_detail'),  # noqa E501
    path('<int:pk>/update/', v.prateleira_update, name='prateleira_update'),  # noqa E501
    path('<int:pk>/delete/', v.prateleira_delete, name='prateleira_delete'),  # noqa E501
    path('import/', v.import_view, name='import_view'),  # noqa E501
    path('export/csv/', v.export_csv, name='export_csv'),  # noqa E501
    path('export/xlsx/', v.export_xlsx, name='export_xlsx'),  # noqa E501
]

urlpatterns = [
    path('', include(prateleira_patterns)),
]
