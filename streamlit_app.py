# streamlit_app.py
import streamlit as st
from app.cliente import ClienteRepository
from app.producto import ProductoRepository
from app.pedido import Pedido
from app.facturacion import calcular_factura

# Repositorios en memoria (persisten mientras la app está viva)
if "clientes_repo" not in st.session_state:
    st.session_state["clientes_repo"] = ClienteRepository()
if "productos_repo" not in st.session_state:
    st.session_state["productos_repo"] = ProductoRepository()
if "pedidos" not in st.session_state:
    st.session_state["pedidos"] = {}

clientes_repo = st.session_state["clientes_repo"]
productos_repo = st.session_state["productos_repo"]
pedidos_store = st.session_state["pedidos"]

st.title("CoffeeManager - Gestión de Pedidos")

menu = st.sidebar.selectbox("Menú", ["Registrar cliente", "Registrar producto", "Crear pedido", "Listar clientes", "Listar productos"])

if menu == "Registrar cliente":
    st.header("Registrar cliente")
    nombre = st.text_input("Nombre")
    telefono = st.text_input("Teléfono")
    direccion = st.text_input("Dirección")
    if st.button("Guardar cliente"):
        if not nombre:
            st.warning("Ingrese un nombre")
        else:
            c = clientes_repo.crear(nombre, telefono, direccion)
            st.success(f"Cliente registrado (ID {c.id})")

elif menu == "Registrar producto":
    st.header("Registrar producto")
    nombre = st.text_input("Nombre del producto")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    if st.button("Guardar producto"):
        if not nombre:
            st.warning("Ingrese nombre")
        else:
            p = productos_repo.crear(nombre, precio)
            st.success(f"Producto registrado (ID {p.id})")

elif menu == "Crear pedido":
    st.header("Crear pedido")
    clientes = clientes_repo.listar()
    productos = productos_repo.listar()
    if not clientes:
        st.info("No hay clientes. Registra uno antes.")
    if not productos:
        st.info("No hay productos. Registra alguno antes.")

    cliente_sel = st.selectbox("Cliente", options=[(c.id, c.nombre) for c in clientes], format_func=lambda x: f"{x[1]}" if x else "")
    producto_sel = st.selectbox("Producto", options=[(p.id, p.nombre, p.precio) for p in productos], format_func=lambda x: f"{x[1]} - ${x[2]:.2f}" if x else "")
    cantidad = st.number_input("Cantidad", min_value=1, value=1, step=1)
    if st.button("Agregar al pedido"):
        if cliente_sel and producto_sel:
            cliente_id = cliente_sel[0]
            producto_id = producto_sel[0]
            producto = productos_repo.obtener(producto_id)
            # Si no existe un pedido activo para este cliente, crear
            pedido = pedidos_store.get(cliente_id)
            if pedido is None:
                pedido = Pedido(id=len(pedidos_store)+1, cliente_id=cliente_id)
                pedidos_store[cliente_id] = pedido
            pedido.agregar_producto(producto, cantidad)
            st.success("Producto agregado al pedido")

    st.subheader("Pedidos actuales")
    for cid, ped in pedidos_store.items():
        st.markdown(f"**Pedido {ped.id} - Cliente {cid}**")
        for it in ped.items:
            st.write(f"- {it.producto.nombre} x{it.cantidad} = ${it.producto.precio * it.cantidad:.2f}")
        sub = ped.subtotal()
        s, iva, total = calcular_factura(sub)
        st.write(f"Subtotal: ${s:.2f}  |  IVA(13%): ${iva:.2f}  |  Total: ${total:.2f}")
        if st.button(f"Eliminar pedido {ped.id}", key=f"del_{ped.id}"):
            del pedidos_store[cid]
            st.experimental_rerun()

elif menu == "Listar clientes":
    st.header("Clientes")
    for c in clientes_repo.listar():
        st.write(f"{c.id} - {c.nombre} | Tel: {c.telefono} | Dir: {c.direccion}")

elif menu == "Listar productos":
    st.header("Productos")
    for p in productos_repo.listar():
        st.write(f"{p.id} - {p.nombre} | Precio: ${p.precio:.2f}")
