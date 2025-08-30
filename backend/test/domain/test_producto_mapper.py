from app.domain.models.producto import Producto
from app.db.models.producto import ProductoORM
from app.domain.mappers.producto_mapper import producto_orm_to_domain, producto_domain_to_orm

def test_producto_orm_to_domain_normalization():
    orm = ProductoORM(
        id=1,
        nombre="  Café molido  ",
        sku="caf-123",
        stock=-5,
        precio=-100.0,
        descripcion="  Suave y aromático  "
    )
    domain = producto_orm_to_domain(orm)
    assert domain.nombre == "Café molido"
    assert domain.sku == "CAF-123"
    assert domain.stock == 0
    assert domain.precio == 0.0
    assert domain.descripcion == "Suave y aromático"

def test_producto_domain_to_orm_normalization():
    domain = Producto(
        id=None,
        nombre="  Té verde  ",
        sku="te-456",
        stock=-10,
        precio=-50.0,
        descripcion="  Orgánico  "
    )
    orm = producto_domain_to_orm(domain)
    assert orm.nombre == "Té verde"
    assert orm.sku == "TE-456"
    assert orm.stock == 0
    assert orm.precio == 0.0
    assert orm.descripcion == "Orgánico"