import pytest
from app.producto import ProductoRepository

@pytest.fixture
def repo():
    return ProductoRepository()

def test_crear_producto_valido(repo):
    producto = repo.crear("Café Espresso", 2.5)
    assert producto.id is not None
    assert producto.precio == 2.5

def test_crear_producto_duplicado(repo):
    repo.crear("Cappuccino", 3.0)
    prod2 = repo.crear("Cappuccino", 3.0)  # duplicado
    assert prod2 is None

def test_listar_productos(repo):
    repo.crear("Té Verde", 1.5)
    productos = repo.listar()
    assert len(productos) >= 1

def test_obtener_producto(repo):
    prod = repo.crear("Latte", 3.5)
    encontrado = repo.obtener(prod.id)
    assert encontrado.nombre == "Latte"
