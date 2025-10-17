from sqlalchemy import Column, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from .db import Base, Session
from .cliente import Cliente
from .producto import Producto

pedido_producto = Table(
    "pedido_producto",
    Base.metadata,
    Column("pedido_id", Integer, ForeignKey("pedidos.id", ondelete="CASCADE")),
    Column("producto_id", Integer, ForeignKey("productos.id", ondelete="CASCADE"))
)

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    total = Column(Float)
    iva = Column(Float)
    total_final = Column(Float)
    cliente = relationship("Cliente")
    productos = relationship("Producto", secondary=pedido_producto)

class PedidoRepository:
    def __init__(self):
        self.session = Session()

    def crear_pedido(self, cliente, lista_productos):
        subtotal = sum([p.precio for p in lista_productos])
        iva = subtotal * 0.13
        total_final = subtotal + iva

        pedido = Pedido(cliente_id=cliente.id, total=subtotal, iva=iva, total_final=total_final)
        pedido.productos.extend(lista_productos)
        self.session.add(pedido)
        self.session.commit()
        return pedido

    def listar_pedidos(self):
        return self.session.query(Pedido).all()

    def eliminar_pedido(self, pedido_id):
        pedido = self.session.get(Pedido, pedido_id)
        if pedido:
            self.session.delete(pedido)
            self.session.commit()
