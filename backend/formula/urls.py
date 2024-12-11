from django.urls import path
from . import views

app_name = 'formula'  # Certifique-se de definir o app_name aqui


urlpatterns = [
    path('dynamic-model/', views.dynamic_model_view, name='dynamic_model_view'),
]
