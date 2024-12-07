# from django.utils.text import slugify


# def consume_pre_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title)

from django.db.models.signals import pre_save
from django.dispatch import receiver
from backend.consume.models import Consume
from django.utils.text import slugify

@receiver(pre_save, sender=Consume)
def consume_pre_save(sender, instance, **kwargs):
    # Usando o código do produto para gerar o slug
    if instance.product:
        instance.slug = slugify(instance.product.codigo)
    else:
        # Caso não tenha um produto associado, defina o slug como algo padrão
        instance.slug = slugify(instance.pk)  # Ou outro valor que faça sentido
