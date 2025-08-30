# backend/tests/db/test_producto.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.db.models.producto import Producto

# Crear una base SQLite en memoria
engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(bind=engine)

def test_producto_model():
    # Crear las tablas
    Base.metadata.create_all(bind=engine)

    # Crear una sesión
    db = TestingSessionLocal()

    # Crear un producto
    producto = Producto(
        nombre="Café en grano",
        sku="CAF123",
        stock=100,
        stock_minimo=20
    )

    # Agregar y confirmar
    db.add(producto)
    db.commit()

    # Recuperar y verificar
    result = db.query(Producto).filter_by(sku="CAF123").first()
    assert result is not None
    assert result.nombre == "Café en grano"
    assert result.stock == 100
    assert result.stock_minimo == 20