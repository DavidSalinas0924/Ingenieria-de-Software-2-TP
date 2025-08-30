from app.domain.models.producto import Producto
from app.db.models.producto import ProductoORM

def producto_orm_to_domain(orm_obj: ProductoORM) -> Producto:
    return Producto(
        id=orm_obj.id,
        nombre=orm_obj.nombre.strip(),
        sku=orm_obj.sku.upper(),
        stock=max(0, orm_obj.stock),
        precio=max(0.0, orm_obj.precio),
        descripcion=orm_obj.descripcion.strip() if orm_obj.descripcion else None
    )

def producto_domain_to_orm(domain_obj: Producto) -> ProductoORM:
    return ProductoORM(
        id=domain_obj.id,
        nombre=domain_obj.nombre.strip(),
        sku=domain_obj.sku.upper(),
        stock=max(0, domain_obj.stock),
        precio=max(0.0, domain_obj.precio),
        descripcion=domain_obj.descripcion.strip() if domain_obj.descripcion else None
    )