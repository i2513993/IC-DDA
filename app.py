import streamlit as st
from models.cliente import Cliente
from services.cliente_services import crear_cliente
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
    # Inputs
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value = 0)
    saldo = st.number_input("Saldo", min_value = 0.0)

    submit = st.form_submit_button("Crear Cliente")

    if submit:
        try:
            if nombre == "":
                st.warning("Debe ingresar un nombre")   
            elif saldo < 0:
                st.warning("El saldo no puede ser negativo")

            else:
                # Crea Cliente + Mensaje
                cliente, mensaje = crear_cliente(nombre, edad, saldo)

                st.success("Cliente creado correctamente")
                st.info(mensaje)

            #Guardar en Memoria
                st.session_state.clientes.append({
                "Nombre": cliente.get_nombre(),
                "Edad": cliente.get_edad(),
                "Saldo": cliente.get_saldo()
            })


        except ValueError as e:
            st.warning(str(e))
        except Exception:
            st.error("Error inesperado")

if len(st.session_state.clientes) > 0:

    st.write("### Tabla de Clientes")
    mostrar_tabla(st.session_state.clientes)
    mostrar_clientes(st.session_state.clientes)
    mostrar_analisis(st.session_state.clientes)

else:
    st.write("No hay clientes registrados")