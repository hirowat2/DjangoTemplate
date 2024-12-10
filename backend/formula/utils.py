from asteval import Interpreter

def evaluate_formula(formula, data):
    """
    Avalia a fórmula para o conjunto de dados fornecido.

    :param formula: Objeto Formula contendo a expressão.
    :param data: Objeto DataSet com os valores.
    :return: Resultado da avaliação da fórmula.
    """
    context = {
        'a': data.a,
        'b': data.b,
        'c': data.c,
    }
    try:
        result = eval(formula.expression, {}, context)
        return result
    except Exception as e:
        raise ValueError(f"Erro ao avaliar a fórmula: {e}")


def safe_evaluate_formula(formula, data):
    """
    Avalia a fórmula com segurança usando asteval.
    """
    context = {
        'a': data.a,
        'b': data.b,
        'c': data.c,
    }
    interpreter = Interpreter()
    try:
        return interpreter.eval(formula.expression, context)
    except Exception as e:
        raise ValueError(f"Erro ao avaliar a fórmula: {e}")
