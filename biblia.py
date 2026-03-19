import streamlit as st
import pandas as pd
import json
import urllib.request

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="Biblia Reina Valera 1960", page_icon="📖", layout="centered")

# URL del archivo JSON de la Biblia Reina Valera 1960
BIBLE_URL = "https://raw.githubusercontent.com"

@st.cache_data
def cargar_biblia():
    try:
        with urllib.request.urlopen(BIBLE_URL) as url:
            data = json.loads(url.read().decode())
            return data
    except Exception as e:
        st.error(f"Error al cargar la Biblia: {e}")
        return None

biblia_full = cargar_biblia()

# 2. ESTILO VISUAL
st.markdown("""
    <style>
    .texto-biblico { 
        font-family: 'Georgia', serif; font-size: 1.25rem; line-height: 1.8; 
        color: #1a1a1a; padding: 25px; background-color: #ffffff; 
        border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #2c3e50;
    }
    .v-num { color: #8e44ad; font-weight: bold; font-size: 0.85rem; margin-right: 8px; vertical-align: top; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Biblia Reina Valera 1960")

if biblia_full:
    # 3. SELECTORES DINÁMICOS
    # Extraemos nombres de libros
    nombres_libros = [libro['book'] for libro in biblia_full]
    
    col1, col2 = st.columns([3, 1])
    with col1:
        libro_sel = st.selectbox("Seleccione el Libro", nombres_libros)
    
    # Obtener el objeto del libro seleccionado
    libro_obj = next(item for item in biblia_full if item["book"] == libro_sel)
    total_capitulos = len(libro_obj['chapters'])
    
    with col2:
        capitulo_sel = st.number_input("Cap.", min_value=1, max_value=total_capitulos, value=1)

    st.divider()

    # 4. MOSTRAR TEXTO DEL CAPÍTULO
    st.subheader(f"{libro_sel} {capitulo_sel}")
    
    # Los capítulos en el JSON son arreglos de versículos (índice empieza en 0)
    versiculos = libro_obj['chapters'][capitulo_sel - 1]
    
    contenido_html = "<div class='texto-biblico'>"
    for i, texto in enumerate(versiculos):
        contenido_html += f"<span class='v-num'>{i+1}</span> {texto}<br><br>"
    contenido_html += "</div>"
    
    st.markdown(contenido_html, unsafe_allow_html=True)

    # 5. BUSCADOR LATERAL
    st.sidebar.header("🔍 Buscador")
    palabra = st.sidebar.text_input("Buscar palabra en este libro:")
    if palabra:
        st.sidebar.write(f"Resultados para '{palabra}':")
        for num_cap, cap in enumerate(libro_obj['chapters']):
            for num_ver, ver in enumerate(cap):
                if palabra.lower() in ver.lower():
                    st.sidebar.markdown(f"**Cap {num_cap+1}:{num_ver+1}**\n{ver}")
else:
    st.warning("Cargando base de datos bíblica... Por favor, espere.")

