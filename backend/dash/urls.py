from django.urls import path
from . import views

app_name = 'dash'  # Definindo o app_name

urlpatterns = [
    path('dash/', views.dashboard_view, name='dash'),
]
