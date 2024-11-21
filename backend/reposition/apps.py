from django.apps import AppConfig


class RepositionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.reposition'

    def ready(self):
        from django.db.models.signals import pre_save

        from .models import Reposition
        from .signals import reposition_pre_save

        pre_save.connect(reposition_pre_save, sender=Reposition)
