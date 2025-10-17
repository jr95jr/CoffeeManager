# tests/test_pedido.py
from app.producto import ProductoRepository
from app.pedido import Pedido

def test_agregar_productos_y_subtotal():
    prod_repo = ProductoRepository()
    p1 = prod_repo.crear("Café", 2.0)
    p2 = prod_repo.crear("Té", 1.5)

    pedido = Pedido(id=1, cliente_id=1)
    pedido.agregar_producto(p1, cantidad=2)  # 2*2.0 = 4.0
    pedido.agregar_producto(p2, cantidad=3)  # 3*1.5 = 4.5
    pedido.agregar_producto(p1, cantidad=1)  # ahora p1 total 3*2.0 = 6.0

    assert len(pedido.items) == 2
    assert pedido.subtotal() == 10.5
