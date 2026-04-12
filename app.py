import streamlit as st
import pandas as pd
from models.cliente import Cliente
from services.cliente_services import crear_cliente


st.title("Demo POO - Ciencia de Datos")
st.write("Ingrese los datos del cliente:")

# Inicializar lista de clientes
if 'clientes' not in st.session_state:
    st.session_state.clientes = []

def mostrar_tabla(clientes):
    df = pd.DataFrame(clientes)
    st.dataframe(df)

def calcular_promedio (clientes):
    suma = 0
    for c in clientes:
        suma += c['Saldo']
    promedio = suma / len(clientes)
    return promedio


with st.form("form_cliente"):
    # Inputs
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value = 0)
    saldo = st.number_input("Saldo", min_value = 0.0)

    submit = st.form_submit_button("Crear Cliente")

    if submitted:
        try:
            if nombre == "":
                st.warning("Debe ingresar un nombre")   
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
        except Exception as e:
            st.error(str(e))

if len(st.session_state.clientes) > 0:

    st.write("### Tabla de Clientes")
    df = pd.DataFrame(st.session_state.clientes) 
    st.dataframe(df)                              

    #FOR  --  Recorrer clientes

    st.write("### Recorrer Clientes")
    for c in st.session_state.clientes:
        st.write(f"{c['Nombre']} - {c['Edad']} - {c['Saldo']}")

    #WHILE --  Recorrido alternativo

    st.write("### Recorrido con While")
    i = 0
    while i < len(st.session_state.clientes):
        c = st.session_state.clientes[i]
        st.write(f"{c['Nombre']} - {c['Edad']} - {c['Saldo']}")
        i += 1

    # Analisis total de clientes

    contador = len(st.session_state.clientes)
    st.write(f"Total de clientes: {contador}")

    #Promedio de saldo
    promedio = calcular_promedio(st.session_state.clientes)
    st.write(f"Promedio de saldo: S/ {round(promedio, 2)}")

else:
    st.write("No hay clientes registrados")