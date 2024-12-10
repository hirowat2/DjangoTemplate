from django.urls import path
from . import views

app_name = 'formula'

urlpatterns = [
    path('formula/<int:formula_id>/<int:data_set_id>/', views.formula, name='formula'),
]
