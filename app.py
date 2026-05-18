import streamlit as st
import pandas as pd
import numpy as np
import os
import time
import random

# ─────────────────────────────────────────────────────────
#  CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SICE-México AI | Ecosistema Analítico",
    page_icon="🦋",
    layout="wide",
    initial_sidebar_state="expanded"
)

STAR_BG = "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?q=80&w=2560&auto=format&fit=crop"

# ─────────────────────────────────────────────────────────
#  CSS GLOBAL
# ─────────────────────────────────────────────────────────
css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&family=DM+Mono:wght@400;500&display=swap');

/* ── Fondo de estrellas ── */
.stApp {{
    background-image:
        linear-gradient(180deg, rgba(3,6,16,0.93) 0%, rgba(5,10,24,0.90) 100%),
        url("{STAR_BG}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
.stMain, .stHeader,
[data-testid="stHeader"],
[data-testid="stMain"],
[data-testid="stVerticalBlock"],
[data-testid="stAppViewMain"] {{
    background: transparent !important;
}}
[data-testid="stMainBlockContainer"] {{
    padding: 3rem 5.5rem !important;
    max-width: 100% !important;
}}

/* ── Sidebar ── */
.stSidebar, [data-testid="stSidebar"] {{
    background: rgba(3, 5, 14, 0.98) !important;
    backdrop-filter: blur(24px) !important;
    border-right: 1px solid rgba(99,179,237,0.10) !important;
}}

/* ── Tipografía global ── */
html, body, .stMarkdown, p, span, label, div, li, h1, h2, h3, h4 {{
    font-family: 'DM Sans', sans-serif !important;
    color: #e2e8f0 !important;
}}

/* ── Selectbox ── */
[data-testid="stSelectbox"] label,
[data-testid="stWidgetLabel"] {{
    font-family: 'DM Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #63b3ed !important;
}}

/* ── Hero ── */
.sice-eyebrow {{
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: #63b3ed;
    margin-bottom: 0.5rem;
}}
.sice-title {{
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.6rem, 5vw, 4rem);
    font-weight: 800;
    color: #ffffff;
    line-height: 1.06;
    letter-spacing: -0.025em;
    margin: 0 0 0.6rem 0;
}}
.sice-subtitle {{
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    color: #4a5568;
    font-weight: 300;
    line-height: 1.65;
    max-width: 70ch;
    margin-bottom: 2rem;
}}

/* ── Banner ── */
.status-banner {{
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    background: rgba(251,191,36,0.04);
    border: 1px solid rgba(251,191,36,0.2);
    border-left: 3px solid #f59e0b;
    padding: 1rem 1.3rem;
    border-radius: 8px;
    margin-bottom: 2.5rem;
    font-size: 0.86rem;
    line-height: 1.65;
    color: #fde68a;
}}
.status-banner strong {{ color: #fef3c7 !important; }}

/* ── Barras dimensionales ── */
.dim-section-label {{
    font-family: 'DM Mono', monospace;
    font-size: 0.64rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #63b3ed;
    margin-bottom: 1.2rem;
}}
.dim-row {{ margin-bottom: 1.5rem; }}
.dim-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.45rem;
}}
.dim-name {{
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #718096;
}}
.dim-score {{
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
}}
.dim-track {{
    background: rgba(255,255,255,0.05);
    border-radius: 99px;
    height: 5px;
    overflow: visible;
    position: relative;
}}
.dim-fill {{
    height: 100%;
    border-radius: 99px;
    position: relative;
    transition: width 0.7s cubic-bezier(.4,0,.2,1);
}}
.dim-fill::after {{
    content: '';
    position: absolute;
    right: -1px;
    top: 50%;
    transform: translateY(-50%);
    width: 9px; height: 9px;
    border-radius: 50%;
    background: inherit;
    filter: brightness(1.5);
    box-shadow: 0 0 10px currentColor;
}}

/* ── Métricas ── */
.metric-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 2rem 0 1.5rem;
}}
.metric-card {{
    background: rgba(6, 11, 26, 0.85);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.5rem 1.3rem;
    text-align: center;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 28px rgba(0,0,0,0.35);
    transition: border-color 0.3s;
}}
.metric-card:hover {{ border-color: rgba(99,179,237,0.22); }}
.metric-lbl {{
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #2d3748;
    margin-bottom: 0.65rem;
}}
.metric-val {{
    font-family: 'Syne', sans-serif;
    font-size: 1.95rem;
    font-weight: 800;
    line-height: 1;
}}

/* ── Sección labels ── */
.section-label {{
    font-family: 'DM Mono', monospace;
    font-size: 0.64rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #63b3ed;
    margin-bottom: 0.3rem;
}}
.section-caption {{
    font-family: 'DM Sans', sans-serif;
    font-size: 0.83rem;
    color: #2d3748;
    margin-bottom: 1rem;
}}

/* ── Botón ── */
.stButton > button {{
    background: linear-gradient(135deg, #1a56db 0%, #0e3fa8 100%) !important;
    color: #fff !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.74rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.75rem 2rem !important;
    box-shadow: 0 4px 20px rgba(26,86,219,0.3) !important;
    transition: all 0.25s ease !important;
}}
.stButton > button:hover {{
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 28px rgba(26,86,219,0.5) !important;
}}

/* ── Memorándum ── */
.memo-shell {{
    background: rgba(5, 8, 20, 0.98);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 40px 80px -20px rgba(0,0,0,0.9);
    margin-top: 1.5rem;
}}
.memo-topbar {{
    padding: 0.45rem 1.8rem;
    display: flex;
    align-items: center;
    gap: 0.45rem;
    background: rgba(255,255,255,0.02);
    border-bottom: 1px solid rgba(255,255,255,0.05);
}}
.memo-dot {{ width: 9px; height: 9px; border-radius: 50%; display: inline-block; }}
.memo-wintitle {{
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    color: #1a202c;
    margin-left: 0.5rem;
    letter-spacing: 0.1em;
}}
.memo-body {{ padding: 2rem 2.6rem 2.6rem; }}
.memo-title {{
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.15rem;
}}
.memo-ref {{
    font-family: 'DM Mono', monospace;
    font-size: 0.67rem;
    color: #2d3748;
    letter-spacing: 0.08em;
    margin-bottom: 2rem;
}}
.memo-sec {{
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #2d3748;
    padding-bottom: 0.35rem;
    border-bottom: 1px dashed rgba(255,255,255,0.07);
    margin-top: 1.8rem;
    margin-bottom: 0.8rem;
}}
.memo-finding {{
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 0.3rem 0 1.3rem;
}}
.memo-analysis {{
    font-family: 'DM Sans', sans-serif;
    font-size: 0.94rem;
    line-height: 1.78;
    font-style: italic;
    color: #718096;
    background: rgba(255,255,255,0.02);
    padding: 1.1rem 1.3rem;
    border-radius: 8px;
    border-left: 3px solid;
    margin-bottom: 1.5rem;
}}
.memo-rec-list {{
    list-style: none;
    padding: 0; margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}}
.memo-rec-item {{
    display: grid;
    grid-template-columns: 2rem 1fr;
    gap: 0.9rem;
    align-items: flex-start;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 0.85rem 1rem;
}}
.rec-num {{
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #2d3748;
    padding-top: 0.15rem;
}}
.rec-title {{
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    color: #e2e8f0;
    margin-bottom: 0.2rem;
}}
.rec-body {{
    font-family: 'DM Sans', sans-serif;
    font-size: 0.83rem;
    color: #4a5568;
    line-height: 1.6;
}}
.memo-footer {{
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #1a202c;
    margin-top: 2.5rem;
    padding-top: 0.9rem;
    border-top: 1px dashed rgba(255,255,255,0.06);
    line-height: 1.75;
}}

/* ── Mariposas Monarca ── */
@keyframes monarchFly {{
    0%   {{ transform: translateY(0) translateX(0) rotate(-3deg); opacity: 1; }}
    20%  {{ transform: translateY(-22vh) translateX(18px) rotate(6deg); opacity: 1; }}
    45%  {{ transform: translateY(-50vh) translateX(-12px) rotate(-4deg); opacity: 0.9; }}
    70%  {{ transform: translateY(-75vh) translateX(22px) rotate(7deg); opacity: 0.55; }}
    100% {{ transform: translateY(-105vh) translateX(-8px) rotate(0deg); opacity: 0; }}
}}
@keyframes wingFlap {{
    0%, 100% {{ transform: scaleX(1); }}
    50%       {{ transform: scaleX(0.45); }}
}}
.butterfly-container {{
    position: fixed;
    bottom: 0; left: 0; right: 0;
    pointer-events: none;
    z-index: 9999;
    height: 100vh;
    overflow: hidden;
}}
.butterfly {{
    position: absolute;
    bottom: -50px;
    animation: monarchFly linear forwards;
    display: inline-block;
}}
.butterfly span {{
    display: inline-block;
    animation: wingFlap 0.38s ease-in-out infinite;
}}

/* ── Divisores ── */
hr {{ border-color: rgba(255,255,255,0.06) !important; }}

/* ── Accesibilidad ── */
@media (prefers-contrast: more) {{
    .sice-subtitle, .metric-lbl, .memo-ref, .rec-body, .memo-footer,
    .section-caption {{ color: #94a3b8 !important; }}
    .memo-analysis {{ color: #e2e8f0 !important; }}
    .dim-name {{ color: #94a3b8 !important; }}
    .pill-desc {{ color: #718096 !important; }}
}}
@media (prefers-reduced-motion: reduce) {{
    .butterfly {{ animation: none !important; opacity: 0 !important; }}
    .dim-fill {{ transition: none !important; }}
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        "<div style='font-family:Syne,sans-serif;font-size:1.25rem;font-weight:800;"
        "color:#fff;letter-spacing:-0.01em;margin-bottom:0.1rem;'>SICE-México</div>"
        "<div style='font-family:DM Mono,monospace;font-size:0.62rem;letter-spacing:0.18em;"
        "text-transform:uppercase;color:#2d3748;margin-bottom:1.5rem;'>Core Engine v2.5</div>",
        unsafe_allow_html=True
    )
    st.write("---")
    st.markdown(
        "<div style='font-family:DM Mono,monospace;font-size:0.62rem;letter-spacing:0.14em;"
        "text-transform:uppercase;color:#63b3ed;margin-bottom:0.65rem;'>Gobernanza & Ciencia Abierta</div>",
        unsafe_allow_html=True
    )
    st.caption(
        "Este ecosistema opera bajo principios de **Ciencia Abierta**, con su núcleo "
        "alojado en un repositorio público de GitHub. Representa una muestra nacional "
        "calibrada con proyecciones a escala global."
    )
    st.write("---")
    st.markdown(
        "<div style='font-family:DM Mono,monospace;font-size:0.62rem;letter-spacing:0.14em;"
        "text-transform:uppercase;color:#63b3ed;margin-bottom:0.65rem;'>Repositorios Indexados</div>",
        unsafe_allow_html=True
    )
    for fn, src in [
        ("ime_2020.csv", "CONAPO"),
        ("03_iim_mex_eeuu_2020_entidad.csv", "Migración"),
        ("13_personas_usuarios_internet.csv", "INEGI"),
        ("biblioteca_aguas_subterraneas.csv", "CONAGUA"),
    ]:
        st.markdown(
            f"<div style='font-family:DM Mono,monospace;font-size:0.7rem;color:#2d3748;"
            f"padding:0.32rem 0;border-bottom:1px solid rgba(255,255,255,0.04);'>"
            f"<span style='color:#10b981;margin-right:0.4rem;'>✔</span>"
            f"<code style='color:#718096;background:transparent;'>{fn}</code>"
            f"<span style='float:right;color:#1a202c;'>{src}</span></div>",
            unsafe_allow_html=True
        )
    st.write("---")
    st.markdown(
        "<div style='font-family:DM Mono,monospace;font-size:0.62rem;letter-spacing:0.14em;"
        "text-transform:uppercase;color:#63b3ed;margin-bottom:0.45rem;'>Investigadora Principal</div>"
        "<div style='font-family:DM Sans,sans-serif;font-size:0.88rem;color:#e2e8f0;'>"
        "Laura Pamela Aranda Medrano</div>"
        "<div style='font-family:DM Sans,sans-serif;font-size:0.76rem;color:#2d3748;margin-top:0.25rem;'>"
        "The Balance Core (2026)</div>",
        unsafe_allow_html=True
    )


# ─────────────────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:2.5rem 0 0.5rem 0;">
    <div class="sice-eyebrow">Sistema de Inferencia Computacional Estratégica · México</div>
    <h1 class="sice-title">SICE-México AI</h1>
    <p class="sice-subtitle">
        Ecosistema computacional de gobernanza predictiva e inferencia macroestructural subnacional.<br>
        Un aporte a Michoacán, a México y al equilibrio del planeta.
    </p>
</div>
<hr style="border:none;border-top:1px solid rgba(255,255,255,0.06);margin:0 0 2.5rem 0;">
""", unsafe_allow_html=True)

st.markdown("""
<div class="status-banner" role="alert" aria-live="polite">
    <span style="font-size:1rem;flex-shrink:0;">⚠</span>
    <span>
        <strong>Fase de Calibración Activa.</strong>
        Los módulos deterministas y capas predictivas están siendo sometidos a procesos
        continuos de optimización algorítmica para asegurar la máxima precisión métrica
        en la inferencia subnacional.
    </span>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
#  TARJETA TEÓRICA — KaTeX para fórmulas confiables
# ─────────────────────────────────────────────────────────
html_teoria = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;1,9..40,300&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{
    delimiters:[
      {left:'$$',right:'$$',display:true},
      {left:'$',right:'$',display:false}
    ],
    throwOnError:false
  });"></script>
<style>
*,*::before,*::after{box-sizing:border-box;}
body{margin:0;padding:0;background:transparent;font-family:'DM Sans',sans-serif;
     color:#e2e8f0;-webkit-font-smoothing:antialiased;}

details{background:rgba(6,10,24,0.96);border:1px solid rgba(99,179,237,0.18);border-radius:12px;overflow:hidden;}
summary{display:flex;justify-content:space-between;align-items:center;
        padding:1rem 1.5rem;cursor:pointer;
        font-family:'DM Mono',monospace;font-size:0.72rem;letter-spacing:0.16em;text-transform:uppercase;
        color:#63b3ed;background:rgba(10,16,36,0.9);
        border-bottom:1px solid rgba(99,179,237,0.1);user-select:none;list-style:none;transition:background .2s;}
summary::-webkit-details-marker{display:none;}
summary:hover{background:rgba(20,28,55,0.9);}
.icon{font-size:.6rem;color:#2d3748;transition:transform .3s;}
details[open] .icon{transform:rotate(180deg);}

.panel{padding:1.8rem 2rem 2.2rem;}
.theory-title{font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:700;color:#fff;
              margin:0 0 .85rem;letter-spacing:-.01em;}
p{font-size:.92rem;line-height:1.78;color:#718096;margin-bottom:.95rem;}
strong{color:#e2e8f0!important;}

.pill-grid{display:grid;grid-template-columns:1fr 1fr;gap:.7rem;margin:1.2rem 0;}
.pill{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.07);border-radius:8px;padding:.8rem .9rem;}
.pill-icon{font-size:.95rem;margin-bottom:.22rem;}
.pill-name{font-family:'Syne',sans-serif;font-size:.78rem;font-weight:700;color:#fff;margin-bottom:.1rem;}
.pill-desc{font-size:.74rem;color:#2d3748;line-height:1.5;}

.formula-wrap{background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);border-radius:10px;
              padding:1.8rem 2rem;margin:1.4rem 0;text-align:center;overflow-x:auto;}
.formula-label{font-family:'DM Mono',monospace;font-size:.62rem;letter-spacing:.18em;
               text-transform:uppercase;color:#2d3748;margin-bottom:1.1rem;}
/* KaTeX colores */
.katex,.katex *{color:#f1f5f9!important;}
.katex-display{margin:.4rem 0!important;}
.katex-display>.katex{font-size:1.5rem!important;}

.theorem-box{background:rgba(99,179,237,.05);border:1px solid rgba(99,179,237,.18);
             border-radius:8px;padding:1rem 1.2rem;margin:1.3rem 0;
             font-size:.87rem;line-height:1.72;color:#94a3b8;}
.theorem-box strong{color:#63b3ed!important;}
.thm-ok{color:#10b981!important;font-weight:700!important;}
.thm-bad{color:#ef4444!important;}

table.gbi{width:100%;border-collapse:collapse;margin:1.1rem 0;font-size:.82rem;}
table.gbi th{font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;
             color:#2d3748;padding:.5rem .75rem;text-align:left;border-bottom:1px solid rgba(255,255,255,.07);}
table.gbi td{padding:.52rem .75rem;border-bottom:1px solid rgba(255,255,255,.04);color:#94a3b8;vertical-align:middle;}
table.gbi tr:last-child td{border-bottom:none;}
.badge{display:inline-block;padding:.18rem .55rem;border-radius:99px;
       font-family:'DM Mono',monospace;font-size:.67rem;font-weight:500;}

.note{font-size:.76rem;color:#2d3748;font-style:italic;line-height:1.6;margin-top:.85rem;}

@media(prefers-contrast:more){
  p,.note,.pill-desc{color:#94a3b8!important;}
  table.gbi td{color:#cbd5e1!important;}
}
</style>
</head>
<body>
<details open>
  <summary>
    <span>📖 &nbsp; The Balance Core — Ontología, Epistemología y Formalización</span>
    <span class="icon">▲</span>
  </summary>
  <div class="panel">

    <h2 class="theory-title">Un Marco para el Equilibrio Sistémico del Siglo XXI</h2>

    <p>
        <strong>The Balance Core</strong> es un marco teórico de relaciones internacionales que reimagina
        la estabilidad no como la acumulación de poder, sino como el <em>equilibrio dinámico</em> entre
        cuatro dimensiones fundamentales de la vida colectiva. Este modelo parte de una convicción
        profunda: los territorios —desde un estado como Michoacán hasta una nación o el sistema planeta—
        pierden resiliencia cuando alguna de sus dimensiones domina desproporcionadamente sobre las demás,
        generando ciclos de extracción, exclusión o colapso que pueden identificarse y revertirse
        antes de que escalen. No es una teoría <em>del</em> poder, sino una teoría <em>más allá</em> del poder.
    </p>

    <div class="pill-grid">
      <div class="pill">
        <div class="pill-icon">🏛️</div>
        <div class="pill-name">Structure (S)</div>
        <div class="pill-desc">Instituciones, gobernanza, sistemas económicos y capacidad burocrática subnacional. Una estructura equilibrada sostiene la vida sin coerción ni sobrecarga.</div>
      </div>
      <div class="pill">
        <div class="pill-icon">🧬</div>
        <div class="pill-name">Identity (I)</div>
        <div class="pill-desc">Cohesión social, arraigo cultural y narrativa colectiva. Una identidad equilibrada evita tanto el nacionalismo excluyente como la disolución cultural.</div>
      </div>
      <div class="pill">
        <div class="pill-icon">🔌</div>
        <div class="pill-name">Connectivity (C)</div>
        <div class="pill-desc">Redes, flujos de información, adopción digital e interdependencia global. Una conectividad equilibrada evita tanto el aislamiento como la dependencia explotadora.</div>
      </div>
      <div class="pill">
        <div class="pill-icon">🌱</div>
        <div class="pill-name">Planetary Ethics (E)</div>
        <div class="pill-desc">Límites biofísicos, sustentabilidad ecosistémica y responsabilidad intergeneracional. No es un valor opcional: es un requisito práctico de supervivencia.</div>
      </div>
    </div>

    <h3 style="font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;color:#63b3ed;
               margin:1.6rem 0 .6rem;letter-spacing:-.01em;">Formalización del Desequilibrio</h3>

    <p>
        La vulnerabilidad territorial se cuantifica mediante el
        <strong>Coeficiente de Dispersión Dimensional ($D$)</strong>,
        calculado como la desviación estándar de los cuatro vectores sobre datos de repositorios oficiales.
        Un valor alto de $D$ revela que el sistema está bajo tensión estructural:
        una dimensión crece o colapsa mientras las demás quedan rezagadas.
    </p>

    <div class="formula-wrap" role="math" aria-label="Coeficiente de dispersión dimensional D">
      <div class="formula-label">Coeficiente de Dispersión Dimensional</div>
      $$D \;=\; \sigma(S,\,I,\,C,\,E) \;=\; \sqrt{\dfrac{1}{4}\sum_{i=1}^{4}\!\left(x_i - \mu\right)^{2}}$$
      <p style="margin-top:1rem;font-size:.82rem;color:#4a5568;">
        donde $\;\mu = \dfrac{S + I + C + E}{4}\;$ es la media dimensional del territorio.
      </p>
    </div>

    <div class="theorem-box">
      <strong>Teorema del Balance Core:</strong><br><br>
      Si $\;S \approx I \approx C \approx E\;$ &nbsp;→&nbsp;
        <span class="thm-ok">Estabilidad y resiliencia territorial</span><br>
      Si $\;S \gg (I,C,E)\;$ &nbsp;→&nbsp; <span class="thm-bad">riesgo de coerción institucional</span><br>
      Si $\;I \gg (S,C,E)\;$ &nbsp;→&nbsp; <span class="thm-bad">exclusión y conflicto identitario</span><br>
      Si $\;C \gg (S,I,E)\;$ &nbsp;→&nbsp; <span class="thm-bad">vulnerabilidad por dependencia digital</span><br>
      Si $\;E \ll (S,I,C)\;$ &nbsp;→&nbsp; <span class="thm-bad">colapso ecológico en curso</span>
    </div>

    <h3 style="font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;color:#63b3ed;
               margin:1.6rem 0 .6rem;letter-spacing:-.01em;">Umbrales del Global Balance Index (GBI · 0–100)</h3>

    <table class="gbi" aria-label="Umbrales del Global Balance Index">
      <thead>
        <tr><th>Rango</th><th>Clasificación</th><th>Descripción</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge" style="background:rgba(16,185,129,.15);color:#10b981;">80–100</span></td>
          <td style="color:#10b981;">Poder Armonizado</td>
          <td>Estable, influyente y adaptativo. Las cuatro dimensiones operan en sinergia.</td>
        </tr>
        <tr>
          <td><span class="badge" style="background:rgba(99,179,237,.12);color:#63b3ed;">60–79</span></td>
          <td style="color:#63b3ed;">Balance Condicional</td>
          <td>Sólido pero con vulnerabilidades latentes en al menos una dimensión.</td>
        </tr>
        <tr>
          <td><span class="badge" style="background:rgba(245,158,11,.12);color:#f59e0b;">40–59</span></td>
          <td style="color:#f59e0b;">Actor en Desequilibrio</td>
          <td>Una dimensión sobrepasa a las demás; requiere intervención estructural.</td>
        </tr>
        <tr>
          <td><span class="badge" style="background:rgba(239,68,68,.12);color:#ef4444;">0–39</span></td>
          <td style="color:#ef4444;">Inestabilidad Alta</td>
          <td>Colapso estructural o identitario probable. Intervención urgente.</td>
        </tr>
      </tbody>
    </table>

    <p class="note">
      * El marco permite diagnosticar no sólo el nivel de equilibrio,
      sino qué vector específico está generando la tensión sistémica —
      orientando las recomendaciones de política pública hacia la causa raíz,
      no hacia los síntomas superficiales.
    </p>

  </div>
</details>
</body>
</html>
"""
st.components.v1.html(html_teoria, height=800, scrolling=False)


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
#  SELECTOR
# ─────────────────────────────────────────────────────────
st.markdown("<div class='section-label'>— Interrogación del Vector Territorial</div>",
            unsafe_allow_html=True)
estado_selector = st.selectbox(
    "Entidad:",
    df["estado"].sort_values().unique(),
    label_visibility="collapsed"
)

row          = df[df["estado"] == estado_selector].iloc[0]
S, I, C, E   = float(row["S"]), float(row["I"]), float(row["C"]), float(row["E"])
gbi_total    = S + I + C + E
valores      = [S, I, C, E]
dispersion_D = float(np.std(valores))
mu           = float(np.mean(valores))
idx_ruptura  = int(np.argmax([abs(v - mu) for v in valores]))
dim_fractura = ["S", "I", "C", "E"][idx_ruptura]
EQUILIBRIO   = dispersion_D <= 4.0


# ─────────────────────────────────────────────────────────
#  DIAGNÓSTICO Y POLÍTICAS PÚBLICAS
# ─────────────────────────────────────────────────────────
if EQUILIBRIO:
    clasificacion = "EQUILIBRIO COHERENTE"
    color_hex     = "#10b981"
    foco          = f"COHERENCIA ADAPTATIVA REGIONAL · {estado_selector.upper()}"
    analisis = (
        f"{estado_selector} opera dentro de un marco de balance estructural saludable. "
        f"Con una dispersión dimensional D\u202f=\u202f{dispersion_D:.2f}, las cuatro dimensiones del sistema "
        f"mantienen una tensión homeostática positiva: ninguna crece a expensas de las demás. "
        f"Esto no significa inmovilidad — significa que el territorio tiene la base para evolucionar "
        f"sin desestabilizarse. El equilibrio es, según The Balance Core, la condición más escasa "
        f"y más valiosa de un sistema territorial. Preservarla requiere tanta habilidad como alcanzarla."
    )
    recs = [
        (
            "Institucionalizar el vector actual como línea base regulatoria",
            "El Gobierno del Estado debe codificar los niveles actuales de cada dimensión en un "
            "documento de Política de Estabilidad Territorial que sirva como referencia obligatoria "
            "para evaluar el impacto de cualquier nueva inversión, programa federal o regulación sectorial "
            "antes de su implementación. Lo que no se mide, no se protege."
        ),
        (
            "Crear un Observatorio Permanente de Equilibrio Subnacional",
            "Establecer una unidad técnica interinstitucional (SEDESOL, SEFIN, IMPLAN) que actualice "
            "trimestralmente los cuatro vectores del GBI con datos del INEGI, CONAPO y CONAGUA. "
            "El objetivo no es vigilar, sino anticipar: detectar desviaciones antes de que crucen "
            "el umbral de D\u202f>\u202f4.0 y requieran intervención de emergencia."
        ),
        (
            "Blindar la conectividad para que no desborde la capacidad institucional",
            "Toda política de expansión digital o inversión en infraestructura de conectividad "
            "debe venir acompañada de un fortalecimiento equivalente en el eje Structure: "
            "capacitación de servidores públicos, marcos de ciberseguridad y protocolos de "
            "gobernanza de datos. La tecnología sin gobernanza genera dependencia, no desarrollo."
        ),
    ]

elif dim_fractura == "E" or E < 10.0:
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "DÉFICIT ÉTICO-ECOLÓGICO · SATURACIÓN BIOFÍSICA"
    analisis = (
        f"El vector de Planetary Ethics en {estado_selector} registra {E:.1f}/25, "
        f"la brecha más severa del sistema (D\u202f=\u202f{dispersion_D:.2f}). "
        f"Los datos de CONAGUA señalan que las presiones industriales y agroindustriales "
        f"están superando la capacidad de regeneración de las cuencas locales. "
        f"The Balance Core advierte con claridad: cuando la ética planetaria colapsa, "
        f"las demás dimensiones son arrastradas con ella. No hay conectividad digital posible sin agua. "
        f"No hay cohesión social posible sin territorio habitable. "
        f"Esta es la ruptura más urgente, y la que tiene el costo de inacción más alto para las generaciones futuras."
    )
    recs = [
        (
            "Establecer una moratoria técnica de concesiones de agua para uso industrial",
            "El Gobierno del Estado debe solicitar formalmente a CONAGUA la suspensión temporal "
            "de nuevas concesiones hídricas en acuíferos con índice de sobreexplotación confirmado, "
            "hasta que se realice una auditoría independiente del balance hídrico regional. "
            "Esta acción es técnica, no ideológica: es la diferencia entre un territorio viable "
            "a 20 años y uno que no lo es."
        ),
        (
            "Integrar los sensores de CONAGUA al tablero de gobernanza en tiempo real",
            "Conectar los datos de abatimiento de acuíferos directamente al pipeline del SICE "
            "para que los tomadores de decisiones reciban alertas automáticas cuando los niveles "
            "críticos sean alcanzados. La información ambiental no puede llegar con meses de retraso "
            "a los escritorios donde se toman decisiones de inversión."
        ),
        (
            "Condicionar incentivos fiscales al cumplimiento del Índice de Ética Planetaria",
            "Reorientar los estímulos fiscales estatales para que las empresas instaladas en el territorio "
            "deban demostrar un balance positivo en el eje E antes de acceder a beneficios de operación. "
            "No es una restricción al desarrollo: es un mecanismo para asegurar que el desarrollo "
            "de hoy no hipoteque el territorio de las próximas generaciones."
        ),
    ]

elif dim_fractura == "I":
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "FRAGMENTACIÓN IDENTITARIA · ALTA INTENSIDAD MIGRATORIA"
    analisis = (
        f"Los microdatos del CONAPO registran una fractura profunda en el tejido social de {estado_selector}: "
        f"el vector Identity alcanza {I:.1f}/25, con D\u202f=\u202f{dispersion_D:.2f}. "
        f"La migración de alta intensidad no es sólo un fenómeno demográfico: "
        f"es la señal de que el territorio ha fallado en ofrecerle a su propia gente "
        f"razones suficientes para quedarse. Cuando una comunidad pierde a sus jóvenes, "
        f"pierde también su memoria institucional, su capacidad organizativa y su potencial de desarrollo endógeno. "
        f"The Balance Core identifica esto como una pérdida sistémica que ninguna transferencia de remesas puede compensar por sí sola."
    )
    recs = [
        (
            "Diseñar un Programa Estatal de Arraigo Productivo para zonas de alta expulsión",
            "Focalizar inversión pública en tecnificación agrícola, acceso a mercados locales y "
            "conectividad digital en los municipios con mayor índice de intensidad migratoria. "
            "La lógica es directa: la migración disminuye cuando permanecer es económicamente viable. "
            "Cada peso invertido en arraigo productivo ahorra décadas de fragmentación comunitaria."
        ),
        (
            "Crear fideicomisos de coinversión con asociaciones de migrantes",
            "Estructurar un mecanismo formal (3x1 ampliado) donde cada peso de remesas dirigido "
            "a proyectos productivos sea apalancado con recursos estatales, municipales y federales. "
            "El objetivo es transformar la remesa —que hoy es una transferencia de consumo— "
            "en capital que genere empleo dentro del territorio y reduzca la necesidad de emigrar."
        ),
        (
            "Institucionalizar la identidad territorial como activo estratégico",
            f"Desarrollar una política de patrimonio cultural activo que vincule la identidad de "
            f"{estado_selector} con oportunidades económicas concretas: turismo con retribución comunitaria, "
            "denominaciones de origen y artesanías con acceso a mercados nacionales e internacionales. "
            "La cultura no es decoración: es economía y es cohesión."
        ),
    ]

elif dim_fractura == "C":
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "ASIMETRÍA DIGITAL · CONECTIVIDAD SIN GOBERNANZA"
    analisis = (
        f"Los datos de la ENDUTIH-INEGI revelan una hiper-conectividad digital en {estado_selector} "
        f"(C\u202f=\u202f{C:.1f}/25) que desborda la capacidad institucional de regulación "
        f"(S\u202f=\u202f{S:.1f}/25). La dispersión D\u202f=\u202f{dispersion_D:.2f} confirma la brecha. "
        f"The Balance Core advierte: la conectividad sin gobernanza equivalente no es desarrollo, "
        f"es vulnerabilidad. Un territorio altamente conectado pero con instituciones débiles "
        f"está expuesto a dependencias tecnológicas, extracción de datos "
        f"y pérdida de soberanía sobre su propia infraestructura crítica."
    )
    recs = [
        (
            "Crear una Agencia Estatal de Soberanía Digital",
            "Establecer una entidad técnica que audite qué datos públicos están siendo procesados "
            "por infraestructuras ajenas al territorio, y que defina qué información gubernamental "
            "crítica debe residir en servidores bajo jurisdicción local. "
            "No se trata de cerrar fronteras digitales: se trata de saber qué ocurre dentro de ellas."
        ),
        (
            "Condicionar el despliegue de nueva infraestructura de conectividad a la madurez institucional",
            "Antes de aprobar expansión de redes 5G, centros de datos o plataformas de e-gobierno, "
            "exigir que el eje Structure alcance paridad con el eje Connectivity. "
            "Esto implica capacitar funcionarios, desarrollar marcos de ciberseguridad y "
            "aprobar legislación de protección de datos subnacional."
        ),
        (
            "Migrar plataformas críticas del gobierno a software abierto",
            "Priorizar soluciones de código abierto en sistemas de salud, educación y administración pública. "
            "Esto reduce la dependencia de proveedores externos, permite auditoría ciudadana y "
            "genera capacidades técnicas locales que fortalecen el eje Structure "
            "y reducen la asimetría con el eje Connectivity de forma simultánea."
        ),
    ]

else:
    clasificacion = "DISPERSIÓN CRÍTICA"
    color_hex     = "#ef4444"
    foco          = "REZAGO ESTRUCTURAL · PARÁLISIS INSTITUCIONAL"
    analisis = (
        f"El algoritmo SICE detecta que el eje Structure en {estado_selector} "
        f"(S\u202f=\u202f{S:.1f}/25) es la dimensión más rezagada del sistema (D\u202f=\u202f{dispersion_D:.2f}). "
        f"Una estructura institucional débil no sólo es un problema administrativo: "
        f"es el cuello de botella que impide que el potencial de las otras dimensiones "
        f"se traduzca en bienestar real. The Balance Core es claro: "
        f"sin instituciones que funcionen, la identidad no puede organizarse, "
        f"la conectividad no puede regularse y la ética planetaria no puede implementarse. "
        f"La reforma institucional no es una reforma más: es la condición de posibilidad de todas las demás."
    )
    recs = [
        (
            "Implementar un Índice de Desempeño Institucional subnacional con metas anuales",
            "Establecer indicadores públicos y verificables de eficiencia burocrática, "
            "tiempos de respuesta, transparencia presupuestal y resolución de trámites. "
            "Vincular el avance en estos indicadores a los criterios de evaluación del presupuesto estatal. "
            "Lo que no se mide públicamente, no mejora."
        ),
        (
            "Reorientar el gasto público con criterio de equilibrio dimensional",
            "Antes de aprobar gasto en los vectores que ya son fuertes, demostrar que el eje Structure "
            "está siendo fortalecido de manera proporcional. "
            "Esto no es austeridad: es arquitectura presupuestal inteligente que protege "
            "la inversión ya realizada en conectividad e identidad."
        ),
        (
            "Fortalecer el marco jurídico con énfasis en rendición de cuentas ciudadana",
            "Promover reformas al marco normativo estatal que faciliten la participación ciudadana "
            "en la auditoría del gasto, la denuncia de opacidad y la evaluación de programas públicos. "
            "Una institucionalidad que no se somete a escrutinio externo no puede fortalecerse desde adentro."
        ),
    ]


# ─────────────────────────────────────────────────────────
#  BARRAS DIMENSIONALES
# ─────────────────────────────────────────────────────────
st.write("")
st.markdown("<div class='dim-section-label'>— Mapa Vectorial Dimensional</div>",
            unsafe_allow_html=True)

DIM_COLOR = {"S": "#63b3ed", "I": "#f6ad55", "C": "#76e4f7", "E": "#68d391"}
DIM_NAME  = {"S": "Structure", "I": "Identity", "C": "Connectivity", "E": "Planetary Ethics"}
DIM_VAL   = {"S": S, "I": I, "C": C, "E": E}

col_l, col_r = st.columns(2)
for idx, (key, val) in enumerate(DIM_VAL.items()):
    pct  = val / 25 * 100
    col  = col_l if idx < 2 else col_r
    col.markdown(f"""
<div class="dim-row">
  <div class="dim-header">
    <span class="dim-name">{DIM_NAME[key]} ({key})</span>
    <span class="dim-score" style="color:{DIM_COLOR[key]};">
      {val:.1f}<span style="font-size:.72rem;color:#2d3748;font-weight:400;"> / 25</span>
    </span>
  </div>
  <div class="dim-track" role="progressbar"
       aria-valuenow="{val:.1f}" aria-valuemin="0" aria-valuemax="25"
       aria-label="{DIM_NAME[key]}: {val:.1f} de 25">
    <div class="dim-fill" style="width:{pct:.1f}%;background:{DIM_COLOR[key]};"></div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
#  MÉTRICAS
# ─────────────────────────────────────────────────────────
gbi_label = (
    "Poder Armonizado"   if gbi_total >= 80 else
    "Balance Condicional" if gbi_total >= 60 else
    "Actor en Desequilibrio" if gbi_total >= 40 else
    "Inestabilidad Alta"
)

st.markdown(f"""
<div class="metric-grid" role="region" aria-label="Métricas del sistema">
  <div class="metric-card">
    <div class="metric-lbl">Global Balance Index (GBI)</div>
    <div class="metric-val" style="color:{color_hex};">
      {gbi_total:.1f}<span style="font-size:.9rem;color:#2d3748;font-weight:400;">/100</span>
    </div>
    <div style="font-family:'DM Mono',monospace;font-size:.62rem;color:#2d3748;
                letter-spacing:.08em;margin-top:.4rem;">{gbi_label}</div>
  </div>
  <div class="metric-card">
    <div class="metric-lbl">Dispersión Dimensional (D)</div>
    <div class="metric-val" style="color:#e2e8f0;">{dispersion_D:.2f}</div>
    <div style="font-family:'DM Mono',monospace;font-size:.62rem;color:#2d3748;
                letter-spacing:.08em;margin-top:.4rem;">
      {"D ≤ 4.0 · Equilibrio" if EQUILIBRIO else "D > 4.0 · Tensión sistémica"}
    </div>
  </div>
  <div class="metric-card">
    <div class="metric-lbl">Clasificación Sistémica</div>
    <div class="metric-val" style="font-size:.92rem;color:{color_hex};margin-top:.35rem;">{clasificacion}</div>
    <div style="font-family:'DM Mono',monospace;font-size:.62rem;color:#2d3748;
                letter-spacing:.08em;margin-top:.4rem;">Eje crítico: {dim_fractura}</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("---")


# ─────────────────────────────────────────────────────────
#  DICTAMEN
# ─────────────────────────────────────────────────────────
st.markdown(
    "<div class='section-label'>— Centro de Inferencia Analítica Subnacional</div>"
    "<p class='section-caption'>"
    "Presione el botón para emitir el dictamen regulatorio con políticas públicas aplicables."
    "</p>",
    unsafe_allow_html=True
)

if st.button("↗ Interrogar Nodo Territorial · Desplegar Dictamen"):
    with st.spinner("Procesando vectores territoriales…"):
        time.sleep(0.35)

    recs_html = ""
    for i, (titulo, desc) in enumerate(recs):
        recs_html += f"""
        <li class="memo-rec-item">
          <span class="rec-num">0{i+1}</span>
          <div>
            <div class="rec-title">{titulo}</div>
            <div class="rec-body">{desc}</div>
          </div>
        </li>"""

    dictamen_html = f"""
    <div class="memo-shell" role="main" aria-label="Dictamen de Gobernanza Predictiva">
      <div class="memo-topbar" aria-hidden="true">
        <span class="memo-dot" style="background:#ef4444;"></span>
        <span class="memo-dot" style="background:#f59e0b;"></span>
        <span class="memo-dot" style="background:#10b981;"></span>
        <span class="memo-wintitle">
          SICE-{estado_selector[:3].upper()}-2026 · DICTAMEN REGULATORIO
        </span>
      </div>
      <div class="memo-body">
        <div class="memo-title">Dictamen de Gobernanza Predictiva</div>
        <div class="memo-ref">
          REF: SICE-{estado_selector[:3].upper()}-2026-RESOLVED &nbsp;·&nbsp;
          Entidad: {estado_selector} &nbsp;·&nbsp;
          GBI: {gbi_total:.1f}/100 &nbsp;·&nbsp; D: {dispersion_D:.2f}
        </div>

        <div class="memo-sec">Eje de Ruptura Multidimensional Identificado</div>
        <div class="memo-finding" style="color:{color_hex};">{foco}</div>

        <div class="memo-sec">Evaluación Macrodinámica del Vector</div>
        <div class="memo-analysis" style="border-color:{color_hex};">{analisis}</div>

        <div class="memo-sec">Directrices de Política Pública — Diseño Institucional</div>
        <ul class="memo-rec-list" aria-label="Recomendaciones de política pública">
          {recs_html}
        </ul>

        <div class="memo-footer">
          Framework determinista de datos abiertos en fase de calibración activa.<br>
          Indexado en SSRN (Elsevier) por la autora Laura Pamela Aranda Medrano, 2026.<br>
          Todos los conceptos de alineación estructural se desprenden del marco
          conceptual abierto de <em>The Balance Core</em>.
        </div>
      </div>
    </div>
    """
    st.html(dictamen_html)

    # ── Mariposas Monarca ──────────────────────────────
    mariposas_html = '<div class="butterfly-container" aria-hidden="true">'
    for _ in range(30):
        left  = random.randint(1, 97)
        delay = round(random.uniform(0, 3.5), 2)
        dur   = round(random.uniform(3.8, 7.0), 2)
        size  = round(random.uniform(1.1, 2.3), 1)
        mariposas_html += (
            f'<div class="butterfly" style="left:{left}%;'
            f'animation-duration:{dur}s;animation-delay:{delay}s;font-size:{size}rem;">'
            f'<span>🦋</span></div>'
        )
    mariposas_html += "</div>"
    st.markdown(mariposas_html, unsafe_allow_html=True)
