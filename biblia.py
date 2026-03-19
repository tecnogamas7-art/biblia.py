import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA (Debe ser la primera instrucción)
st.set_page_config(page_title="Biblia Digital Pro", page_icon="📖", layout="centered")

# 2. ESTILO VISUAL MINIMALISTA (CSS corregido)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .biblia-contenedor { 
        font-family: 'Georgia', serif; 
        font-size: 1.2rem; 
        line-height: 1.8; 
        color: #2c3e50; 
        padding: 30px; 
        background-color: white; 
        border-radius: 15px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #e1e4e8;
    }
    .versiculo-num { color: #8e44ad; font-weight: bold; font-size: 0.9rem; vertical-align: super; margin-right: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. TÍTULO Y ENCABEZADO
st.title("📖 Biblia Sistematizada")
st.caption("Lectura simplificada • Reina Valera 1960")

# 4. BASE DE DATOS DE LOS 66 LIBROS
biblia_data = {
    "Antiguo Testamento": [
        "Génesis", "Éxodo", "Levítico", "Números", "Deuteronomio", "Josué", "Jueces", "Rut", 
        "1 Samuel", "2 Samuel", "1 Reyes", "2 Reyes", "1 Crónicas", "2 Crónicas", "Esdras", 
        "Nehemías", "Ester", "Job", "Salmos", "Proverbios", "Eclesiastés", "Cantares", 
        "Isaías", "Jeremías", "Lamentaciones", "Ezequiel", "Daniel", "Oseas", "Joel", 
        "Amós", "Abdías", "Jonás", "Miqueas", "Nahúm", "Habacuc", "Sofonías", "Hageo", 
        "Zacarías", "Malaquías"
    ],
    "Nuevo Testamento": [
        "Mateo", "Marcos", "Lucas", "Juan", "Hechos", "Romanos", "1 Corintios", "2 Corintios", 
        "Gálatas", "Efesios", "Filipenses", "Colosenses", "1 Tesalonicenses", "2 Tesalonicenses", 
        "1 Timoteo", "2 Timoteo", "Tito", "Filemón", "Hebreos", "Santiago", "1 Pedro", 
        "2 Pedro", "1 Juan", "2 Juan", "3 Juan", "Judas", "Apocalipsis"
    ]
}

# 5. BUSCADOR SISTEMATIZADO
with st.container():
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        testamento_sel = st.selectbox("Testamento", list(biblia_data.keys()))
    with col2:
        libro_sel = st.selectbox("Libro", biblia_data[testamento_sel])
    with col3:
        capitulo_sel = st.number_input("Cap.", min_value=1, value=1, step=1)

st.divider()

# 6. VISTA DEL PASAJE (Estructura para el texto)
st.subheader(f"{libro_sel} {capitulo_sel}")

# Nota: Aquí es donde conectaremos la base de datos real en el siguiente paso.
with st.container():
    st.markdown(f"""
    <div class="biblia-contenedor">
        <span class="versiculo-num">1</span> En el principio creó Dios los cielos y la tierra.<br>
        <span class="versiculo-num">2</span> Y la tierra estaba desordenada y vacía, y las tinieblas estaban sobre la faz del abismo, y el Espíritu de Dios se movía sobre la faz de las aguas.<br>
        <span class="versiculo-num">3</span> Y dijo Dios: Sea la luz; y fue la luz.
    </div>
    """, unsafe_allow_html=True)

# 7. BARRA LATERAL (Funciones adicionales)
st.sidebar.header("🔍 Herramientas")
buscar_palabra = st.sidebar.text_input("Buscar por palabra clave:")

if buscar_palabra:
    st.sidebar.info(f"Buscando '{buscar_palabra}' en {libro_sel}...")

st.sidebar.markdown("---")
st.sidebar.write("✨ **Inspiración:**")
st.sidebar.success("'Lámpara es a mis pies tu palabra, y lumbrera a mi camino.' - Salmos 119:105")

# Pie de página
st.markdown("---")
st.markdown("<center><small>Desarrollado para estudio bíblico sistemático</small></center>", unsafe_allow_html=True)
