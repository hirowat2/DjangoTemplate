from django.db import models
from django.urls import reverse_lazy
from backend.core.models import TimeStampedModel
from backend.segment.models import Segment, TypeProduction, ProdLevel  # Assumindo que o Segment está no app "segment"
from django.utils.text import slugify
from django.db.models import JSONField
class Category(models.Model):
    title = models.CharField('título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return f'{self.title}'
class UnEstoque(models.Model):
    title = models.CharField('Título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Un Estoque'
        verbose_name_plural = 'Un Estoques'

    def __str__(self):
        return self.title


class TipoEmbalagem(models.Model):
    title = models.CharField('Título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Tipo de Embalagem'
        verbose_name_plural = 'Tipos de Embalagem'

    def __str__(self):
        return self.title


class Product(TimeStampedModel):
    # Relacionamentos
    un_estoque = models.ForeignKey(UnEstoque, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    tipo_embalagem = models.ForeignKey(TipoEmbalagem, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    segment = models.OneToOneField(Segment, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)


    # Campos adicionais
    slug = models.SlugField()
    codigo = models.CharField(max_length=100)
    novo_codigo = models.CharField(max_length=100)
    data_validade = models.DateField()
    planta = models.CharField('planta', max_length=100, null=True, blank=True)
    quantidade_un_embalagem = models.PositiveIntegerField('Qtd und na embalagem', null=True, blank=True)
    und_armazen = models.CharField('Und Armazen', max_length=100, null=True, blank=True)
    quantidade_embalagem_un_armazenamento = models.PositiveIntegerField('Qtd emb um Armaz', null=True, blank=True)
    codigo_predecessor = models.CharField('Código do Predecessor', max_length=100, null=True, blank=True)


    # Campos obrigatórios do produto
    title = models.CharField('Título', max_length=255, unique=True)
    description = models.TextField('Descrição', null=True, blank=True)
    price = models.DecimalField('Custo Unitário', max_digits=9, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='categoria',
        related_name='products',
        null=True,
        blank=True,
    )

    # Campos dinâmicos como JSON para armazenar as propriedades do Segment
    seg_name = models.CharField('Título', max_length=255, null=True, blank=True)
    type_production =  models.OneToOneField(TypeProduction, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    nivel_produto = models.OneToOneField(ProdLevel, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    possible_segment = models.CharField('Título', max_length=255, null=True, blank=True)


    class Meta:
        ordering = ('title',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.title} - {self.segment.title if self.segment else "No Segment"}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Populate dynamic properties field based on the related Segment
        if self.segment:
            self.seg_name = self.segment.title
            # self.type_prod = self.segment.type_prod
            # self.prod_level = self.segment.prod_level
            self.possible_segment = self.segment.possible_segment
            # self.seg_name = {field.name: getattr(self.segment, field.name) for field in self.segment._meta.fields}
            # self.type_prod = {field.name: getattr(self.segment, field.name) for field in self.segment._meta.fields if hasattr(self.segment, 'type_prod')}
            # self.prod_level = {field.name: getattr(self.segment, field.name) for field in self.segment._meta.fields if hasattr(self.segment, 'prod_level')}
            # self.possible_segment = {field.name: getattr(self.segment, field.name) for field in self.segment._meta.fields if hasattr(self.segment, 'possible_segment')}

        super().save(*args, **kwargs)


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
    photo = models.ImageField(upload_to='products/photos/')  # Specify directory for photos
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return f'{self.pk}'
