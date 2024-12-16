from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

from backend.product.api import router as product_router  # Ajuste o caminho

# Criação da instância da API
api = NinjaAPI()

api.add_router("/products/", product_router)

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),  # noqa E501
    path('accounts/', include('backend.accounts.urls')),  # noqa E501
    path('bookstore/', include('backend.bookstore.urls', namespace='bookstore')),  # noqa E501
    path('crm/', include('backend.crm.urls', namespace='crm')),  # noqa E501
    path('expense/', include('backend.expense.urls', namespace='expense')),  # noqa E501
    path('product/', include('backend.product.urls', namespace='product')),  # noqa E501
    path('consume/', include('backend.consume.urls', namespace='consume')),  # noqa E501
    # path('vehicle/', include('backend.vehicle.urls', namespace='vehicle')),  # noqa E501
    # path('kitchensink/', include('backend.kitchensink.urls', namespace='kitchensink')),  # noqa E501
    # path('dashboards/', include('backend.dashboards.urls', namespace='dashboards')),  # noqa E501
    path('dash/', include('backend.dash.urls', namespace='dash')),  # noqa E501
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    # path('dashboards/', include('dashboards.urls')),
    # path('dash/', include('backend.dash.urls', namespace='dash')),  # noqa E501
    path('prateleira/', include('backend.prateleira.urls', namespace='prateleira')),  # noqa E501
    path('reposition/', include('backend.reposition.urls', namespace='reposition')),  # noqa E501
    path('segment/', include('backend.segment.urls', namespace='segment')),  # noqa E501
    path('todo/', include('backend.todo.urls', namespace='todo')),  # noqa E501
    path("api/", api.urls),  # noqa E501
    path('admin/', admin.site.urls),  # noqa E501
]
