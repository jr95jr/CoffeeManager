from sqlalchemy import Column, Integer, String, Float
from .db import Base, Session

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)

class ProductoRepository:
    def __init__(self):
        self.session = Session()

    def agregar_producto(self, nombre, precio):
        producto = Producto(nombre=nombre, precio=precio)
        self.session.add(producto)
        self.session.commit()
        return producto

    def listar_productos(self):
        return self.session.query(Producto).all()

    def actualizar_producto(self, producto_id, nombre, precio):
        producto = self.session.get(Producto, producto_id)
        if producto:
            producto.nombre = nombre
            producto.precio = precio
            self.session.commit()

    def eliminar_producto(self, producto_id):
        producto = self.session.get(Producto, producto_id)
        if producto:
            self.session.delete(producto)
            self.session.commit()
