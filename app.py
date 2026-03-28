import streamlit as st
import pandas as pd
from models.cliente import Cliente
from services.cliente_service import crear_cliente


st.title("Demo POO - Ciencia de Datos")
st.write("Ingrese los datos del cliente:")

# Inputs
nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value = 0)
saldo = st.number_input("Saldo", min_value = 0.0)

# Botón
if st.button("Crear Cliente"):

    try:
        # Crea Cliente + Mensaje
        cliente, mensaje = crear_cliente(nombre, edad, saldo)

        st.success("Cliente creado correctamente")

        st.info(mensaje)

        st.write("### Información del cliente: ")
        st.write(cliente.mostrar_info())

        data = {
            "Nombre": [cliente.get_nombre()],
            "Edad": [cliente.get_edad()],
            "Saldo": [cliente.get_saldo()]
        }

        df = pd.DataFrame(data)

        st.write("### Tabla del Cliente")
        st.dataframe(df)

    
    except Exception as e:
        st.error(str(e))