from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class ProductoORM(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    sku = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)
    descripcion = Column(String, nullable=True)