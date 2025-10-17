from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from app.db import Base, engine, SessionLocal

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    direccion = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<Cliente(nombre='{self.nombre}', correo='{self.correo}')>"

# Crear tabla
def crear_tabla():
    Base.metadata.create_all(bind=engine)

# CRUD
def agregar_cliente(nombre, correo, telefono=None, direccion=None):
    session = SessionLocal()
    try:
        nuevo = Cliente(nombre=nombre, correo=correo, telefono=telefono, direccion=direccion)
        session.add(nuevo)
        session.commit()
        session.refresh(nuevo)
        return nuevo
    except IntegrityError:
        session.rollback()
        return None  # Ya existe
    finally:
        session.close()

def obtener_clientes():
    session = SessionLocal()
    clientes = session.query(Cliente).all()
    session.close()
    return clientes
