from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db import Base, engine, SessionLocal
from datetime import datetime
from app.cliente import Cliente
from app.producto import Producto

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)
    fecha = Column(Float, default=datetime.utcnow)

    cliente = relationship("Cliente")
    producto = relationship("Producto")

def crear_tabla():
    Base.metadata.create_all(bind=engine)
