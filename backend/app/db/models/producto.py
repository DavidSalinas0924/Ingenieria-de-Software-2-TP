from sqlalchemy import Column, Integer, String, Float, Text
from app.db.base import Base

class ProductoORM(Base):
    __tablename__ = "productos"
    __table_args__ = {"extend_existing": True}  # 👈 Evita conflictos si ya existe

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    stock = Column(Integer, default=0)
    precio = Column(Float, nullable=False)
    descripcion = Column(Text)