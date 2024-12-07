from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date

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
class ProductSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: Optional[Decimal]
    category: Optional[CategorySchema]
    un_estoque: Optional[UnEstoqueSchema]
    tipo_embalagem: Optional[TipoEmbalagemSchema]
    segmentation: Optional[SegmentationSchema]
    planta: Optional[str]
    codigo: str
    novo_codigo: Optional[str]
    data_validade: Optional[date]
    quantidade_un_embalagem: Optional[int]
    quantidade_embalagem_un_armazenamento: Optional[int]
    codigo_predecessor: Optional[str]
    custo_unitario: Optional[Decimal]

    class Config:
        orm_mode = True
