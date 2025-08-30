from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base  


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    stock = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)

   # movimientos = relationship("Movimiento", back_populates="producto")