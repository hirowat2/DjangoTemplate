from django.apps import AppConfig


class FormulaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.formula'

    def ready(self):
        from django.db.models.signals import pre_save

        from .models import Formula
        from .signals import formula_pre_save

        pre_save.connect(formula_pre_save, sender=Formula)
