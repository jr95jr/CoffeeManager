from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from .db import Base
from datetime import datetime

class PedidoItem:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

class Pedido:
    def __init__(self, id, cliente_id):
        self.id = id
        self.cliente_id = cliente_id
        self.items = []

    def agregar_producto(self, producto, cantidad):
        # Si ya existe el producto, suma cantidad
        for it in self.items:
            if it.producto.id == producto.id:
                it.cantidad += cantidad
                return
        self.items.append(PedidoItem(producto, cantidad))

    def subtotal(self):
        return sum(it.producto.precio * it.cantidad for it in self.items)
