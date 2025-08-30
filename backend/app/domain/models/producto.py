# backend/app/domain/models/producto.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class Producto:
    id: Optional[int]
    nombre: str
    sku: str
    stock: int
    precio: float
    descripcion: Optional[str] = None