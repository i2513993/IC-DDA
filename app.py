import streamlit as st
from utils.form_utils import procesar_cliente, procesar_edicion
from utils.cliente_utils import mostrar_tabla_con_acciones, mostrar_clientes, mostrar_analisis
from services.supabase_client import obtener_clientes

st.title("Demo POO - Ciencia de Datos")

if "clientes" not in st.session_state:
    st.session_state.clientes = []

if "editando" not in st.session_state:
    st.session_state.editando = None

# ── FORMULARIO CREAR ──────────────────────────────────────
if st.session_state.editando is None:
    st.write("Ingrese los datos del cliente:")
    with st.form("form_cliente"):
        nombre = st.text_input("Nombre")
        edad = st.number_input("Edad", min_value=0)
        saldo = st.number_input("Saldo")
        submitted = st.form_submit_button("Crear Cliente")
        if submitted:
            procesar_cliente(nombre, edad, saldo)

# ── FORMULARIO EDITAR ─────────────────────────────────────
else:
    cliente = st.session_state.editando
    st.write(f"### Editando cliente: {cliente['nombre']}")
    with st.form("form_editar"):
        nombre = st.text_input("Nombre", value=cliente["nombre"])
        edad = st.number_input("Edad", min_value=0, value=cliente["edad"])
        saldo = st.number_input("Saldo", value=float(cliente["saldo"]))
        col1, col2 = st.columns(2)
        with col1:
            guardar = st.form_submit_button("Guardar cambios")
        with col2:
            cancelar = st.form_submit_button("Cancelar")

        if guardar:
            procesar_edicion(cliente["id"], nombre, edad, saldo)
        if cancelar:
            st.session_state.editando = None
            st.rerun()

# ── TABLA DESDE SUPABASE ──────────────────────────────────
st.write("### Tabla de Clientes (Base de datos)")
clientes_db = obtener_clientes()

if clientes_db:
    mostrar_tabla_con_acciones(clientes_db)
    mostrar_clientes(clientes_db)
    mostrar_analisis(clientes_db)
else:
    st.warning("Aún no hay clientes registrados")