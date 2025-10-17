import pytest
from app.producto import ProductoRepository

@pytest.fixture
def repo():
    return ProductoRepository()

def test_agregar_producto(repo):
    producto = repo.agregar_producto("Test Coffee", 1.5)
    assert producto.id is not None
    assert producto.nombre == "Test Coffee"
    assert producto.precio == 1.5
