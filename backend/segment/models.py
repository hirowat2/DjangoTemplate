from django.db import models
from django.urls import reverse_lazy
from backend.core.models import TimeStampedModel
from django.utils.text import slugify

class ProdLevel(models.Model):
    title = models.CharField('título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'prod_level'
        verbose_name_plural = 'prod_level'

    def __str__(self):
        return f'{self.title}'
class TypeProduction(models.Model):
    title = models.CharField('título', max_length=255, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'type_prod'
        verbose_name_plural = 'type_prod'

    def __str__(self):
        return f'{self.title}'

class Segment(TimeStampedModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    prod_level = models.ForeignKey(
        'ProdLevel',
        on_delete=models.CASCADE,
        verbose_name='Nível do produto',
        related_name='segment',
        null=True,
        blank=True,
    )

    type_prod = models.ForeignKey(
        'TypeProduction',
        on_delete=models.CASCADE,
        verbose_name='Tipo do Produto',
        related_name='segment',
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=100)
    description = models.TextField('descrição', null=True, blank=True)

    possible_segment = models.CharField(max_length=100)

    slug = models.SlugField('slug de segment', null=True, blank=True)

    class Meta:
        verbose_name = 'segment'
        verbose_name_plural = 'segments'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('segment:segment_detail', kwargs={'pk': self.pk})

    def list_url(self):
        return reverse_lazy('segment:segment_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural

# class PreSegment(TimeStampedModel):


#     prod_level = models.ForeignKey(
#         'ProdLevel',
#         on_delete=models.CASCADE,
#         verbose_name='Nível do produto',
#         related_name='products',
#         null=True,
#         blank=True,
#     )

#     type_prod = models.ForeignKey(
#         'TypeProduction',
#         on_delete=models.CASCADE,
#         verbose_name='Tipo do Produto',
#         related_name='products',
#         null=True,
#         blank=True,
#     )

#     title = models.CharField(max_length=100)
#     description = models.TextField('descrição', null=True, blank=True)

# class Segment(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     segment = models.ForeignKey(PreSegment, related_name='possible_segments', on_delete=models.CASCADE)
#     value = models.CharField('Possible Segment Value', max_length=100)
#     slug = models.SlugField('slug de segment', null=True, blank=True)

#     class Meta:
#         verbose_name = 'segment'
#         verbose_name_plural = 'segments'

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse_lazy('segment:segment_detail', kwargs={'pk': self.pk})

#     def list_url(self):
#         return reverse_lazy('segment:segment_list')

#     @property
#     def verbose_name(self):
#         return self._meta.verbose_name

#     @property
#     def verbose_name_plural(self):
#         return self._meta.verbose_name_plural

#     def __str__(self):
#         return self.value