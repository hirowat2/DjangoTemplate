from rest_framework import serializers
from .models import Product, Category, UnEstoque, tipo_embalagem, segmentation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class UnEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnEstoque
        fields = ['id', 'title']

class TipoEmbalagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_embalagem
        fields = ['id', 'title']

class SegmentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = segmentation
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    un_estoque = UnEstoqueSerializer(read_only=True)
    tipo_embalagem = TipoEmbalagemSerializer(read_only=True)
    segmentation = SegmentationSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'price', 'category', 'un_estoque', 'tipo_embalagem',
            'segmentation', 'slug', 'planta', 'codigo', 'novo_codigo', 'data_validade',
            'quantidade_un_embalagem', 'quantidade_embalagem_un_armazenamento',
            'codigo_predecessor', 'custo_unitario'
        ]

