from django.test import TestCase
from .models import Formula, DataSet
from .utils import evaluate_formula

class FormulaEvaluationTest(TestCase):
    def setUp(self):
        self.formula = Formula.objects.create(name="Soma", expression="a + b + c")
        self.data_set = DataSet.objects.create(name="Exemplo", a=10, b=5, c=2)

    def test_evaluate_formula(self):
        result = evaluate_formula(self.formula, self.data_set)
        self.assertEqual(result, 17)  # 10 + 5 + 2 = 17
