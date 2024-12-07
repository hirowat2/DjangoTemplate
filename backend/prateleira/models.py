from django.db import models
from django.urls import reverse_lazy
from backend.core.models import TimeStampedModel
from backend.product.models import Product  # Ajuste o caminho para o modelo Product

class Prateleira(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,  # ou default configurado, se necessário
        blank=False,  # para garantir que seja obrigatório no formulário
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    formula_calculo = models.CharField('formula calculo', max_length=100, null=True, blank=True)
    reserva_historico = models.FloatField('reserva historico', null=True, blank=True)
    inicio_reserva = models.FloatField('inicio reserva', null=True, blank=True)
    fim_reserva = models.FloatField('fim reserva', null=True, blank=True)
    reserva = models.FloatField('reserva', null=True, blank=True)
    segurança = models.FloatField('segurança', null=True, blank=True)
    pulmao = models.FloatField('pulmão', null=True, blank=True)
    ciclo = models.SlugField('ciclo',null=True, blank=True)
    dep_maximo = models.FloatField('dep maximo',null=True, blank=True)
    dep_medio = models.FloatField('dep medio',null=True, blank=True)
    quarentena = models.FloatField('quarentena',null=True, blank=True)
    transito = models.FloatField('transito',null=True, blank=True)
    prateleira_total = models.FloatField('prateleira total',null=True, blank=True)
    pto_reposicao = models.FloatField('pto reposição',null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ('product__title',)
        verbose_name = 'prateleira'
        verbose_name_plural = 'prateleiras'

    def __str__(self):
      return f'{self.product.codigo} | {self.product.planta} | {self.product.title}'

    def get_absolute_url(self):
        return reverse_lazy('prateleira:prateleira_detail', kwargs={'pk': self.pk})

    def list_url(self):
        return reverse_lazy('prateleira:prateleira_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural
