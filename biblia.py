import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Biblia Digital", page_icon="📖", layout="centered")

# 2. BASE DE DATOS INTEGRADA (Textos reales RVR1960)
# Esta estructura permite que la app funcione sin archivos externos
BIBLIA_LOCAL = {
    "Salmos": {
        23: ["Jehová es mi pastor; nada me faltará.", "En lugares de delicados pastos me hará descansar; Junto a aguas de reposo me pastoreará.", "Confortará mi alma; Me guiará por sendas de justicia por amor de su nombre."],
        91: ["El que habita al abrigo del Altísimo Morará bajo la sombra del Omnipotente.", "Diré yo a Jehová: Esperanza mía, y castillo mío; Mi Dios, en quien confiaré.", "Él te librará del lazo del cazador, De la peste destructora."],
        121: ["Alzaré mis ojos a los montes; ¿De dónde vendrá mi socorro?", "Mi socorro viene de Jehová, Que hizo los cielos y la tierra.", "No dará tu pie al resbaladero, Ni se dormirá el que te guarda."]
    },
    "Juan": {
        1: ["En el principio era el Verbo, y el Verbo era con Dios, y el Verbo era Dios.", "Este era en el principio con Dios.", "Todas las cosas por él fueron hechas, y sin él nada de lo que ha sido hecho, fue hecho.", "En él estaba la vida, y la vida era la luz de los hombres."],
        3: ["Había un hombre de los fariseos que se llamaba Nicodemo, un principal entre los judíos.", "Este vino a Jesús de noche, y le dijo: Rabí, sabemos que has venido de Dios como maestro...", "Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito..."]
    }
}

# 3. ESTILO VISUAL
st.markdown("""
    <style>
    .texto-biblico { 
        font-family: 'Georgia', serif; font-size: 1.3rem; line-height: 1.8; 
        color: #1a1a1a; padding: 25px; background-color: white; 
        border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-left: 5px dotted #2c3e50;
    }
    .v-num { color: #8e44ad; font-weight: bold; font-size: 0.9rem; margin-right: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Biblia Sistematizada")

# 4. SELECTORES
libros_disp = ["Salmos", "Juan", "Génesis", "Mateo", "Romanos", "Apocalipsis"]
col1, col2 = st.columns([2, 1])

with col1:
    libro_sel = st.selectbox("Libro", libros_disp)
with col2:
    # Ajustamos capítulos según lo que tenemos cargado
    caps_lista = list(BIBLIA_LOCAL.get(libro_sel, {1: []}).keys())
    cap_sel = st.selectbox("Cap.", caps_lista if caps_lista else [1])

st.divider()

# 5. MOSTRAR TEXTO
st.subheader(f"{libro_sel} {cap_sel}")

if libro_sel in BIBLIA_LOCAL and cap_sel in BIBLIA_LOCAL[libro_sel]:
    versiculos = BIBLIA_LOCAL[libro_sel][cap_sel]
    html = "<div class='texto-biblico'>"
    for i, texto in enumerate(versiculos):
        html += f"<span class='v-num'>{i+1}</span> {texto}<br><br>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
else:
    st.info(f"El texto de {libro_sel} {cap_sel} está disponible en la versión impresa. Pronto lo sincronizaremos aquí.")
    st.image("https://images.unsplash.com", caption="Escudriñad las Escrituras")

# 6. BARRA LATERAL
st.sidebar.header("🔍 Navegación")
st.sidebar.write("📌 **Sugerencias de hoy:**")
st.sidebar.button("Leer Salmo 23", on_click=lambda: st.toast("Cargando Salmo 23..."))
st.sidebar.button("Leer Juan 3", on_click=lambda: st.toast("Cargando Juan 3..."))
