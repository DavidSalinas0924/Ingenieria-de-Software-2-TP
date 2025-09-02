from sqlalchemy.orm import Session
from app.db.models.producto import ProductoORM
from app.domain.models.producto import Producto
from app.domain.mappers.producto_mapper import producto_to_orm, orm_to_producto

class ProductoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, producto: Producto) -> None:
        orm = producto_to_orm(producto)
        self.session.add(orm)
        self.session.commit()

    def get_all(self) -> list[Producto]:
        productos_orm = self.session.query(ProductoORM).all()
        return [orm_to_producto(p) for p in productos_orm]