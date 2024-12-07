from django.db import models
from django.urls import reverse_lazy
from backend.core.models import TimeStampedModel
from backend.product.models import Product  # Ajuste o caminho para o modelo Product

class Consume(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='consumos',
        # null=True,
        # blank=False,
        # related_name='consumos',  # Acesso inverso no produto
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    consumo_historico = models.FloatField('consumo histórico', null=True, blank=True)
    cv_diario = models.FloatField('cv diário', null=True, blank=True)
    cv_periodo_lt = models.FloatField('cv período lt', null=True, blank=True)
    demanda_dia_prev = models.FloatField('demanda dia prev', null=True, blank=True)
    fator_k = models.FloatField('fator k', null=True, blank=True)
    menor_lote_consumo = models.FloatField('menor lote consumo', null=True, blank=True)
    slug = models.SlugField('slug de consumo', null=True, blank=True)


    class Meta:
        ordering = ('product',)
        # ordering = ('product__title',)
        verbose_name = 'consumo'
        verbose_name_plural = 'consumos'

    def __str__(self):
        return f'{self.product.codigo}'

    def get_absolute_url(self):
        return reverse_lazy('consume:consume_detail', kwargs={'pk': self.pk})

    def list_url(self):
        return reverse_lazy('consume:consume_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural