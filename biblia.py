import streamlit as st

# 1. Configuración de la página (DEBE SER LA PRIMERA LÍNEA DE STREAMLIT)
st.set_page_config(page_title="Biblia Digital Pro", page_icon="📖", layout="centered")

# 2. Estilo visual corregido
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .biblia-texto { 
        font-family: 'Georgia', serif; 
        font-size: 20px; 
        line-height: 1.6; 
        color: #1a1a1a; 
        padding: 20px; 
        background: white; 
        border-radius: 10px; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.05); 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Biblia Sistematizada")
st.caption("Lectura simplificada y navegación rápida")

# Estructura de la Biblia
biblia_data = {
    "Antiguo Testamento": ["Génesis", "Éxodo", "Levítico", "Números", "Deuteronomio", "Salmos", "Proverbios"],
    "Nuevo Testamento": ["Mateo", "Marcos", "Lucas", "Juan", "Hechos", "Romanos", "Apocalipsis"]
}

# --- BUSCADOR SISTEMATIZADO ---
with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        testamento = st.selectbox("Testamento", list(biblia_data.keys()))
    with col2:
        libro = st.selectbox("Libro", biblia_data[testamento])
    with col3:
        capitulo = st.number_input("Cap.", min_value=1, value=1, step=1)

st.divider()

# --- VISTA DEL PASAJE ---
st.subheader(f"{libro} {capitulo}")

with st.container():
    st.markdown(f"""
    <div class="biblia-texto">
        <b>1</b> En el principio creó Dios los cielos y la tierra.<br>
        <b>2</b> Y la tierra estaba desordenada y vacía, y las tinieblas estaban sobre la faz del abismo...<br>
        <b>3</b> Y dijo Dios: Sea la luz; y fue la luz.
    </div>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
st.sidebar.header("🔍 Buscador Rápido")
tema = st.sidebar.text_input("Buscar por palabra:")
if tema:
    st.sidebar.info(f"Buscando '{tema}'...")

st.sidebar.markdown("---")
st.sidebar.write("📌 **Versículo del día:**")
st.sidebar.warning("'Lámpara es a mis pies tu palabra, y lumbrera a mi camino.' - Salmos 119:105")
