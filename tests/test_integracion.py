# tests/test_integracion.py
from app.cliente import ClienteRepository
from app.producto import ProductoRepository
from app.pedido import Pedido
from app.facturacion import calcular_factura

def test_flujo_integracion_registrar_pedido_y_facturar():
    # repos
    crepo = ClienteRepository()
    prepo = ProductoRepository()

    cliente = crepo.crear("Cliente Test")
    p1 = prepo.crear("Americano", 3.0)
    p2 = prepo.crear("Capuccino", 4.5)

    # crear pedido
    pedido = Pedido(id=1, cliente_id=cliente.id)
    pedido.agregar_producto(p1, cantidad=1)  # 3.0
    pedido.agregar_producto(p2, cantidad=2)  # 9.0
    subtotal = pedido.subtotal()
    assert subtotal == 12.0

    s, iva, total = calcular_factura(subtotal)
    assert s == 12.0
    # IVA 13% de 12.0 = 1.56 -> redondeado 1.56, total 13.56
    assert iva == 1.56
    assert total == 13.56
