import streamlit as st
from utils.from_utils import procesar_cliente
from utils.cliente_utils import (
    mostrar_tabla,
    mostrar_clientes,
    mostrar_analisis
)

st.title("Demo POO - Ciencia de Datos")
st.write("Ingrese los datos del cliente:")

if 'clientes' not in st.session_state:
    st.session_state.clientes = []

with st.form("form_cliente"):
    nombre = st.text_input("Nombre")
    edad   = st.number_input("Edad", min_value=0)
    saldo  = st.number_input("Saldo")

    submitted = st.form_submit_button("Crear Cliente")

    if submitted:
        procesar_cliente(nombre, edad, saldo)

if len(st.session_state.clientes) > 0:
    st.write("### Tabla de Clientes")
    mostrar_tabla(st.session_state.clientes)
    mostrar_clientes(st.session_state.clientes)
    mostrar_analisis(st.session_state.clientes)
else:
    st.write("No hay clientes registrados")