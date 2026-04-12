import pandas as pd 
import streamlit as st


def mostrar_tabla(clientes):
    df = pd.DataFrame(clientes)
    st.dataframe(df)

def mostrar_clientes(clientes):
    st.write("### Lista de clientes (for)")
    for c in st.session_state.clientes:
        st.write(f"{c['Nombre']} - Edad: {c['Edad']}")

    st.write("### Recorrido con While")
    i = 0
    while i < len(st.session_state.clientes):
        c = st.session_state.clientes[i]
        st.write(f"{c['Nombre']} - Edad: {c['Edad']}")
        i += 1

def calcular_promedio(clientes):
    suma = 0
    for c in clientes:
        suma += c["Saldo"]
    return suma / len(clientes)

def mostrar_analisis(clientes):
    contador = len (st.session_state.clientes)
    st.write(f"Total de clientes: {contador}")

    promedio = calcular_promedio(st.session_state.clientes)
    st.write(f"Promedio de saldo: S/ {round(promedio, 2)}")