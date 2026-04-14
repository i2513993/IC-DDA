import streamlit as st
from services.cliente_service import crear_cliente
from services.supabase_service import insertar_cliente

def procesar_cliente(nombre, edad, saldo):

    try:
        if nombre == "":
            st.warning("Ingrese un nombre válido")
            return

        if saldo < 0:
            st.warning("El saldo no puede ser negativo")
            return

        cliente, mensaje = crear_cliente(nombre, edad, saldo)

        st.success("Cliente creado correctamente")
        st.info(mensaje)

        cliente_dict = {
            "nombre": cliente.get_nombre(),
            "edad": cliente.get_edad(),
            "saldo": cliente.get_saldo()
        }

        # Guardar en memoria
        st.session_state.clientes.append({
            "Nombre": cliente.get_nombre(),
            "Edad": cliente.get_edad(),
            "Saldo": cliente.get_saldo()
        })

        # Guardar en Supabase
        insertar_cliente(cliente_dict)

    except ValueError as e:
        st.warning(str(e))

    except Exception as e:
        st.error("Error inesperado: " + str(e))