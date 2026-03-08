import os
from io import BytesIO
from datetime import datetime

import streamlit as st

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

from mono_b64 import MONO_DATA_URI
from styles import apply_styles
from utils import download_button
from ejercicios_python import EJERCICIOS

# Streamlit uploader limit (UI). Drive soporta grande; aquí dejamos 250MB como antes.
MAX_UPLOAD_BYTES = 250 * 1024 * 1024

# Google Drive scope
SCOPES = ["https://www.googleapis.com/auth/drive"]


# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Ferran", page_icon="📚", layout="wide")
apply_styles()

# ── Session state ─────────────────────────────────────────────────────────────
if "seccion" not in st.session_state:
    st.session_state.seccion = None


def sanitize_filename(name: str) -> str:
    """Devuelve solo el nombre base del archivo eliminando separadores de ruta."""
    return os.path.basename(name).replace("..", "").strip()


def get_drive_service():
    """
    Crea un cliente Drive API con cuenta de servicio desde st.secrets["google"].
    """
    creds_dict = dict(st.secrets["google"])
    creds = service_account.Credentials.from_service_account_info(
        creds_dict,
        scopes=SCOPES,
    )
    return build("drive", "v3", credentials=creds)


def upload_to_drive(file_bytes: bytes, file_name: str):
    """
    Sube un archivo a la carpeta configurada en st.secrets["folders"]["uploads_folder_id"].
    Retorna (file_id, webViewLink).
    """
    safe_name = sanitize_filename(file_name)
    if not safe_name:
        raise ValueError("Nombre de archivo inválido.")

    folder_id = st.secrets["folders"]["uploads_folder_id"]
    service = get_drive_service()

    file_metadata = {"name": safe_name, "parents": [folder_id]}
    media = MediaIoBaseUpload(
        BytesIO(file_bytes),
        mimetype="application/octet-stream",
        resumable=True,
    )

    created = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id,webViewLink,name,createdTime")
        .execute()
    )
    return created["id"], created.get("webViewLink", "")


def list_drive_files(limit: int = 50):
    """
    Lista archivos en la carpeta configurada.
    """
    folder_id = st.secrets["folders"]["uploads_folder_id"]
    service = get_drive_service()

    results = (
        service.files()
        .list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="files(id,name,webViewLink,createdTime,size)",
            orderBy="createdTime desc",
            pageSize=limit,
        )
        .execute()
    )
    return results.get("files", [])


# ──────────────────────────────────────────────────────────────────────────────
# INTERFAZ PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────────

st.image(MONO_DATA_URI, use_column_width=True)
st.title("📚 Ferran — Recursos Académicos")
st.markdown("---")

# ── Upload a Google Drive ─────────────────────────────────────────────────────
st.subheader("⬆️ Subir archivo (Google Drive)")
st.caption("Se guardará en tu carpeta configurada de Google Drive (sin login de usuario).")

uploaded_file = st.file_uploader(
    "Selecciona un archivo para subir",
    type=None,
    help="Máximo 250 MB por archivo.",
)

if uploaded_file is not None:
    file_size_mb = uploaded_file.size / (1024 * 1024)

    if uploaded_file.size > MAX_UPLOAD_BYTES:
        st.error(f"❌ Archivo demasiado grande ({file_size_mb:.1f} MB). Máximo: 250 MB")
    else:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"📄 {uploaded_file.name} ({file_size_mb:.1f} MB)")
        with col2:
            if st.button("📤 Subir"):
                try:
                    with st.spinner("Subiendo a Google Drive..."):
                        file_bytes = uploaded_file.read()
                        file_id, link = upload_to_drive(file_bytes, uploaded_file.name)

                    st.success(f"✅ '{uploaded_file.name}' subido a Google Drive")
                    if link:
                        st.markdown(f"🔗 Abrir archivo: {link}")
                    else:
                        st.info(f"Archivo ID: {file_id}")
                except Exception as exc:
                    st.error(f"❌ Error al subir a Google Drive: {exc}")

st.markdown("---")

# ── Secciones ────────────────────────────────────────────────────────────────
st.subheader("📂 Secciones")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📘 ICS111\nAdm. Empresas", key="ics111", use_container_width=True):
        st.session_state.seccion = "ics111"

with col2:
    if st.button("📗 ICS161\nIntro. Economía", key="ics161", use_container_width=True):
        st.session_state.seccion = "ics161"

with col3:
    if st.button("📐 MATE10\nÁlgebra", key="mate10", use_container_width=True):
        st.session_state.seccion = "mate10"

with col4:
    if st.button("🐍 Ejercicios\nPython", key="python", use_container_width=True):
        st.session_state.seccion = "python"

PDF_PATHS = {
    "ics111": ("pdfs/ics111_administracion_empresas.pdf", "ICS111 - Administración de Empresas"),
    "ics161": ("pdfs/ics161_introduccion_economia.pdf", "ICS161 - Introducción a la Economía"),
    "mate10": ("pdfs/mate10_algebra_geometria.pdf", "MATE10 - Álgebra y Geometría"),
}

if st.session_state.seccion in PDF_PATHS:
    path, title = PDF_PATHS[st.session_state.seccion]
    st.markdown(f"### {title}")
    download_button(path, title)

elif st.session_state.seccion == "python":
    st.markdown("### 🐍 Ejercicios Python")
    for categoria in EJERCICIOS:
        with st.expander(f"{categoria['icono']} {categoria['categoria']}"):
            for ej in categoria["ejercicios"]:
                st.markdown(f"**{ej['titulo']}**")
                st.info(ej["enunciado"])
                if ej.get("ejemplo"):
                    st.code(ej["ejemplo"], language="text")
                st.code(ej["codigo"], language="python")
                st.markdown("---")

st.markdown("---")

if st.button("🗂️ Ver Recién Subidos", key="recientes", use_container_width=True):
    st.session_state.seccion = "recientes"

if st.session_state.seccion == "recientes":
    st.subheader("📥 Archivos subidos recientemente (Google Drive)")

    try:
        archivos = list_drive_files(limit=50)
        if not archivos:
            st.info("📭 No hay archivos en la carpeta todavía.")
        else:
            for f in archivos:
                name = f.get("name", "archivo")
                created = f.get("createdTime", "")
                link = f.get("webViewLink", "")
                fecha = created[:10] if created else ""

                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.markdown(f"📄 **{name}** {f'— {fecha}' if fecha else ''}")
                with col_b:
                    if link:
                        st.markdown(link)
                    else:
                        st.caption("Sin link")
    except Exception as exc:
        st.error(f"❌ Error listando Google Drive: {exc}")
