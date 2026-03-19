import streamlit as st
from datetime import datetime

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Biblia Digital Pro", page_icon="📖", layout="centered")

# 2. BASE DE DATOS LOCAL (Ejemplo de funcionamiento real)
# Aquí puedes ir pegando los textos de cada capítulo
TEXTOS_BIBLIA = {
    "Génesis": {
        1: ["En el principio creó Dios los cielos y la tierra.", 
            "Y la tierra estaba desordenada y vacía, y las tinieblas estaban sobre la faz del abismo.",
            "Y dijo Dios: Sea la luz; y fue la luz."]
    },
    "Salmos": {
        23: ["Jehová es mi pastor; nada me faltará.",
             "En lugares de delicados pastos me hará descansar.",
             "Junto a aguas de reposo me pastoreará."]
    },
    "Juan": {
        1: ["En el principio era el Verbo, y el Verbo era con Dios, y el Verbo era Dios.",
            "Este era en el principio con Dios.",
            "Todas las cosas por él fueron hechas, y sin él nada de lo que ha sido hecho, fue hecho."]
    }
}

# 3. ESTILO VISUAL PROFESIONAL
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .biblia-box { 
        font-family: 'Georgia', serif; font-size: 1.3rem; line-height: 1.8; 
        color: #1a1a1a; padding: 30px; background-color: white; 
        border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-top: 5px solid #2c3e50;
    }
    .v-num { color: #8e44ad; font-weight: bold; font-size: 0.9rem; margin-right: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 4. ENCABEZADO
st.title("📖 Biblia Reina Valera 1960")
st.caption("Lectura Sistematizada y Simplificada")

# 5. SELECTORES DE NAVEGACIÓN
libros_disponibles = [
    "Génesis", "Éxodo", "Levítico", "Números", "Deuteronomio", "Salmos", "Proverbios", 
    "Mateo", "Marcos", "Lucas", "Juan", "Hechos", "Romanos", "Apocalipsis"
]

col1, col2 = st.columns([2, 1])
with col1:
    libro_sel = st.selectbox("📖 Libro", libros_disponibles)
with col2:
    cap_sel = st.number_input("Capítulo", min_value=1, value=1 if libro_sel != "Salmos" else 23)

st.divider()

# 6. LÓGICA DE VISUALIZACIÓN
st.subheader(f"{libro_sel} {cap_sel}")

# Verificamos si tenemos el texto en nuestra base de datos
if libro_sel in TEXTOS_BIBLIA and cap_sel in TEXTOS_BIBLIA[libro_sel]:
    versiculos = TEXTOS_BIBLIA[libro_sel][cap_sel]
    
    contenido_html = "<div class='biblia-box'>"
    for i, texto in enumerate(versiculos):
        contenido_html += f"<span class='v-num'>{i+1}</span> {texto}<br><br>"
    contenido_html += "</div>"
    
    st.markdown(contenido_html, unsafe_allow_html=True)
else:
    # Mensaje si el capítulo aún no está cargado en el código
    st.info(f"El texto de {libro_sel} {cap_sel} está siendo procesado para la versión digital.")
    st.markdown("""
    <div class='biblia-box'>
        <span class='v-num'>1</span> [Texto en preparación para la lectura sistematizada...]
    </div>
    """, unsafe_allow_html=True)

# 7. BARRA LATERAL
st.sidebar.header("🔍 Herramientas")
st.sidebar.write("📌 **Versículo de hoy:**")
st.sidebar.warning("'Todo lo puedo en Cristo que me fortalece.' - Filipenses 4:13")

# Pie de página
st.markdown("---")
st.markdown(f"<center><small>© {datetime.now().year} Biblia Digital Sistematizada</small></center>", unsafe_allow_html=True)
