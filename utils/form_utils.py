import streamlit as st
from services.cliente_services import crear_cliente
from services.supabase_client import insertar_cliente

def procesar_cliente(nombre, edad, saldo):

    try:
        if nombre == "":
            st.warning("Ingrese un nombre válido")
            return

        if saldo < 0:
            st.warning("El saldo no puede ser negativo")
import streamlit as st
from services.cliente_services import crear_cliente
from services.supabase_client import insertar_cliente, actualizar_cliente

def procesar_cliente(nombre, edad, saldo):
    try:
        if nombre == "":
            st.warning("Ingrese un nombre válido")
            return

        cliente, mensaje = crear_cliente(nombre, edad, saldo)
        st.success("Cliente creado correctamente")
        st.info(mensaje)

        cliente_dict = {
            "nombre": cliente.get_nombre(),
            "edad": cliente.get_edad(),
            "saldo": cliente.get_saldo()
        }

        insertar_cliente(cliente_dict)

    except ValueError as e:
        st.warning(str(e))
    except Exception as e:
        st.error("Error inesperado: " + str(e))

def procesar_edicion(id, nombre, edad, saldo):
    try:
        if nombre == "":
            st.warning("El nombre es obligatorio")
            return
        if not nombre.replace(" ", "").isalpha():
            st.warning("El nombre solo debe contener letras")
            return
        if edad < 18:
            st.warning("El cliente debe ser mayor de edad")
            return
        if saldo < 0:
            st.warning("El saldo no puede ser negativo")
            return

        cliente_dict = {
            "nombre": nombre,
            "edad": int(edad),
            "saldo": float(saldo)
        }

        actualizar_cliente(id, cliente_dict)
        st.success("Cliente actualizado correctamente")
        st.session_state.editando = None
        st.rerun()

    except Exception as e:
        st.error("Error inesperado: " + str(e))