import pytest
from app.producto import ProductoRepository
from app.pedido import Pedido

@pytest.fixture
def productos_repo():
    return ProductoRepository()

def test_agregar_productos_y_subtotal(productos_repo):
    p1 = productos_repo.crear("Café", 2.0)
    p2 = productos_repo.crear("Té", 1.5)

    pedido = Pedido(id=1, cliente_id=1)
    pedido.agregar_producto(p1, 2)  # 2*2 = 4
    pedido.agregar_producto(p2, 3)  # 3*1.5 = 4.5
    pedido.agregar_producto(p1, 1)  # ahora p1 total = 6

    assert len(pedido.items) == 2
    assert pedido.subtotal() == 10.5
