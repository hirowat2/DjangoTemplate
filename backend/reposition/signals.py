from django.db.models.signals import pre_save
from django.dispatch import receiver
from backend.reposition.models import Reposition
from django.utils.text import slugify


@receiver(pre_save, sender=Reposition)
def reposition_pre_save(sender, instance, **kwargs):
    # Usando o código do produto para gerar o slug
    if instance.product:
        instance.slug = slugify(instance.product.codigo)
    else:
        # Caso não tenha um produto associado, defina o slug como algo padrão
        instance.slug = slugify(instance.pk)