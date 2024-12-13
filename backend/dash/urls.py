# dahs/urls.py
from django.urls import include, path

from backend.dash import views as v

app_name = 'dash'

# A ordem das urls é importante por causa do slug, quando existir.
dash_patterns = [
    path('home/', v.home, name='home'),  # noqa E501
]

urlpatterns = [
    path('', include(dash_patterns)),
]
