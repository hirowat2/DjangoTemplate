from django.apps import AppConfig


class ConsumeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.consume'

    def ready(self):
        from django.db.models.signals import pre_save

        from .models import Consume
        from .signals import consume_pre_save

        pre_save.connect(consume_pre_save, sender=Consume)
