# segment/urls.py
from django.urls import include, path

from backend.segment import views as v

app_name = 'segment'

# A ordem das urls é importante por causa do slug, quando existir.
segment_patterns = [
    # path('', v.segmentListView.as_view(), name='segment_list'),  # noqa E501
    path('', v.segment_list, name='segment_list'),  # noqa E501
    path('create/', v.segment_create, name='segment_create'),  # noqa E501
    path('<int:pk>/', v.segment_detail, name='segment_detail'),  # noqa E501
    path('<int:pk>/update/', v.segment_update, name='segment_update'),  # noqa E501
    path('<int:pk>/delete/', v.segment_delete, name='segment_delete'),  # noqa E501
    path('import/', v.import_view, name='import_view'),  # noqa E501
    path('export/csv/', v.export_csv, name='export_csv'),  # noqa E501
    path('export/xlsx/', v.export_xlsx, name='export_xlsx'),  # noqa E501
]

urlpatterns = [
    path('', include(segment_patterns)),
]
