from django.db import models
from django.urls import reverse_lazy
from backend.core.models import TimeStampedModel
from backend.product.models import Product  # Ajuste o caminho para o modelo Product

class Reposition(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='repositions',
    )
    lt_pre_ordem = models.FloatField('lt pré ordem', null=True, blank=True)
    lt_ordem = models.FloatField('lt ordem', null=True, blank=True)
    lt_quarentena = models.FloatField('lt quarentena', null=True, blank=True)
    lt_total = models.FloatField('lt total', null=True, blank=True)
    cv_lead_time = models.FloatField('cv lead time', null=True, blank=True)
    lote_minimo_rep = models.FloatField('lote mínimo reposição', null=True, blank=True)
    lote_multiplo_rep = models.FloatField('lote múltiplo reposição', null=True, blank=True)
    intervalo_reposicao = models.FloatField('intervalo reposição', null=True, blank=True)
    campanha_ideal = models.FloatField('campanha ideal', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ('product__title',)
        verbose_name = 'reposição'
        verbose_name_plural = 'reposições'

    def __str__(self):
        return f"{self.codigo} - {self.planta}"

    def get_absolute_url(self):
        return reverse_lazy('reposition:reposition_detail', kwargs={'pk': self.pk})

    def list_url(self):
        return reverse_lazy('reposition:reposition_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural
