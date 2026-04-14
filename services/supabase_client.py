from supabase import create_client
import streamlit as st

# Crear Cliente
def get_supabase_client():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

# Insertar datos en schema Bronze
def insertar_cliente(cliente_dict):
    supabase = get_supabase_client()

    response = (
        supabase
        .table("clientes")
        .schema("bronze")
        .insert(cliente_dict)
        .execute()
    )

    return response

# Listar desde la base de datos
def obtener_clientes():
    supabase = get_supabase_client()

    response = (
        supabase
        .table("clientes")
        .schema("bronze")
        .select("*")
        .execute()
    )

    return response.data