from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Formula

@receiver(pre_save, sender=Formula)
def formula_pre_save(sender, instance, **kwargs):
    # Lógica do sinal
    print(f"Antes de salvar a fórmula: {instance}")
