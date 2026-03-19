import streamlit as st

# 1. CONFIGURACIÓN (Debe ir al inicio)
st.set_page_config(page_title="Biblia Digital", page_icon="📖", layout="centered")

# 2. ESTILO CORREGIDO
st.markdown("""
    <style>
    .biblia-contenedor { 
        font-family: 'Georgia', serif; 
        font-size: 1.2rem; 
        line-height: 1.8; 
        color: #2c3e50; 
        padding: 20px; 
        background-color: white; 
        border-radius: 10px; 
        border: 1px solid #ddd;
    }
    .v-num { color: #8e44ad; font-weight: bold; font-size: 0.8rem; margin-right: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. TÍTULO
st.title("📖 Biblia Sistematizada")

# 4. DATOS COMPLETOS
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

# 5. BUSCADOR VERTICAL (Más estable para evitar distorsión)
testamento_sel = st.selectbox("1. Elija el Testamento", list(biblia_data.keys()))
libro_sel = st.selectbox("2. Elija el Libro", biblia_data[testamento_sel])
capitulo_sel = st.number_input("3. Ingrese el Capítulo", min_value=1, value=1, step=1)

st.divider()

# 6. VISTA DEL PASAJE
st.subheader(f"{libro_sel} {capitulo_sel}")

st.markdown(f"""
<div class="biblia-contenedor">
    <span class="v-num">1</span> En el principio creó Dios los cielos y la tierra.<br>
    <span class="v-num">2</span> Y la tierra estaba desordenada y vacía, y las tinieblas estaban sobre la faz del abismo...<br>
    <span class="v-num">3</span> Y dijo Dios: Sea la luz; y fue la luz.
</div>
""", unsafe_allow_html=True)

# 7. BARRA LATERAL
st.sidebar.header("🔍 Herramientas")
buscar = st.sidebar.text_input("Buscar palabra clave:")
if buscar:
    st.sidebar.info(f"Buscando '{buscar}'...")
