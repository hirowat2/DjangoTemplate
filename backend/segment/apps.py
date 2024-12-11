from django.apps import AppConfig


class SegmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.segment'

    def ready(self):
        from django.db.models.signals import pre_save

        from .models import Segment
        from .signals import segment_pre_save

        pre_save.connect(segment_pre_save, sender=Segment)
