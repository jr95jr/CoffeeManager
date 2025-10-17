import pytest
from app.cliente import ClienteRepository
from app.producto import ProductoRepository
from app.pedido import Pedido
from app.facturacion import calcular_factura

@pytest.fixture
def repos():
    return ClienteRepository(), ProductoRepository()

def test_flujo_integracion_registrar_pedido_y_facturar(repos):
    crepo, prepo = repos

    # Crear cliente y productos
    cliente = crepo.crear("Cliente Test", "test@example.com")
    p1 = prepo.crear("Americano", 3.0)
    p2 = prepo.crear("Capuccino", 4.5)

    # Crear pedido
    pedido = Pedido(id=1, cliente_id=cliente.id)
    pedido.agregar_producto(p1, 1)  # 3.0
    pedido.agregar_producto(p2, 2)  # 9.0
    subtotal = pedido.subtotal()
    assert subtotal == 12.0

    s, iva, total = calcular_factura(subtotal)
    assert s == 12.0
    assert iva == 1.56  # 13% de 12
    assert total == 13.56
