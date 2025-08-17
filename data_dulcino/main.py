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

