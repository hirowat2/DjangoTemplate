# consume/urls.py
from django.urls import include, path

from backend.consume import views as v

app_name = 'consume'

# A ordem das urls é importante por causa do slug, quando existir.
consume_patterns = [
    # path('', v.consumeListView.as_view(), name='consume_list'),  # noqa E501
    path('', v.consume_list, name='consume_list'),  # noqa E501
    path('create/', v.consume_create, name='consume_create'),  # noqa E501
    path('<int:pk>/', v.consume_detail, name='consume_detail'),  # noqa E501
    path('<int:pk>/update/', v.consume_update, name='consume_update'),  # noqa E501
    path('<int:pk>/delete/', v.consume_delete, name='consume_delete'),  # noqa E501
    path('import/', v.import_view, name='import_view'),  # noqa E501
    path('export/csv/', v.export_csv, name='export_csv'),  # noqa E501
    path('export/xlsx/', v.export_xlsx, name='export_xlsx'),  # noqa E501
]

urlpatterns = [
    path('', include(consume_patterns)),
]
