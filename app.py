import streamlit as st
from models.cliente import Cliente
from services.cliente_services import crear_cliente


st.title("DEMO POO - CIENCIA DE DATOS")
st.write("Ingrese los datos del cliente")

nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value= 0)
saldo = st.number_input("Saldo", min_value= 0.0)

if st.button("Crear Cliente"):

    try:
        #Secuencia
        cliente, mensaje = crear_cliente(nombre, edad, saldo)

        st.success("Cliente creado correctamente")

        st.info (mensaje)
        st.write("### Informacion de cliente")
        st.write(cliente.mostrar_info())

        if hasattr (cliente, "clasificar_cliente"):
            st.white("### Clasificación")
            st.write(cliente.clasificar_cliente())

        if hasattr (cliente,"Es mayor de edad")
            if cliente.es_mayor_de_edad():
                st.success("Es mayor de edad")
            else:
                st.warning("Es menor de edad")
    except Exception as e:
        st.error(str(e))
