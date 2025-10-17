import pytest
from app.cliente import ClienteRepository
from app.producto import ProductoRepository
from app.pedido import PedidoRepository

@pytest.fixture
def clientes_repo():
    return ClienteRepository()

@pytest.fixture
def productos_repo():
    return ProductoRepository()

@pytest.fixture
def pedidos_repo():
    return PedidoRepository()

def test_crear_pedido(clientes_repo, productos_repo, pedidos_repo):
    cliente = clientes_repo.agregar_cliente("Pedido User", "pedido@example.com")
    prod1 = productos_repo.agregar_producto("Coffee A", 2.0)
    prod2 = productos_repo.agregar_producto("Coffee B", 3.0)
    
    pedido = pedidos_repo.crear_pedido(cliente, [prod1, prod2])
    
    assert pedido.id is not None
    assert len(pedido.productos) == 2
    assert round(pedido.total,2) == 5.0
    assert round(pedido.iva,2) == 0.65
    assert round(pedido.total_final,2) == 5.65
