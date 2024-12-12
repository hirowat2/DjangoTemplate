from django.db.models.signals import pre_save
from django.dispatch import receiver
from backend.prateleira.models import Prateleira
from django.utils.text import slugify

@receiver(pre_save, sender=Prateleira)
def prateleira_pre_save(sender, instance, **kwargs):
    if instance.product:
        instance.slug = slugify(instance.product.codigo)
    else:
        # Caso não tenha um produto associado, defina o slug como algo padrão
        instance.slug = slugify(instance.pk)