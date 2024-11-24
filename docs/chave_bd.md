---
id: doc1
título: Conceito de banco de dados no django
sidebar_label: Índice
---

# Conceito de banco de dados no django

- [Conceito de banco de dados no django](#conceito-de-banco-de-dados-no-django)
  - [Exemplo para o modelo Product](#exemplo-para-o-modelo-product)
  - [Impactos de alterar a chave primária](#impactos-de-alterar-a-chave-primária)
  - [Abordagem 1: Herança de Modelos](#abordagem-1-herança-de-modelos)
    - [Exemplo:](#exemplo)
  - [Abordagem 2: Relacionamentos com OneToOneField](#abordagem-2-relacionamentos-com-onetoonefield)
  - [Abordagem 3: Adicionar campos diretamente ao modelo Product](#abordagem-3-adicionar-campos-diretamente-ao-modelo-product)






Para definir uma chave primária para as tabelas no banco de dados, o Django, por padrão, já cria um campo id como chave primária em cada modelo. No entanto, caso você deseje usar um campo diferente como chave primária, você pode definir explicitamente o atributo primary_key=True no campo correspondente.

## Exemplo para o modelo Product

Se você deseja que o campo codigo seja a chave primária do modelo Product, modifique a definição do campo da seguinte forma:

```python
codigo = models.CharField(
    'código', max_length=50, unique=True, primary_key=True, default='default_codigo'
)
```

Isso transforma o campo codigo na chave primária, e o Django não criará automaticamente o campo id para esse modelo.

## Impactos de alterar a chave primária

Relacionamentos: Qualquer relacionamento com o modelo que use a chave primária precisará referenciar o novo campo.
Integridade dos dados: Certifique-se de que o valor definido como chave primária seja único e não nulo.
Migrações: Alterar a chave primária de um modelo existente pode ser complicado em bancos de dados já em uso. Certifique-se de criar uma migração apropriada e testar cuidadosamente.
Se você deseja manter o campo id como chave primária, mas garantir a unicidade de codigo, você já está utilizando unique=True, o que é suficiente para esse propósito.


## Abordagem 1: Herança de Modelos

Essa abordagem cria tabelas separadas nos aplicativos `consume` e `reposition`, mas elas compartilham a mesma chave primária do modelo `Product`. Isso é útil quando as informações adicionais são extensões claras de `Product`.

### Exemplo:

```python
# consume/models.py
from backend.models import Product

class ProductConsumption(Product):
    consumption_rate = models.DecimalField(
        'Taxa de Consumo', max_digits=10, decimal_places=2, null=True, blank=True
    )
    consumed_by = models.CharField('Consumido por', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'product_consumption'
        verbose_name = 'Consumo do Produto'
        verbose_name_plural = 'Consumos de Produtos'

# reposition/models.py
from backend.models import Product

class ProductReposition(Product):
    stock_level = models.PositiveIntegerField('Nível de Estoque', null=True, blank=True)
    reorder_point = models.PositiveIntegerField('Ponto de Reposição', null=True, blank=True)

    class Meta:
        db_table = 'product_reposition'
        verbose_name = 'Reposição do Produto'
        verbose_name_plural = 'Reposições de Produtos'

```

## Abordagem 2: Relacionamentos com OneToOneField

Se as informações adicionais são claramente separadas, use o campo OneToOneField para criar uma extensão lógica do modelo Product. Isso mantém uma tabela para o modelo Product e armazena informações extras em tabelas relacionadas.


```python
# consume/models.py
from backend.models import Product

class ProductConsumption(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='consumption',
        verbose_name='Produto'
    )
    consumption_rate = models.DecimalField(
        'Taxa de Consumo', max_digits=10, decimal_places=2, null=True, blank=True
    )
    consumed_by = models.CharField('Consumido por', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'product_consumption'
        verbose_name = 'Consumo do Produto'
        verbose_name_plural = 'Consumos de Produtos'

# reposition/models.py
from backend.models import Product

class ProductReposition(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='reposition',
        verbose_name='Produto'
    )
    stock_level = models.PositiveIntegerField('Nível de Estoque', null=True, blank=True)
    reorder_point = models.PositiveIntegerField('Ponto de Reposição', null=True, blank=True)

    class Meta:
        db_table = 'product_reposition'
        verbose_name = 'Reposição do Produto'
        verbose_name_plural = 'Reposições de Produtos'

```

Acesso aos dados



```python
# Obter informações de consumo de um produto
product = Product.objects.get(id=1)
consumption = product.consumption  # Objeto relacionado
print(consumption.consumption_rate)

# Obter informações de reposição de um produto
reposition = product.reposition
print(reposition.stock_level)
```

## Abordagem 3: Adicionar campos diretamente ao modelo Product

Se as informações adicionais são sempre aplicáveis a todos os produtos, considere adicionar os campos diretamente ao modelo Product. Isso evita a criação de tabelas extras e mantém tudo no mesmo lugar.


```python
class Product(TimeStampedModel):
    # Campos existentes
    title = models.CharField('título', max_length=255, unique=True)
    description = models.TextField('descrição', null=True, blank=True)

    # Novos campos para consumo e reposição
    consumption_rate = models.DecimalField(
        'Taxa de Consumo', max_digits=10, decimal_places=2, null=True, blank=True
    )
    consumed_by = models.CharField('Consumido por', max_length=255, null=True, blank=True)
    stock_level = models.PositiveIntegerField('Nível de Estoque', null=True, blank=True)
    reorder_point = models.PositiveIntegerField('Ponto de Reposição', null=True, blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

```

