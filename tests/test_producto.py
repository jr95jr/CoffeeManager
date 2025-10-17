# tests/test_producto.py
import pytest
from app.producto import ProductoRepository

def test_crear_producto_valido():
    repo = ProductoRepository()
    p = repo.crear("Café Espresso", 2.5)
    assert p.id == 1
    assert p.precio == 2.5

def test_precio_negativo_error():
    repo = ProductoRepository()
    with pytest.raises(ValueError):
        repo.crear("Malo", -5)
