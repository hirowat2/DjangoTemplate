from ninja import Router
from .models import Product
from .schemas import ProductSchema
from typing import List

router = Router()

# Listar todos os produtos
@router.get("/products", response=List[ProductSchema])
def list_products(request):
    products = Product.objects.all()
    return [
        ProductSchema(
            id=product.id,
            codigo=product.codigo,
            planta=product.planta,
            title=product.title,
            description=product.description,
            price=product.price,
            category=product.category.id if product.category else None,
            un_estoque=product.un_estoque.id if product.un_estoque else None,
            tipo_embalagem=product.tipo_embalagem.id if product.tipo_embalagem else None,
            segmentation=product.segmentation.value if hasattr(product.segmentation, 'value') else str(product.segmentation),
            novo_codigo=product.novo_codigo,
            data_validade=product.data_validade.isoformat() if product.data_validade else None,
            quantidade_un_embalagem=product.quantidade_un_embalagem,
            quantidade_embalagem_un_armazenamento=product.quantidade_embalagem_un_armazenamento,
            codigo_predecessor=product.codigo_predecessor,
            custo_unitario=product.custo_unitario,
        )
        for product in products
    ]
# def list_products(request):
#     products = Product.objects.select_related(
#         'category', 'un_estoque', 'tipo_embalagem', 'segmentation'
#     ).all()
#     return products

# Obter um produto pelo ID
@router.get("/products/{product_id}", response=ProductSchema)
def get_product(request, product_id: int):
    try:
        product = Product.objects.select_related(
            'category', 'un_estoque', 'tipo_embalagem', 'segmentation'
        ).get(pk=product_id)
        return product
    except Product.DoesNotExist:
        return {"error": "Product not found"}

# Criar um novo produto
@router.post("/products", response=ProductSchema)
def create_product(request, payload: ProductSchema):
    product = Product.objects.create(**payload.dict())
    return product

# Atualizar um produto existente
@router.put("/products/{product_id}", response=ProductSchema)
def update_product(request, product_id: int, payload: ProductSchema):
    try:
        product = Product.objects.get(pk=product_id)
        for attr, value in payload.dict().items():
            setattr(product, attr, value)
        product.save()
        return product
    except Product.DoesNotExist:
        return {"error": "Product not found"}

# Deletar um produto
@router.delete("/products/{product_id}")
def delete_product(request, product_id: int):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return {"success": "Product deleted"}
    except Product.DoesNotExist:
        return {"error": "Product not found"}

