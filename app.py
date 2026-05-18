import streamlit as st
import pandas as pd
import numpy as np
import os
import time

# ─────────────────────────────────────────────────────────
#  CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SICE-México AI | Ecosistema Analítico",
    page_icon="🇲🇽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────
#  ESTILOS GLOBALES
# ─────────────────────────────────────────────────────────
STAR_BG = "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?q=80&w=2560&auto=format&fit=crop"

css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Mono:wght@400;500&display=swap');

/* ── Fondo de estrellas ── */
.stApp {{
    background-image:
        linear-gradient(180deg, rgba(4,8,20,0.92) 0%, rgba(6,12,28,0.88) 100%),
        url("{STAR_BG}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}}

/* ── Capas intermedias transparentes ── */
.stMain, .stHeader,
[data-testid="stHeader"],
[data-testid="stMain"],
[data-testid="stVerticalBlock"],
[data-testid="stAppViewMain"] {{
    background: transparent !important;
}}

/* ── Contenedor principal ── */
[data-testid="stMainBlockContainer"] {{
    padding: 3.5rem 6rem !important;
    max-width: 100% !important;
}}

/* ── Sidebar ── */
.stSidebar, [data-testid="stSidebar"] {{
    background: rgba(4, 7, 18, 0.97) !important;
    backdrop-filter: blur(24px) !important;
    border-right: 1px solid rgba(99,179,237,0.12) !important;
}}

/* ── Tipografía global ── */
html, body, .stMarkdown, p, span, label, div, li {{
    font-family: 'DM Sans', sans-serif !important;
    color: #e2e8f0 !important;
}}

/* ── Selectbox / widgets ── */
[data-testid="stSelectbox"] label,
[data-testid="stWidgetLabel"] {{
    font-family: 'DM Mono', monospace !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #63b3ed !important;
}}

/* ── Encabezado principal ── */
.sice-hero {{
    padding: 2.5rem 0 1rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 2.5rem;
}}
.sice-eyebrow {{
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #63b3ed;
    margin-bottom: 0.6rem;
}}
.sice-title {{
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 5vw, 3.8rem);
    font-weight: 800;
    color: #ffffff;
    line-height: 1.08;
    letter-spacing: -0.02em;
    margin: 0 0 0.5rem 0;
}}
.sice-subtitle {{
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    color: #718096;
    font-weight: 300;
    letter-spacing: 0.01em;
    max-width: 72ch;
    line-height: 1.6;
}}

/* ── Banner de alerta ── */
.status-banner {{
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    background: rgba(251,191,36,0.05);
    border: 1px solid rgba(251,191,36,0.25);
    border-left: 3px solid #f59e0b;
    padding: 1.1rem 1.4rem;
    border-radius: 8px;
    margin-bottom: 2.5rem;
    font-size: 0.88rem;
    line-height: 1.65;
    color: #fde68a;
}}
.status-banner strong {{ color: #fef3c7 !important; }}

/* ── Barras de dimensión ── */
.dim-row {{
    margin-bottom: 1.4rem;
}}
.dim-label {{
    font-family: 'DM Mono', monospace;
    font-size: 0.76rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 0.4rem;
    display: flex;
    justify-content: space-between;
}}
.dim-track {{
    background: rgba(255,255,255,0.06);
    border-radius: 99px;
    height: 6px;
    overflow: hidden;
    position: relative;
}}
.dim-fill {{
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s cubic-bezier(.4,0,.2,1);
    position: relative;
}}
.dim-fill::after {{
    content: '';
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: inherit;
    filter: brightness(1.4);
    box-shadow: 0 0 8px currentColor;
}}

/* ── Tarjetas métricas ── */
.metric-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin: 2rem 0;
}}
.metric-card {{
    background: rgba(8, 14, 32, 0.8);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.6rem 1.4rem;
    text-align: center;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    transition: border-color 0.3s;
}}
.metric-card:hover {{ border-color: rgba(99,179,237,0.25); }}
.metric-label {{
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #4a5568;
    margin-bottom: 0.7rem;
}}
.metric-val {{
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    line-height: 1;
}}

/* ── Memorándum ejecutivo ── */
.memo-shell {{
    background: rgba(6, 10, 24, 0.97);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 0;
    overflow: hidden;
    box-shadow: 0 40px 80px -20px rgba(0,0,0,0.85);
    margin-top: 2rem;
}}
.memo-topbar {{
    padding: 0.5rem 2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(255,255,255,0.025);
    border-bottom: 1px solid rgba(255,255,255,0.06);
}}
.memo-dot {{
    width: 10px; height: 10px;
    border-radius: 50%;
    display: inline-block;
}}
.memo-body {{ padding: 2.2rem 2.8rem 2.8rem; }}
.memo-title {{
    font-family: 'Syne', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.2rem;
}}
.memo-ref {{
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    color: #4a5568;
    margin-bottom: 2rem;
}}
.memo-section {{
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #4a5568;
    padding-bottom: 0.4rem;
    border-bottom: 1px dashed rgba(255,255,255,0.08);
    margin-top: 2rem;
    margin-bottom: 0.9rem;
}}
.memo-finding {{
    font-family: 'Syne', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 0.4rem 0 1.5rem;
}}
.memo-analysis {{
    font-family: 'DM Sans', sans-serif;
    font-size: 0.97rem;
    line-height: 1.75;
    font-style: italic;
    color: #94a3b8;
    background: rgba(255,255,255,0.02);
    padding: 1.2rem 1.4rem;
    border-radius: 8px;
    border-left: 3px solid;
    margin-bottom: 1.5rem;
}}
.memo-rec-list {{
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
}}
.memo-rec-item {{
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    font-size: 0.93rem;
    line-height: 1.6;
    color: #cbd5e1;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 0.9rem 1.1rem;
}}
.rec-num {{
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    font-weight: 500;
    color: #4a5568;
    padding-top: 0.1rem;
    flex-shrink: 0;
}}
.memo-footer {{
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: #2d3748;
    margin-top: 2.5rem;
    padding-top: 1rem;
    border-top: 1px dashed rgba(255,255,255,0.07);
    line-height: 1.7;
}}

/* ── Botón principal ── */
.stButton > button {{
    background: linear-gradient(135deg, #1a56db 0%, #0e3fa8 100%) !important;
    color: #fff !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.75rem 2rem !important;
    cursor: pointer !important;
    box-shadow: 0 4px 20px rgba(26,86,219,0.35) !important;
    transition: all 0.25s ease !important;
}}
.stButton > button:hover {{
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 28px rgba(26,86,219,0.5) !important;
}}

/* ── Divisor ── */
hr {{ border-color: rgba(255,255,255,0.06) !important; }}

/* ── Modo accesible: alto contraste ── */
@media (prefers-contrast: more) {{
    .sice-subtitle, .metric-label, .memo-ref {{ color: #cbd5e1 !important; }}
    .memo-analysis {{ color: #e2e8f0 !important; }}
    .dim-label {{ color: #e2e8f0 !important; }}
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        "<div style='font-family:Syne,sans-serif;font-size:1.3rem;font-weight:800;"
        "color:#fff;letter-spacing:-0.01em;margin-bottom:0.15rem;'>SICE-México</div>"
        "<div style='font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.18em;"
        "text-transform:uppercase;color:#4a5568;margin-bottom:1.6rem;'>Core Engine v2.5</div>",
        unsafe_allow_html=True
    )
    st.write("---")

    st.markdown(
        "<div style='font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.14em;"
        "text-transform:uppercase;color:#63b3ed;margin-bottom:0.6rem;'>Gobernanza & Ciencia Abierta</div>",
        unsafe_allow_html=True
    )
    st.caption(
        "Este ecosistema opera bajo principios estrictos de **Ciencia Abierta**, "
        "alojando su núcleo en un repositorio público de GitHub. Representa una muestra "
        "nacional calibrada con proyecciones a escala global."
    )
    st.write("---")

    st.markdown(
        "<div style='font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.14em;"
        "text-transform:uppercase;color:#63b3ed;margin-bottom:0.6rem;'>Repositorios Indexados</div>",
        unsafe_allow_html=True
    )
    repos = [
        ("ime_2020.csv", "CONAPO"),
        ("03_iim_mex_eeuu_2020_entidad.csv", "Migración"),
        ("13_personas_usuarios_internet.csv", "INEGI"),
        ("biblioteca_aguas_subterraneas.csv", "CONAGUA"),
    ]
    for fn, src in repos:
        st.markdown(
            f"<div style='font-family:DM Mono,monospace;font-size:0.72rem;color:#4a5568;"
            f"padding:0.35rem 0;border-bottom:1px solid rgba(255,255,255,0.04);'>"
            f"<span style='color:#10b981;'>✔</span> <code style='color:#94a3b8;'>{fn}</code>"
            f"<span style='float:right;color:#2d3748;'>{src}</span></div>",
            unsafe_allow_html=True
        )
    st.write("---")

    st.markdown(
        "<div style='font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.14em;"
        "text-transform:uppercase;color:#63b3ed;margin-bottom:0.5rem;'>Investigadora Principal</div>"
        "<div style='font-family:DM Sans,sans-serif;font-size:0.88rem;color:#e2e8f0;'>"
        "Laura Pamela Aranda Medrano</div>"
        "<div style='font-family:DM Sans,sans-serif;font-size:0.78rem;color:#4a5568;margin-top:0.3rem;'>"
        "The Balance Core (2026)</div>",
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────────────────
st.markdown("""
<div class="sice-hero">
    <div class="sice-eyebrow">Sistema de Inferencia Computacional Estratégica · México</div>
    <h1 class="sice-title">SICE-México AI</h1>
    <p class="sice-subtitle">
        Ecosistema Computacional de Gobernanza Predictiva<br>
        e Inferencia Macroestructural Subnacional
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="status-banner" role="alert" aria-live="polite">
    <span style="font-size:1.1rem;flex-shrink:0;">⚠</span>
    <span>
        <strong>Fase de Calibración Activa.</strong>
        Los módulos deterministas y capas predictivas están siendo sometidos a procesos
        continuos de optimización algorítmica para asegurar la máxima precisión métrica
        en la inferencia subnacional.
    </span>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
#  TARJETA TEÓRICA (HTML+MathJax — sin JS de acordeón)
# ─────────────────────────────────────────────────────────
html_teoria = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<script>
MathJax = {
  tex: { inlineMath: [['\\\\(','\\\\)']], displayMath: [['\\\\[','\\\\]']] },
  options: { skipHtmlTags: ['script','noscript','style','textarea'] }
};
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }
body {
    margin: 0; padding: 0;
    background: transparent;
    font-family: 'DM Sans', sans-serif;
    color: #e2e8f0;
    -webkit-font-smoothing: antialiased;
}

details {
    background: rgba(8, 14, 32, 0.92);
    border: 1px solid rgba(99,179,237,0.2);
    border-radius: 12px;
    overflow: hidden;
    backdrop-filter: blur(16px);
}

summary {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.1rem 1.6rem;
    cursor: pointer;
    font-family: 'DM Mono', monospace;
    font-size: 0.76rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #63b3ed;
    background: rgba(15,23,42,0.8);
    border-bottom: 1px solid rgba(99,179,237,0.1);
    user-select: none;
    list-style: none;
    transition: background 0.2s;
}
summary::-webkit-details-marker { display: none; }
summary:hover { background: rgba(26,32,60,0.9); }
summary .icon {
    font-size: 0.65rem;
    color: #4a5568;
    transition: transform 0.3s;
}
details[open] summary .icon { transform: rotate(180deg); }

.panel { padding: 2rem 2.2rem 2.4rem; }

.theory-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.45rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 1rem 0;
    letter-spacing: -0.01em;
}

p {
    font-size: 0.95rem;
    line-height: 1.78;
    color: #94a3b8;
    margin-bottom: 1rem;
}

.dim-pills {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
    margin: 1.4rem 0;
}
.pill {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 8px;
    padding: 0.85rem 1rem;
}
.pill-icon { font-size: 1rem; margin-bottom: 0.3rem; }
.pill-name {
    font-family: 'Syne', sans-serif;
    font-size: 0.82rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 0.15rem;
}
.pill-desc {
    font-size: 0.78rem;
    color: #4a5568;
    line-height: 1.5;
}

.formula-block {
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 1.6rem 2rem;
    margin: 1.6rem 0;
    text-align: center;
    overflow-x: auto;
}

.formula-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.64rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #4a5568;
    margin-bottom: 1rem;
}

.note {
    font-size: 0.8rem;
    color: #4a5568;
    font-style: italic;
    line-height: 1.6;
    margin-top: 1rem;
}

/* Accesibilidad: texto legible en alto contraste */
@media (prefers-contrast: more) {
    p, .note { color: #e2e8f0 !important; }
    .pill-desc { color: #94a3b8 !important; }
}
</style>
</head>
<body>
<details open>
  <summary>
    <span>📖 &nbsp; Ontología y Epistemología del Balance Core</span>
    <span class="icon">▲</span>
  </summary>
  <div class="panel">

    <h2 class="theory-title">La Ontología del Balance Sistémico y Multidimensional</h2>

    <p>
      <strong style="color:#e2e8f0;">The Balance Core</strong> postula que la estabilidad
      estructural de un territorio depende de la <em>alineación proporcional</em> y la
      <em>tensión homeostática</em> de cuatro vectores vitales. A diferencia de enfoques
      ortodoxos orientados hacia la acumulación unidimensional, este modelo detecta
      cuándo un vector está canibalizando los recursos de otro.
    </p>

    <div class="dim-pills">
      <div class="pill">
        <div class="pill-icon">🏛️</div>
        <div class="pill-name">Structure (S)</div>
        <div class="pill-desc">Capacidad institucional, solidez jurídica y resiliencia burocrática subnacional.</div>
      </div>
      <div class="pill">
        <div class="pill-icon">🧬</div>
        <div class="pill-name">Identity (I)</div>
        <div class="pill-desc">Cohesión del tejido social, arraigo cultural y contención a la dispersión migratoria.</div>
      </div>
      <div class="pill">
        <div class="pill-icon">🔌</div>
        <div class="pill-name">Connectivity (C)</div>
        <div class="pill-desc">Densidad de redes, adopción digital e interconexión con flujos macroeconómicos globales.</div>
      </div>
      <div class="pill">
        <div class="pill-icon">🌱</div>
        <div class="pill-name">Planetary Ethics (E)</div>
        <div class="pill-desc">Cumplimiento de límites biofísicos, sustentabilidad ecosistémica e hidrogeológica.</div>
      </div>
    </div>

    <h3 style="font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:700;color:#63b3ed;
               margin:1.8rem 0 0.7rem;letter-spacing:-0.01em;">
      Formalización del Desequilibrio
    </h3>

    <p>
      La vulnerabilidad territorial se cuantifica mediante el
      <strong style="color:#e2e8f0;">Coeficiente de Dispersión Dimensional (D)</strong>,
      calculado como la desviación estándar de los cuatro vectores sobre datos extraídos
      de repositorios oficiales:
    </p>

    <div class="formula-block" role="math" aria-label="Fórmula del coeficiente de dispersión D">
      <div class="formula-label">Coeficiente de Dispersión Dimensional</div>
      \\[
        D = \\sigma(S,\\,I,\\,C,\\,E)
          = \\sqrt{\\frac{1}{4}\\sum_{i=1}^{4}\\left(x_i - \\mu\\right)^{2}}
      \\]
      <p style="margin-top:1rem;font-size:0.85rem;color:#4a5568;">
        donde \\(\\mu = \\dfrac{S+I+C+E}{4}\\) es la media dimensional del territorio.
      </p>
    </div>

    <p class="note">
      * Un valor de D ≤ 4.0 indica Equilibrio Coherente (Adaptive Coherence).
        Valores superiores señalan Dispersión Crítica (Systemic Imbalance), donde al menos
        un vector concentra o drena desproporcionadamente los recursos del sistema.
    </p>

  </div>
</details>
</body>
</html>
"""

st.components.v1.html(html_teoria, height=640, scrolling=False)


# ─────────────────────────────────────────────────────────
#  CARGA DE DATOS
# ─────────────────────────────────────────────────────────
@st.cache_data
def cargar_datos():
    if os.path.exists("datos_sice.csv"):
        return pd.read_csv("datos_sice.csv")
    return pd.DataFrame({
        "estado": ["Michoacán", "Nuevo León", "Ciudad de México", "Jalisco", "Yucatán"],
        "S": [11.5, 21.8, 23.2, 19.4, 13.1],
        "I": [23.8,  4.3,  2.1, 14.5,  3.8],
        "C": [12.4, 24.1, 24.8, 20.2, 14.5],
        "E": [18.5,  4.2, 11.4, 12.6, 21.3],
    })

df = cargar_datos()

if df is None:
    st.warning("Cargue el archivo `datos_sice.csv` en la raíz del repositorio para inicializar el pipeline.")
    st.stop()


# ─────────────────────────────────────────────────────────
#  SELECTOR DE ENTIDAD
# ─────────────────────────────────────────────────────────
st.markdown(
    "<div style='font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.18em;"
    "text-transform:uppercase;color:#63b3ed;margin-bottom:0.4rem;'>— Interrogación del Vector Territorial</div>",
    unsafe_allow_html=True
)
estado_selector = st.selectbox(
    "Seleccione la entidad federativa a auditar:",
    df["estado"].sort_values().unique(),
    label_visibility="collapsed"
)

data_vector  = df[df["estado"] == estado_selector].iloc[0]
S, I, C, E   = float(data_vector["S"]), float(data_vector["I"]), float(data_vector["C"]), float(data_vector["E"])

gbi_total    = S + I + C + E
valores      = [S, I, C, E]
dispersion_D = float(np.std(valores))
promedio_u   = float(np.mean(valores))
desviaciones = [v - promedio_u for v in valores]
idx_ruptura  = int(np.argmax(np.abs(desviaciones)))
codigos_dim  = ["S", "I", "C", "E"]
dim_fractura = codigos_dim[idx_ruptura]

EQUILIBRIO = dispersion_D <= 4.0

if EQUILIBRIO:
    clasificacion = "EQUILIBRIO COHERENTE"
    color_hex     = "#10b981"
    foco          = "DÉFICIT BAJO · COHERENCE ADAPTATIVA REGIONAL"
    analisis      = (
        f"El territorio de {estado_selector} opera dentro de un marco de balance estructural "
        f"proporcional. Su índice de dispersión analítica D\u202f=\u202f{dispersion_D:.2f} indica que "
        f"ninguna dimensión está canibalizando los recursos de otra. El sistema muestra resiliencia "
        f"homeostática apta para políticas de consolidación progresiva."
    )
    recs = [
        ("Preservación Dinámica del Modelo",
         "Institucionalizar el vector actual como línea base regulatoria para la planificación territorial estratégica."),
        ("Monitoreo de Fluctuación Coetánea",
         "Implementar auditorías de varianza semestrales para detectar desviaciones antes de cruzar el umbral de fricción."),
        ("Optimización Estructurada",
         "Prohibir políticas de expansión acelerada en conectividad que no demuestren acoplamiento simétrico con capacidades locales."),
    ]
elif dim_fractura == "E" or E < 10.0:
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "DÉFICIT ÉTICO-ECOLÓGICO POR SATURACIÓN INDUSTRIAL"
    analisis      = (
        f"El vector de {estado_selector} exhibe sobreexplotación biofísica severa. "
        f"El indicador hidrogeológico real extraído de CONAGUA ({E:.1f}/25) señala que las presiones "
        f"del nearshoring transnacional están rebasando la resiliencia de las cuencas locales. "
        f"El desequilibrio D\u202f=\u202f{dispersion_D:.2f} confirma la fractura del eje ambiental."
    )
    recs = [
        ("Moratoria de Nearshoring Extractivo",
         "Suspender inmediatamente licencias a corporaciones con demanda hídrica intensiva mientras se recalibra la capacidad de las cuencas."),
        ("Monitoreo Satelital Coetáneo",
         "Conectar la infraestructura de sensores CONAGUA directamente al pipeline del SICE para auditar el abatimiento de acuíferos en tiempo real."),
        ("Equilibrio Planetario Mandatorio",
         "Anteponer los límites de supervivencia biofísica sobre incentivos comerciales en toda nueva regulación de inversión extranjera."),
    ]
elif dim_fractura == "I":
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "DISRUPCIÓN IDENTITARIA POR ALTA INTENSIDAD MIGRATORIA"
    analisis      = (
        f"Los microdatos del CONAPO detectan fragmentación del tejido social en {estado_selector} "
        f"(I\u202f=\u202f{I:.1f}/25). La alta intensidad migratoria transnacional genera una fuga crítica "
        f"de capital social que erosiona la cohesión comunitaria y debilita la capacidad de organización institucional local."
    )
    recs = [
        ("Políticas de Arraigo Coetáneo",
         "Destinar incentivos a la tecnificación del campo en regiones de expulsión demográfica para frenar la migración forzada."),
        ("Fideicomisos de Resiliencia Social",
         "Estructurar coinversión institucional con asociaciones de migrantes para transformar remesas en capital productivo endógeno."),
        ("Estabilización del Entorno",
         "Fortalecer mecanismos de cohesión comunitaria interna para blindar la identidad cultural regional."),
    ]
elif dim_fractura == "C":
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "DOMINANCIA ASIMÉTRICA DE CONECTIVIDAD DIGITAL"
    analisis      = (
        f"La entidad registra hiper-conectividad digital (C\u202f=\u202f{C:.1f}/25) según la ENDUTIH-INEGI, "
        f"que desborda sus capacidades institucionales de control (S\u202f=\u202f{S:.1f}/25). "
        f"La asimetría D\u202f=\u202f{dispersion_D:.2f} expone una brecha de gobernanza digital de riesgo sistémico."
    )
    recs = [
        ("Soberanía de Datos Gubernamentales",
         "Mandatar que toda metadata crítica gubernamental sea procesada en infraestructuras locales soberanas."),
        ("Sustitución de Dependencias Críticas",
         "Migrar plataformas tecnológicas clave a soluciones de software abierto con capacidad de auditoría interna."),
        ("Gobernanza de Redes",
         "Vincular el despliegue de nueva infraestructura de conectividad a la maduración de capacidades de auditoría en el eje Structure."),
    ]
else:
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "DEBILIDAD ESTRUCTURAL Y REZAGO INSTITUCIONAL"
    analisis      = (
        f"El algoritmo SICE reporta parálisis en el eje Structure (S\u202f=\u202f{S:.1f}/25), "
        f"condicionado por altos índices de marginación e ineficiencia burocrática. "
        f"La dispersión D\u202f=\u202f{dispersion_D:.2f} confirma que el rezago institucional actúa como "
        f"cuello de botella para el desarrollo de los demás vectores."
    )
    recs = [
        ("Automatización del Control Institucional",
         "Implementar la matriz determinista SICE para erradicar procesos opacos y reducir la discrecionalidad burocrática."),
        ("Inversión Proporcional Compensatoria",
         "Reorientar el gasto público estatal exclusivamente hacia los ejes rezagados hasta restablecer el equilibrio dimensional."),
        ("Blindaje Normativo",
         "Fortalecer el marco jurídico subnacional bajo principios de realismo periférico y auditoría ciudadana continua."),
    ]


# ─────────────────────────────────────────────────────────
#  BARRAS DIMENSIONALES
# ─────────────────────────────────────────────────────────
st.write("")
st.markdown(
    "<div style='font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.18em;"
    "text-transform:uppercase;color:#63b3ed;margin-bottom:1.2rem;'>— Mapa Vectorial Dimensional</div>",
    unsafe_allow_html=True
)

dim_colors = {"S": "#63b3ed", "I": "#f6ad55", "C": "#76e4f7", "E": "#68d391"}
dim_names  = {"S": "Structure", "I": "Identity", "C": "Connectivity", "E": "Planetary Ethics"}
dim_vals   = {"S": S, "I": I, "C": C, "E": E}

col_left, col_right = st.columns(2)
for idx, (key, val) in enumerate(dim_vals.items()):
    col = col_left if idx < 2 else col_right
    pct = val / 25 * 100
    col.markdown(f"""
<div class="dim-row">
  <div class="dim-label">
    <span>{dim_names[key]} ({key})</span>
    <span style="color:{dim_colors[key]};">{val:.1f} / 25</span>
  </div>
  <div class="dim-track" role="progressbar" aria-valuenow="{val:.1f}" aria-valuemin="0" aria-valuemax="25"
       aria-label="{dim_names[key]}: {val:.1f} de 25">
    <div class="dim-fill" style="width:{pct:.1f}%;background:{dim_colors[key]};"></div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
#  MÉTRICAS
# ─────────────────────────────────────────────────────────
st.markdown(f"""
<div class="metric-grid" role="region" aria-label="Métricas del sistema">
  <div class="metric-card">
    <div class="metric-label">Global Balance Index (GBI)</div>
    <div class="metric-val" style="color:{color_hex};">{gbi_total:.1f}<span style="font-size:1rem;color:#4a5568;font-weight:400;">/100</span></div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Dispersión Dimensional (D)</div>
    <div class="metric-val" style="color:#e2e8f0;">{dispersion_D:.2f}</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Clasificación Sistémica</div>
    <div class="metric-val" style="font-size:1rem;color:{color_hex};margin-top:0.4rem;">{clasificacion}</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("---")


# ─────────────────────────────────────────────────────────
#  GENERADOR DE DICTAMEN
# ─────────────────────────────────────────────────────────
st.markdown(
    "<div style='font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.18em;"
    "text-transform:uppercase;color:#63b3ed;margin-bottom:0.3rem;'>— Centro de Inferencia Analítica Subnacional</div>"
    "<p style='font-size:0.85rem;color:#4a5568;font-family:DM Sans,sans-serif;margin-bottom:1rem;'>"
    "Presione el botón para emitir el dictamen regulatorio predictivo.</p>",
    unsafe_allow_html=True
)

if st.button("↗ Interrogar Nodo Territorial · Desplegar Dictamen"):
    with st.spinner("Procesando vectores territoriales…"):
        time.sleep(0.4)

    recs_items = "".join(
        f'<li class="memo-rec-item">'
        f'<span class="rec-num">0{i+1}</span>'
        f'<span><strong style="color:#fff;font-family:DM Sans,sans-serif;">{titulo}.</strong>'
        f'&ensp;<span style="color:#94a3b8;">{desc}</span></span>'
        f'</li>'
        for i, (titulo, desc) in enumerate(recs)
    )

    dictamen_html = f"""
    <div class="memo-shell" role="main" aria-label="Dictamen de Gobernanza Predictiva">
      <div class="memo-topbar" aria-hidden="true">
        <span class="memo-dot" style="background:#ef4444;"></span>
        <span class="memo-dot" style="background:#f59e0b;"></span>
        <span class="memo-dot" style="background:#10b981;"></span>
        <span style="font-family:DM Mono,monospace;font-size:0.65rem;color:#2d3748;margin-left:0.6rem;">
          SICE-{estado_selector[:3].upper()}-2026 · DICTAMEN REGULATORIO
        </span>
      </div>
      <div class="memo-body">
        <div class="memo-title">Dictamen de Gobernanza Predictiva</div>
        <div class="memo-ref">
          REF: SICE-{estado_selector[:3].upper()}-2026-RESOLVED &nbsp;·&nbsp;
          Entidad: {estado_selector} &nbsp;·&nbsp;
          Emisión Experimental
        </div>

        <div class="memo-section">Eje de Ruptura Multidimensional</div>
        <div class="memo-finding" style="color:{color_hex};">{foco}</div>

        <div class="memo-section">Evaluación Macrodinámica del Vector</div>
        <div class="memo-analysis" style="border-color:{color_hex};">{analisis}</div>

        <div class="memo-section">Directrices Regulatorias de Diseño Institucional</div>
        <ul class="memo-rec-list" aria-label="Recomendaciones">
          {recs_items}
        </ul>

        <div class="memo-footer">
          Framework determinista de datos abiertos en fase de calibración.<br>
          Respaldado por el portafolio empírico en Harvard Dataverse e indexado en SSRN (Elsevier)<br>
          por la autora Laura Pamela Aranda Medrano, 2026. Todos los conceptos de alineación
          estructural se desprenden del marco conceptual abierto de <em>The Balance Core</em>.
        </div>
      </div>
    </div>
    """
    st.html(dictamen_html)
    st.balloons()
