from sqlalchemy import Column, Integer, String
from .db import Base, Session

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    telefono = Column(String(20))
    direccion = Column(String(200))

class ClienteRepository:
    def __init__(self):
        self.session = Session()

    def agregar_cliente(self, nombre, correo, telefono, direccion):
        cliente = Cliente(nombre=nombre, correo=correo, telefono=telefono, direccion=direccion)
        self.session.add(cliente)
        self.session.commit()
        return cliente

    def listar_clientes(self):
        return self.session.query(Cliente).all()

    def actualizar_cliente(self, cliente_id, nombre, correo, telefono, direccion):
        cliente = self.session.get(Cliente, cliente_id)
        if cliente:
            cliente.nombre = nombre
            cliente.correo = correo
            cliente.telefono = telefono
            cliente.direccion = direccion
            self.session.commit()

    def eliminar_cliente(self, cliente_id):
        cliente = self.session.get(Cliente, cliente_id)
        if cliente:
            self.session.delete(cliente)
            self.session.commit()
