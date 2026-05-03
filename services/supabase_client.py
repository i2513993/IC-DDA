from supabase import create_client
import streamlit as st

def get_supabase_client():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

def insertar_cliente(cliente_dict):
    supabase = get_supabase_client()
    response = (
        supabase
        .schema("bronze")
        .table("clientes")
        .insert(cliente_dict)
        .execute()
    )
    return response

def obtener_clientes():
    supabase = get_supabase_client()
    response = (
        supabase
        .schema("bronze")
        .table("clientes")
        .select("*")
        .execute()
    )
    return response.data

def actualizar_cliente(id, cliente_dict):
    supabase = get_supabase_client()
    response = (
        supabase
        .schema("bronze")
        .table("clientes")
        .update(cliente_dict)
        .eq("id", id)
        .execute()
    )
    return response

def eliminar_cliente(id):
    supabase = get_supabase_client()
    response = (
        supabase
        .schema("bronze")
        .table("clientes")
        .delete()
        .eq("id", id)
        .execute()
    )
    return response