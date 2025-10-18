import streamlit as st
from app.cliente import ClienteRepository
from app.producto import ProductoRepository
from app.pedido import PedidoRepository
from app.db import Base, engine
from app.cliente import Cliente
from app.producto import Producto
from app.pedido import Pedido

Base.metadata.create_all(bind=engine)

# Inicializar repositorios
if "clientes_repo" not in st.session_state:
    st.session_state["clientes_repo"] = ClienteRepository()
if "productos_repo" not in st.session_state:
    st.session_state["productos_repo"] = ProductoRepository()
if "pedidos_repo" not in st.session_state:
    st.session_state["pedidos_repo"] = PedidoRepository()

clientes_repo = st.session_state["clientes_repo"]
productos_repo = st.session_state["productos_repo"]
pedidos_repo = st.session_state["pedidos_repo"]

# Menú lateral
st.sidebar.title("Menú")
opcion = st.sidebar.radio("Selecciona una opción", ["Clientes", "Productos", "Pedidos"])

# ------------------ CLIENTES ------------------
if opcion == "Clientes":
    st.header("Gestión de Clientes")
    accion = st.radio("Acción", ["Listar", "Crear", "Actualizar", "Eliminar"], horizontal=True)

    if accion == "Crear":
        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo")
        telefono = st.text_input("Teléfono")
        direccion = st.text_input("Dirección")
        if st.button("Agregar Cliente"):
            clientes_repo.agregar_cliente(nombre, correo, telefono, direccion)
            st.success(f"Cliente {nombre} agregado.")

    elif accion == "Listar":
        clientes = clientes_repo.listar_clientes()
        for c in clientes:
            with st.expander(f"{c.id} - {c.nombre}"):
                st.write(f"Correo: {c.correo}")
                st.write(f"Teléfono: {c.telefono}")
                st.write(f"Dirección: {c.direccion}")

    elif accion == "Actualizar":
        clientes = clientes_repo.listar_clientes()
        cliente_sel = st.selectbox("Selecciona cliente", clientes, format_func=lambda c: f"{c.id} - {c.nombre}")
        nuevo_nombre = st.text_input("Nuevo nombre", cliente_sel.nombre)
        nuevo_correo = st.text_input("Nuevo correo", cliente_sel.correo)
        nuevo_telefono = st.text_input("Nuevo teléfono", cliente_sel.telefono)
        nueva_direccion = st.text_input("Nueva dirección", cliente_sel.direccion)
        if st.button("Actualizar Cliente"):
            clientes_repo.actualizar_cliente(cliente_sel.id, nuevo_nombre, nuevo_correo, nuevo_telefono, nueva_direccion)
            st.success(f"Cliente {cliente_sel.id} actualizado.")

    elif accion == "Eliminar":
        clientes = clientes_repo.listar_clientes()
        cliente_sel = st.selectbox("Selecciona cliente", clientes, format_func=lambda c: f"{c.id} - {c.nombre}")
        if st.button("Eliminar Cliente"):
            clientes_repo.eliminar_cliente(cliente_sel.id)
            st.success(f"Cliente {cliente_sel.id} eliminado.")

# ------------------ PRODUCTOS ------------------
elif opcion == "Productos":
    st.header("Gestión de Productos")
    accion = st.radio("Acción", ["Listar", "Crear", "Actualizar", "Eliminar"], horizontal=True)

    if accion == "Crear":
        nombre = st.text_input("Nombre")
        precio = st.number_input("Precio", min_value=0.0, format="%.2f")
        if st.button("Agregar Producto"):
            productos_repo.agregar_producto(nombre, precio)
            st.success(f"Producto {nombre} agregado.")

    elif accion == "Listar":
        productos = productos_repo.listar_productos()
        for p in productos:
            with st.expander(f"{p.id} - {p.nombre}"):
                st.write(f"Precio: ${p.precio:.2f}")

    elif accion == "Actualizar":
        productos = productos_repo.listar_productos()
        producto_sel = st.selectbox("Selecciona producto", productos, format_func=lambda p: f"{p.id} - {p.nombre}")
        nuevo_nombre = st.text_input("Nuevo nombre", producto_sel.nombre)
        nuevo_precio = st.number_input("Nuevo precio", value=producto_sel.precio, min_value=0.0, format="%.2f")
        if st.button("Actualizar Producto"):
            productos_repo.actualizar_producto(producto_sel.id, nuevo_nombre, nuevo_precio)
            st.success(f"Producto {producto_sel.id} actualizado.")

    elif accion == "Eliminar":
        productos = productos_repo.listar_productos()
        producto_sel = st.selectbox("Selecciona producto", productos, format_func=lambda p: f"{p.id} - {p.nombre}")
        if st.button("Eliminar Producto"):
            productos_repo.eliminar_producto(producto_sel.id)
            st.success(f"Producto {producto_sel.id} eliminado.")

# ------------------ PEDIDOS ------------------
elif opcion == "Pedidos":
    st.header("Gestión de Pedidos")
    accion = st.radio("Acción", ["Listar", "Crear", "Eliminar"], horizontal=True)

    if accion == "Crear":
        clientes = clientes_repo.listar_clientes()
        productos = productos_repo.listar_productos()
        cliente_sel = st.selectbox("Selecciona Cliente", clientes, format_func=lambda c: f"{c.id} - {c.nombre}")
        productos_sel = st.multiselect("Selecciona Productos", productos, format_func=lambda p: f"{p.id} - {p.nombre} (${p.precio})")
        if st.button("Crear Pedido"):
            if productos_sel:
                pedidos_repo.crear_pedido(cliente_sel, productos_sel)
                st.success("Pedido creado exitosamente.")
            else:
                st.error("Debes seleccionar al menos un producto.")

    elif accion == "Listar":
        pedidos = pedidos_repo.listar_pedidos()
        for p in pedidos:
            with st.expander(f"Pedido {p.id} - Cliente: {p.cliente.nombre}"):
                st.write(f"Total: ${p.total_final:.2f}")
                st.write("Productos:")
                for prod in p.productos:
                    st.write(f"- {prod.nombre} (${prod.precio:.2f})")

    elif accion == "Eliminar":
        pedidos = pedidos_repo.listar_pedidos()
        pedido_sel = st.selectbox("Selecciona Pedido", pedidos, format_func=lambda p: f"{p.id} - Cliente: {p.cliente.nombre}")
        if st.button("Eliminar Pedido"):
            pedidos_repo.eliminar_pedido(pedido_sel.id)
            st.success(f"Pedido {pedido_sel.id} eliminado.")
