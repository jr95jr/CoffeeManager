from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.exc import IntegrityError
from .db import Base, engine, SessionLocal

# Modelo Producto
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    precio = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Producto(nombre='{self.nombre}', precio={self.precio})>"

# Crear tabla
def crear_tabla():
    Base.metadata.create_all(bind=engine)

# CRUD
def agregar_producto(nombre, precio):
    session = SessionLocal()
    try:
        nuevo = Producto(nombre=nombre, precio=precio)
        session.add(nuevo)
        session.commit()
        session.refresh(nuevo)
        return nuevo
    except IntegrityError:
        session.rollback()
        return None  # Ya existe
    finally:
        session.close()

def obtener_productos():
    session = SessionLocal()
    productos = session.query(Producto).all()
    session.close()
    return productos

# Repository
class ProductoRepository:
    def __init__(self):
        crear_tabla()

    def crear(self, nombre, precio):
        return agregar_producto(nombre, precio)

    def listar(self):
        return obtener_productos()

    def obtener(self, producto_id):
        productos = obtener_productos()
        for p in productos:
            if p.id == producto_id:
                return p
        return None
