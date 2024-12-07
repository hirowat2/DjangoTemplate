from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date
from ninja import Schema
from pydantic import Field
from typing import Optional

# Schemas para as chaves estrangeiras
class CategorySchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

class UnEstoqueSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

class TipoEmbalagemSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

class SegmentationSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

# Schema para o produto
class ProductSchema(Schema):
    id: int
    codigo: str
    planta: str
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[int] = None  # Ou use o esquema de categoria, se necessário
    un_estoque: Optional[int] = None  # Id do estoque
    tipo_embalagem: Optional[int] = None  # Id do tipo de embalagem
    segmentation: Optional[str] = None  # Ajuste conforme seu modelo
    novo_codigo: Optional[str] = None
    data_validade: Optional[str] = None  # Ajuste conforme seu modelo
    quantidade_un_embalagem: Optional[int] = None
    quantidade_embalagem_un_armazenamento: Optional[int] = None
    codigo_predecessor: Optional[str] = None
    # custo_unitario: Optional[float] = None

# class ProductSchema(BaseModel):
#     id: int
#     title: str
#     description: Optional[str]
#     price: Optional[Decimal]
#     category: Optional[CategorySchema]
#     un_estoque: Optional[UnEstoqueSchema]
#     tipo_embalagem: Optional[TipoEmbalagemSchema]
#     segmentation: Optional[SegmentationSchema]
#     planta: Optional[str]
#     codigo: str
#     novo_codigo: Optional[str]
#     data_validade: Optional[date]
#     quantidade_un_embalagem: Optional[int]
#     quantidade_embalagem_un_armazenamento: Optional[int]
#     codigo_predecessor: Optional[str]
#     custo_unitario: Optional[Decimal]

#     class Config:
#         orm_mode = True
