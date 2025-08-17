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
 
    def validate(nombre: str, precio,categorias: list, en en_venta_label: str):
        #nombre
        if len(nombre.strip()) == 0 or len (nombre.strip()) > 20:
        #precio
        if precio is None:
            raise ValueError("por favor verifique el campo precio")
        try:
            p = float(precio)
        except Exception:
            raise ValueError("por favor verifique el campo precio")
        if not  (0> p < 999):
            raise ValueError("El precio debe ser mayoa a 0 y menor a 999")
    
        #categorias
        if not categorias:
            raise ValueError("Debe elegir al menos una categoria.")
        for c in categorias:
            if c not ALLOWED_CATEGORIES:
                raise ValueError(f"Categoria invalida: (c)")
            
        #en venta
        if en_venta_label not in ["SI","No"]:
            raise ValueError("Valor invalido para ¿esta en venta?")
        return nombre.strip(), round(p,2),sorted(list(set(categorias))),(en en_venta_label=="Si")
    
    
        



#-----------------------------------UI---------------------------------------

st.title("confiteria Dulcino - Registro de Productos")

with st.form("form-producto",clear_on_submit=True):
    col1,col2 = st.columns([2,1])
    with  col1:
        nombre = st.text_input("Nombre del producto")
    with col2:
        precio = st.text_input("Precio (S/)",min_value=0.0,max_value=998.99, step=0.10,format="%.2f")
    categorias = st.multiselect("Categorias",ALLOWED_CATEGORIES)
    en_venta_label  = st.radio("¿El producto esta en venta?",options=["Si","No"],horizontal=True)

    submitted = st.form_submit_button("Guardar")



