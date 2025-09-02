from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.domain.models.producto import Producto
from app.repositories.producto_repository import ProductoRepository

def test_producto_repository_add_and_get():
    # Setup: motor en memoria y sesión
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    # Repositorio
    repo = ProductoRepository(session)

    # Producto de dominio
    producto = Producto(
        id=1,
        nombre="Café",
        sku="CAF123",
        stock=10,
        precio=1200.0,
        descripcion="Café en grano premium"
    )

    # Acción: agregar y recuperar
    repo.add(producto)
    productos = repo.get_all()

    # Validación
    assert len(productos) == 1
    assert productos[0].nombre == "Café"
    assert productos[0].sku == "CAF123"
    assert productos[0].precio == 1200.0