from supabase import create_client, Client
import streamlit as st


@st.cache_resource
def get_supabase_client() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


def insertar_cliente(cliente_dict: dict) -> dict:
    try:
        supabase = get_supabase_client()
        response = (
            supabase
            .schema("bronze")   # ← schema ANTES de table
            .table("clientes")
            .insert(cliente_dict)
            .execute()
        )
        return response.data[0] if response.data else {}
    except Exception as e:
        raise RuntimeError(f"Error al insertar cliente: {e}")


def obtener_clientes() -> list:
    try:
        supabase = get_supabase_client()
        response = (
            supabase
            .schema("bronze")   # ← schema ANTES de table
            .table("clientes")
            .select("*")
            .execute()
        )
        return response.data
    except Exception as e:
        raise RuntimeError(f"Error al obtener clientes: {e}")