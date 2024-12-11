from django.shortcuts import render
from django.apps import apps

def dynamic_model_view(request, model_name):
    Model = apps.get_model('myapp', model_name)
    data = Model.objects.all()
    return render(request, 'dynamic_model_view.html', {'data': data})
