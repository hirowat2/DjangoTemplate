from django.apps import AppConfig


class PrateleiraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.prateleira'

    def ready(self):
        from django.db.models.signals import pre_save

        from .models import Prateleira
        from .signals import prateleira_pre_save

        pre_save.connect(prateleira_pre_save, sender=Prateleira)
