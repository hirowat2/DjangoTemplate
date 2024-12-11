from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Segment
from django.utils.text import slugify

@receiver(pre_save, sender=Segment)
def segment_pre_save(sender, instance, **kwargs):
    # Verifique se 'segment_title' tem valor
    if instance.possible_segment:
        instance.slug = slugify(instance.possible_segment)
    else:
        # Caso não tenha, gere o slug a partir do pk
        instance.slug = slugify(instance.pk)
