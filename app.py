import os
import streamlit as st
from github import Github, GithubException, UnknownObjectException

from mono_b64 import MONO_DATA_URI
from styles import apply_styles
from utils import download_button
from ejercicios_python import EJERCICIOS

# Maximum allowed upload size (250 MB)
MAX_UPLOAD_BYTES = 250 * 1024 * 1024

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Ferran", page_icon="📚", layout="wide")
apply_styles()

# ── Session state ─────────────────────────────────────────────────────────────
if "seccion" not in st.session_state:
    st.session_state.seccion = None

# ── Helper: sanitize filename ────────────────────────────────────────────────
def sanitize_filename(name: str) -> str:
    """Devuelve solo el nombre base del archivo eliminando separadores de ruta."""
    return os.path.basename(name).replace("..", "").strip()

# ── Helper: upload a file to GitHub ──────────────────────────────────────────
def upload_to_github(file_bytes: bytes, file_name: str) -> bool:
    """Sube un archivo a la carpeta 'recién subidos' del repositorio de GitHub."""
    safe_name = sanitize_filename(file_name)
    if not safe_name:
        st.error("Nombre de archivo inválido.")
        return False
    try:
        token = st.secrets["github"]["token"]
        repo_name = st.secrets["github"]["repo"]
        g = Github(token)
        repo = g.get_repo(repo_name)
        path = f"recién subidos/{safe_name}"
        try:
            existing = repo.get_contents(path)
            repo.update_file(
                path=path,
                message=f"Actualizar {safe_name}",
                content=file_bytes,
                sha=existing.sha,
            )
            st.success(f"✅ '{safe_name}' actualizado en GitHub")
        except UnknownObjectException:
            repo.create_file(
                path=path,
                message=f"Agregar {safe_name}",
                content=file_bytes,
            )
            st.success(f"✅ '{safe_name}' subido a GitHub")
        return True
    except GithubException as exc:
        st.error(f"❌ Error GitHub: {exc.data.get('message', exc)}")
        return False
    except KeyError:
        st.error("❌ Secrets no configurados correctamente")
        return False
    except Exception as exc:
        st.error(f"❌ Error: {str(exc)}")
        return False

# ── Helper: list files in 'recién subidos' ────────────────────────────────────
def list_recent_uploads():
    """Obtiene archivos de 'recién subidos'."""
    try:
        token = st.secrets["github"]["token"]
        repo_name = st.secrets["github"]["repo"]
        g = Github(token)
        repo = g.get_repo(repo_name)
        contents = repo.get_contents("recién subidos")
        return contents if isinstance(contents, list) else [contents]
    except UnknownObjectException:
        return []
    except GithubException as exc:
        st.warning(f"No acceso a carpeta: {exc.data.get('message', exc)}")
        return []
    except Exception as exc:
        st.error(f"Error: {exc}")
        return []

# ──────────────────────────────────────────────────────────────────────────────
# INTERFAZ PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────────

# Imagen de Fido Dido
st.image(MONO_DATA_URI, use_column_width=True)
st.title("📚 Ferran — Recursos Académicos")
st.markdown("---")

# Sección de UPLOAD
st.subheader("⬆️ Subir archivo al repositorio")
uploaded_file = st.file_uploader(
    "Selecciona un archivo para subir a *recién subidos*",
    type=None,
    help="Máximo 250 MB por archivo"
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
                file_bytes = uploaded_file.read()
                upload_to_github(file_bytes, uploaded_file.name)

st.markdown("---")

# Secciones principales
st.subheader("📂 Secciones")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📘 ICS111\nAdm. Empresas", key="ics111"):
        st.session_state.seccion = "ics111"

with col2:
    if st.button("📗 ICS161\nIntro. Economía", key="ics161"):
        st.session_state.seccion = "ics161"

with col3:
    if st.button("📐 MATE10\nÁlgebra", key="mate10"):
        st.session_state.seccion = "mate10"

with col4:
    if st.button("🐍 Ejercicios\nPython", key="python"):
        st.session_state.seccion = "python"

# Renderizar sección seleccionada
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

# Botón "Ver Recién Subidos"
if st.button("🗂️ Ver Recién Subidos", key="recientes"):
    st.session_state.seccion = "recientes"

if st.session_state.seccion == "recientes":
    st.subheader("📥 Archivos subidos recientemente")
    archivos = list_recent_uploads()
    if archivos:
        for archivo in archivos:
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown(f"📄 **{archivo.name}**")
            with col_b:
                st.download_button(
                    label="⬇️ Descargar",
                    data=archivo.decoded_content,
                    file_name=archivo.name,
                    key=f"dl_{archivo.sha}",
                )
    else:
        st.info("📭 No hay archivos en la carpeta 'recién subidos' todavía.")
