from django.shortcuts import render, get_object_or_404
from .models import Formula, DataSet
from .utils import evaluate_formula
from django.http import JsonResponse

def formula(request, formula_id, data_set_id):
    formula = get_object_or_404(Formula, id=formula_id)
    data_set = get_object_or_404(DataSet, id=data_set_id)
    result = evaluate_formula(formula, data_set)
    return render(request, 'formula/result.html', {'result': result})

# def formula(request, formula_id, data_set_id):
#     # Implementação lógica
#     return JsonResponse({'result': 'calculation success'})