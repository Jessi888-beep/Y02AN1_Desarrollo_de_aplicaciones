import os
import pandas as pd
import streamlit as st
from datetime import datetime

DATA_DIR = "datos_sinteticos"
CSV_PATH = os.path.join(DATA_DIR,"productos.csv")

ALLOWED_CATEGORIES = [
    "Chocolates","Caramelos","Mashmelos","Galletas","Salados", "Gomas de mascar"
    ]

st.title("Confiteria Dulcino")

def ensure_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_df() -> pd.DataFrame:
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH,encoding="utf-8")
        return df
    return pd.DataFrame(columns=["nombre","precio","categorias","en venta","ts"])


#-----------------------------------UI---------------------------------------

st.title("confiteria Dulcino - Registro de Productos")

with st.form("form-producto",clear_on_submit=True):
    coll,col2 = st.columns([2,1])
    with  coll:
        nombre = st.text_input("Nombre del producto")
    with coll2:
        precio = st.text_input("Precio (S/)",min_value=0.0,max_value=998.99, step=0.10,format="%.2f")
    categorias = st.multiselect("Categorias",ALLOWED_CATEGORIES)
    en_venta_label  = st.radio("¿El producto esta en venta?",options=["Si","No"],horizontal=True)

    submitted = st.form_submit_button("Guardar")


