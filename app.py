




import streamlit as st
from styles import apply_styles
from utils import list_pdfs, download_button
import pytz
from datetime import datetime


# Configuración de página
st.set_page_config(page_title="Repositorio de Guías", layout="wide")
apply_styles()

st.title("📚 Descarga de Material")

# Secciones requeridas
secciones = ["Python", "Economía", "Matemáticas", "Administración"]
seleccion = st.sidebar.radio("Selecciona una categoría:", secciones)

st.header(f"Guías de {seleccion}")

# Mapeo de carpetas (asegúrate de que existan en tu repo/PC)
folder_map = {
    "Python": "pdfs/python",
    "Economía": "pdfs/economia",
    "Matemáticas": "pdfs/mate",
    "Administración": "pdfs/administracion"
}

folder_path = folder_map[seleccion]
files = list_pdfs(folder_path)

if files:
    for file in files:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"📄 {file}")
        with col2:
            download_button(f"{folder_path}/{file}", file)
else:
    st.info("Aún no hay archivos en esta sección.")
