from rest_framework import serializers
from .models import Product, Category, UnEstoque

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class UnEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnEstoque
        fields = ['id', 'title']

# class TipoEmbalagemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = tipo_embalagem
#         fields = ['id', 'title']

# class SegmentationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = segmentation
#         fields = ['id', 'title']

# class TypeProductionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = type_production
#         fields = ['id', 'title']

# class NivelProdutoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = nivel_produto
#         fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    un_estoque = UnEstoqueSerializer(read_only=True)
    # tipo_embalagem = TipoEmbalagemSerializer(read_only=True)
    # segmentation = SegmentationSerializer(read_only=True)
    # type_production = TypeProductionSerializer(read_only=True)
    # nivel_produto = NivelProdutoSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        # fields = [
        #     'id', 'title', 'description', 'price', 'category', 'un_estoque', 'tipo_embalagem',
        #     'segmentation', 'type_production', 'nivel_produto', 'slug', 'planta', 'codigo', 'novo_codigo', 'data_validade',
        #     'quantidade_un_embalagem', 'quantidade_embalagem_un_armazenamento',
        #     'codigo_predecessor', 'custo_unitario'
        # ]

