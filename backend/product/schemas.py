from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date
from ninja import Schema
from pydantic import Field
from typing import Optional

class ForeignKeySchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

CategorySchema = ForeignKeySchema
UnEstoqueSchema = ForeignKeySchema
# TipoEmbalagemSchema = ForeignKeySchema
# SegmentationSchema = ForeignKeySchema
# TypeProductionSchema = ForeignKeySchema
# NivelProdutoSchema = ForeignKeySchema


# Schema para o produto
class ProductSchema(Schema):
    id: int
    codigo: str
    planta: str
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[CategorySchema] = None
    un_estoque: Optional[UnEstoqueSchema] = None
    # tipo_embalagem: Optional[TipoEmbalagemSchema] = None
    # segmentation: Optional[SegmentationSchema] = None
    # type_production: Optional[TypeProductionSchema] = None
    # nivel_produto: Optional[NivelProdutoSchema] = None
    novo_codigo: Optional[str] = None
    data_validade: Optional[str] = None
    quantidade_un_embalagem: Optional[int] = None
    quantidade_embalagem_un_armazenamento: Optional[int] = None
    codigo_predecessor: Optional[str] = None
