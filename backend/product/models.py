from django.db import models
from django.urls import reverse_lazy
from backend.core.models import TimeStampedModel

class Category(models.Model):
    title = models.CharField('título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return f'{self.title}'

class UnEstoque(models.Model):
    title = models.CharField('título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'un_estoque'
        verbose_name_plural = 'un_estoque'

    def __str__(self):
        return f'{self.title}'


class tipo_embalagem(models.Model):
    title = models.CharField('título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'tipo_embalagem'
        verbose_name_plural = 'tipo_embalagem'

    def __str__(self):
        return f'{self.title}'

class Product(TimeStampedModel):
    title = models.CharField('título', max_length=255, unique=True)
    description = models.TextField('descrição', null=True, blank=True)
    price = models.DecimalField('preço', max_digits=9, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='categoria',
        related_name='products',
        null=True,
        blank=True,
    )
    un_estoque = models.ForeignKey(
        'UnEstoque',
        on_delete=models.CASCADE,
        verbose_name='un_estoque',
        related_name='products',
        null=True,
        blank=True,
    )
    tipo_embalagem = models.ForeignKey(
        'tipo_embalagem',
        on_delete=models.SET_NULL,
        verbose_name='tipo_embalagem',
        related_name='products',
        null=True,
        blank=True,
    )
    slug = models.SlugField(null=True, blank=True)

    # Novos campos adicionados
    planta = models.CharField('planta', max_length=100, null=True, blank=True)
    codigo = models.CharField('código', max_length=50, unique=True, default='default_codigo')
    novo_codigo = models.CharField('novo código', max_length=50, null=True, blank=True)
    data_validade = models.DateField('data de validade', null=True, blank=True)
    quantidade_un_embalagem = models.PositiveIntegerField('quantidade un embalagem', null=True, blank=True)
    quantidade_embalagem_un_armazenamento = models.PositiveIntegerField('quantidade embalagem un armazenamento', null=True, blank=True)
    codigo_predecessor = models.CharField('código predecessor', max_length=50, null=True, blank=True)
    custo_unitario = models.DecimalField('custo unitário', max_digits=9, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('product:product_detail', kwargs={'pk': self.pk})

    def list_url(self):
        return reverse_lazy('product:product_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural


class Photo(TimeStampedModel):
    photo = models.ImageField(upload_to='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return f'{self.pk}'
