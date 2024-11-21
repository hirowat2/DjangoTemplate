from django.db import models
from django.urls import reverse_lazy
from backend.core.models import TimeStampedModel


class Consume(TimeStampedModel):
    # title = models.CharField('título', max_length=255, unique=True)
    planta = models.CharField('planta', max_length=100, null=True, blank=True)
    codigo = models.CharField('código', max_length=50, unique=True, default='default_codigo')
    description = models.TextField('descrição', null=True, blank=True)
    consumo_historico = models.FloatField('consumo histórico', null=True, blank=True)
    cv_diario = models.FloatField('cv diário', null=True, blank=True)
    cv_periodo_lt = models.FloatField('cv período lt', null=True, blank=True)
    demanda_dia_prev = models.FloatField('demanda dia prev', null=True, blank=True)
    fator_k = models.FloatField('fator k', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ('planta',)
        verbose_name = 'consumo'
        verbose_name_plural = 'consumos'

    def __str__(self):
        return f'{self.planta}'

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

