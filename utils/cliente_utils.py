import pandas as pd
import streamlit as st
from services.supabase_client import eliminar_cliente

def mostrar_tabla_con_acciones(clientes):
    st.write("#### Registros")
    for c in clientes:
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 1])
        with col1:
            st.write(c["nombre"])
        with col2:
            st.write(f"Edad: {c['edad']}")
        with col3:
            st.write(f"S/ {c['saldo']}")
        with col4:
            if st.button("✏️", key=f"edit_{c['id']}"):
                st.session_state.editando = c
                st.rerun()
        with col5:
            if st.button("🗑️", key=f"del_{c['id']}"):
                eliminar_cliente(c["id"])
                st.success("Cliente eliminado")
                st.rerun()

def mostrar_tabla(clientes):
    df = pd.DataFrame(clientes)
    st.dataframe(df)

def mostrar_clientes(clientes):
    st.write("### Lista de clientes (for)")
    for c in clientes:
        st.write(f"{c['nombre']} - Edad: {c['edad']}")

    st.write("### Recorrido con While")
    i = 0
    while i < len(clientes):
        c = clientes[i]
        st.write(f"{c['nombre']} - Edad: {c['edad']}")
        i += 1

def calcular_promedio(clientes):
    suma = 0
    for c in clientes:
        suma += c["saldo"]
    return suma / len(clientes)

def mostrar_analisis(clientes):
    st.write(f"Total de clientes: {len(clientes)}")
    promedio = calcular_promedio(clientes)
    st.write(f"Promedio de saldo: S/ {round(promedio, 2)}")