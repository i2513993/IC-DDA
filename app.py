import streamlit as st
from models.cliente import Cliente
from services.cliente_services import crear_cliente

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Demo POO", layout="centered")

st.title("DEMO POO - CIENCIA DE DATOS")
st.write("Complete el formulario para registrar un nuevo cliente en el sistema.")

# ENTRADAS DE USUARIO
with st.container():
    nombre = st.text_input("Nombre completo")
    col1, col2 = st.columns(2)
    with col1:
        edad = st.number_input("Edad", min_value=0, step=1)
    with col2:
        saldo = st.number_input("Saldo Inicial", min_value=0.0, step=10.0)

# BOTÓN DE ACCIÓN
if st.button("Registrar Cliente"):
    try:
        # Llamamos al servicio (que nos devuelve el objeto y un mensaje)
        cliente_obj, mensaje_servicio = crear_cliente(nombre, edad, saldo)

        # Si todo sale bien:
        st.success("¡Proceso completado!")
        st.info(mensaje_servicio)
    
        st.subheader("Ficha del Cliente")
        st.code(cliente_obj.mostrar_info())

        # Uso de métodos de la clase
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Categoría:**")
            st.write(cliente_obj.clasificar_cliente())
        
        with col_b:
            if cliente_obj.es_mayor_de_edad():
                st.write("**Estado:**")
                st.write("Adulto Verificado")

    except ValueError as e:
        # Aquí atrapamos los "raise ValueError" de los servicios
        st.warning(f"Error de validación: {e}")
    except Exception as e:
        # Error genérico por si algo falla en el servidor
        st.error(f"Error inesperado: {e}")