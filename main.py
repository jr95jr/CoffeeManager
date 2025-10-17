from app.cliente import ClienteRepository
from app.producto import ProductoRepository
from app.pedido import PedidoRepository

def main():
    clientes_repo = ClienteRepository()
    productos_repo = ProductoRepository()
    pedidos_repo = PedidoRepository()

    # Agregar Cliente
    cliente = clientes_repo.agregar_cliente("Joel Rojas", "joel@example.com", "123456789", "Calle Falsa 123")
    print(f"Cliente agregado: {cliente.nombre} - {cliente.correo}")

    # Agregar Productos
    prod1 = productos_repo.agregar_producto("Café Espresso", 2.5)
    prod2 = productos_repo.agregar_producto("Café Latte", 3.0)
    print(f"Producto agregado: {prod1.nombre} - ${prod1.precio}")
    print(f"Producto agregado: {prod2.nombre} - ${prod2.precio}")

    # Crear Pedido con varios productos
    pedido = pedidos_repo.crear_pedido(cliente, [prod1, prod2])
    print(f"Pedido creado para {cliente.nombre}")
    print(f"Productos: {[p.nombre for p in pedido.productos]}")
    print(f"Subtotal: ${pedido.total:.2f}, IVA: ${pedido.iva:.2f}, Total Final: ${pedido.total_final:.2f}")

    # Listar Clientes
    print("\nClientes registrados:")
    for c in clientes_repo.listar_clientes():
        print(f"- {c.nombre} ({c.correo})")

    # Listar Productos
    print("\nProductos registrados:")
    for p in productos_repo.listar_productos():
        print(f"- {p.nombre} - ${p.precio}")

    # Listar Pedidos
    print("\nPedidos registrados:")
    for ped in pedidos_repo.listar_pedidos():
        print(f"- Pedido {ped.id} Cliente: {ped.cliente.nombre}, Total: ${ped.total_final:.2f}")

if __name__ == "__main__":
    main()
