from app.cliente import crear_tabla, agregar_cliente, obtener_clientes
from app.producto import crear_tabla as crear_tabla_producto, agregar_producto, obtener_productos

# Crear tablas
crear_tabla()
crear_tabla_producto()

# Agregar cliente de prueba (no duplicar)
cliente = agregar_cliente("Joel Rojas", "joel@example.com")
if cliente:
    print("Cliente agregado:", cliente)
else:
    print("Cliente ya existe")

# Agregar producto de prueba
producto = agregar_producto("Café Espresso", 2.5)
if producto:
    print("Producto agregado:", producto)
else:
    print("Producto ya existe")

# Mostrar clientes
print("\nClientes registrados:")
for c in obtener_clientes():
    print(c)

# Mostrar productos
print("\nProductos registrados:")
for p in obtener_productos():
    print(p)
