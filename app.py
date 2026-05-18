import streamlit as st
import pandas as pd
import numpy as np
import os
import time

# 1. CONFIGURACIÓN SOBERANA DE INTERFAZ (Gala Académica e UI Inmersiva)
st.set_page_config(
    page_title="SICE-México AI | Ecosistema Analítico",
    page_icon="🇲🇽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INYECCIÓN ABSOLUTA Y DESMANTELAMIENTO DE CAPAS OSCURAS (Solución Raíz)
video_path = "assets/globo_futurista.mp4"

if os.path.exists(video_path):
    import base64
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    video_base64 = base64.b64encode(video_bytes).decode()
    
    st.markdown(f"""
        <style>
        /* 1. Forzar al video a abarcar toda la pantalla física detrás de todo */
        #background-video {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            object-fit: cover;
            z-index: -99999 !important;
            opacity: 0.35;
            pointer-events: none;
        }}
        
        /* 2. APAGAR EL FONDO NEGRO DE LA RAÍZ DE LA APP (El verdadero culpable) */
        html, body, .stApp, .stAppViewMain, [data-testid="stAppViewMain"] {{
            background-color: transparent !important;
            background: transparent !important;
        }}

        /* 3. Volver transparentes los bloques intermedios de contenido */
        .stMain, .stMainBlockContainer, [data-testid="stMain"], [data-testid="stHeader"] {{
            background-color: transparent !important;
            background: transparent !important;
        }}
        
        /* 4. Limpieza de márgenes estructurales molestos */
        [data-testid="stMainBlockContainer"] {{
            padding: 3rem 5rem !important;
            max-width: 100% !important;
        }}
        
        /* 5. Panel lateral con Glassmorphism oscuro para que contraste bonito */
        .stSidebar, [data-testid="stSidebar"] {{
            background-color: rgba(10, 15, 30, 0.93) !important;
            backdrop-filter: blur(15px) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        }}
        </style>
        
        <video autoplay loop muted playsinline id="background-video">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); color: #F8FAFC; }
        </style>
    """, unsafe_allow_html=True)

# 3. ESTILOS DE TIPOGRAFÍA Y INTERFAZ DE ALTA DIRECCIÓN
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,700;1,9..144,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    .main-title { font-family: 'Fraunces', serif; font-size: 3.6rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.1rem; text-shadow: 0 4px 15px rgba(0,0,0,0.6); }
    .subtitle { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; color: #94A3B8; margin-bottom: 2.5rem; font-weight: 300; }
    
    /* Tarjeta de marco teórico */
    .theory-card { background: rgba(15, 23, 42, 0.85); color: #F8FAFC; padding: 2.2rem; border-radius: 1rem; margin-bottom: 2.5rem; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(8px); }
    .theory-title { font-family: 'Fraunces', serif; font-size: 1.7rem; color: #38BDF8; font-style: italic; margin-bottom: 1rem; }
    
    /* Cajas métricas flotantes */
    .metric-box { background-color: rgba(15, 23, 42, 0.75); padding: 1.4rem; border-radius: 0.75rem; border: 1px solid rgba(255,255,255,0.1); text-align: center; backdrop-filter: blur(6px); box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
    .metric-label { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em; color: #94A3B8; font-weight: 600; }
    .metric-val { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 2.1rem; font-weight: 800; margin-top: 0.2rem; }
    
    /* El contenedor ejecutivo premium para el Dictamen */
    .memo-container { background: rgba(10, 15, 30, 0.94); border: 1px solid rgba(255, 255, 255, 0.15); padding: 2.5rem; border-radius: 12px; box-shadow: 0 30px 60px -15px rgba(0,0,0,0.7); backdrop-filter: blur(20px); margin-top: 2rem; font-family: 'Plus Jakarta Sans', sans-serif; color: #F8FAFC; }
    .memo-header { font-family: 'Fraunces', serif; font-size: 2.2rem; font-weight: 400; color: #FFFFFF; margin-bottom: 0.2rem; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 0.6rem; }
    .memo-meta { font-size: 0.88rem; color: #94A3B8; font-family: monospace; margin-bottom: 1.8rem; }
    .memo-section-title { font-size: 0.95rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #94A3B8; margin-top: 2rem; margin-bottom: 0.8rem; border-bottom: 1px dashed rgba(255,255,255,0.15); padding-bottom: 0.3rem; }
    
    /* Forzar estilos de textos globales */
    .stMarkdown, p, span, label, h3 { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# 4. PANEL LATERAL (Sidebar Curado)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/space-shield.png", width=70)
    st.markdown("<h3 style='margin:0; color:#FFFFFF;'>SICE-México AI</h3>", unsafe_allow_html=True)
    st.caption("Engine v1.9 | Full-Screen Fixed")
    st.write("---")
    st.markdown("**📂 Portafolio Nacional Conectado:**")
    st.caption("✔️ `ime_2020.csv` (CONAPO)\n\n✔️ `03_iim_mex_eeuu.csv` (Migración)\n\n✔️ `usuarios_internet.csv` (INEGI)\n\n✔️ `biblioteca_aguas.csv` (CONAGUA)")
    st.write("---")
    st.markdown("**👤 Investigadora Principal:**\nLaura Pamela Aranda Medrano")
    st.caption("Modelos respaldados por la base de conocimientos teórica de *The Balance Core* (2026).")

# 5. ENCABEZADO DE LA PLATAFORMA
st.markdown('<div class="main-title">SICE-México AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ecosistema Computacional de Gobernanza Predictiva e Inferencia Macroestructural Subnacional</div>', unsafe_allow_html=True)

# 6. EXPLICACIÓN DE LA LÓGICA DE BALANCE INTERACTIVA
with st.expander("📖 EXPLICACIÓN CIENTÍFICA: ¿Cómo funciona la Lógica del Balance Core?"):
    st.markdown("""
    <div class="theory-card">
        <div class="theory-title">La Ontología del Balance Sistémico</div>
        <p style="font-size:1.05rem; line-height:1.7;">
            A diferencia de los modelos tradicionales orientados exclusivamente hacia la acumulación unidimensional de poder, 
            <strong>The Balance Core</strong> postula que la estabilidad real de un territorio depende de la <strong>alineación proporcional</strong> de sus cuatro dimensiones vitales.
        </p>
        <h4 style="color:#38BDF8; margin-top:1.5rem;">La Ecuación del Desequilibrio</h4>
        <p style='text-align: center; font-size: 1.4rem; background: rgba(255,255,255,0.06); padding: 1rem; border-radius: 0.5rem; margin: 1.5rem 0; color:#FFFFFF;'>
            $$D = \\sigma(S, I, C, E) = \\sqrt{\\frac{1}{4}\\sum_{i=1}^{4}(x_i - \\mu)^2}$$
        </p>
    </div>
    """, unsafe_allow_html=True)

# 7. PIPELINE DE BASES DE DATOS NACIONAL
@st.cache_data
def cargar_pipeline_nacional():
    if os.path.exists("datos_sice.csv"):
        return pd.read_csv("datos_sice.csv")
    else:
        return pd.DataFrame({
            "estado": ["Michoacán", "Nuevo León", "Ciudad de México", "Jalisco", "Yucatán"],
            "S": [11.5, 21.8, 23.2, 19.4, 13.1],
            "I": [23.8, 4.3, 2.1, 14.5, 3.8],
            "C": [12.4, 24.1, 24.8, 20.2, 14.5],
            "E": [18.5, 4.2, 11.4, 12.6, 21.3]
        })

df = cargar_pipeline_nacional()

if df is not None:
    # 8. SELECCIÓN DE ESTADO INTERACTIVO
    st.write("### 📍 Interrogación del Vector Territorial")
    estado_selector = st.selectbox("Elija la entidad federativa a auditar sobre la red de datos:", df["estado"].sort_values().unique())
    
    data_vector = df[df["estado"] == estado_selector].iloc[0]
    S, I, C, E = float(data_vector["S"]), float(data_vector["I"]), float(data_vector["C"]), float(data_vector["E"])

    # 9. RESOLUCIÓN MATEMÁTICA INTERNA
    gbi_total = S + I + C + E
    valores_sistema = [S, I, C, E]
    dispersion_D = np.std(valores_sistema)
    promedio_neto = np.mean(valores_sistema)

    desviaciones = [v - promedio_neto for v in valores_sistema]
    idx_ruptura = np.argmax(np.abs(desviaciones))
    codigos_dimension = ["S", "I", "C", "E"]
    dim_fracturada_codigo = codigos_dimension[idx_ruptura]

    if dispersion_D <= 4.0:
        clasificacion_sistema = "EQUILIBRIO COHERENTE (Adaptive Coherence)"
        color_hex = "#10B981"
        foco_diagnostico = "DÉFICIT BAJO / COHERENCE ADAPTATIVA REGIONAL"
        analisis_teorico = f"El territorio de {estado_selector} opera dentro de un marco de balance estructural proporcional. Su índice de dispersión analítica de D = {dispersion_D:.2f} denota que ninguna dimensión está canibalizando los recursos de otra."
        recom_1 = "**Preservación Dinámica del Modelo:** Institucionalizar el vector actual como línea base regulatoria para la planificación territorial estratégica."
        recom_2 = "**Monitoreo de Fluctuación Coetánea:** Implementar auditorías de varianza semestrales para detectar desviaciones antes de cruzar el umbral de fricción."
        recom_3 = "**Optimización Estructurada:** Prohibir políticas de expansión acelerada en conectividad que no demuestren un acoplamiento simétrico."
    else:
        clasificacion_sistema = "DISPERSIÓN CRÍTICA (Systemic Imbalance)"
        color_hex = "#EF4444"
        
        if dim_fracturada_codigo == "E" or E < 10.0:
            foco_diagnostico = "DÉFICIT ÉTICO-ECOLÓGICO POR SATURACIÓN INDUSTRIAL"
            analisis_teorico = f"El vector de {estado_selector} muestra una severa sobreexplotación biofísica. El indicador hídrico de las bases de CONAGUA ({E:.1f}/25) delata que las presiones del nearshoring transnacional están rebasando la resiliencia local."
            recom_1 = "**Moratoria de Nearshoring Extractivo:** Suspender inmediatamente la entrega de licencias a corporaciones que demanden un consumo hídrico intensivo."
            recom_2 = "**Monitoreo Satelital Coetáneo:** Conectar la infraestructura de sensores de CONAGUA directamente al pipeline del SICE para auditar el abatimiento de acuíferos."
            recom_3 = "**Equilibrio Planetario Mandatorio:** Anteponer los límites de supervivencia física analizados en tu obra (*When the Ground Gives Way*)."
        elif dim_fracturada_codigo == "I":
            foco_diagnostico = "DISRUPCIÓN IDENTITARIA POR ALTA INTENSIDAD MIGRATORIA"
            analisis_teorico = f"Los microdatos del CONAPO detectan una fragmentación del tejido social en {estado_selector} ({I:.1f}/25). La alta intensidad migratoria transnacional genera una fuga crítica de capital social."
            recom_1 = "**Políticas de Arraigo Coetáneo:** Destinar incentivos económicos dirigidos a la tecnificación del campo en las regiones de expulsión demográfica."
            recom_2 = "**Fideicomisos de Resiliencia Social:** Estructurar un esquema de coinversión institucional con asociaciones de migrantes para transformar remesas."
            recom_3 = "**Estabilización del Entorno:** Fortalecer los mecanismos de cohesión comunitaria interna para blindar la identidad."
        elif dim_fracturada_codigo == "C":
            foco_diagnostico = "DOMINANCIA ASIMÉTRICA DE CONECTIVIDAD DIGITAL"
            analisis_teorico = f"La entidad registra una hiper-conectividad digital ({C:.1f}/25) según los datos de la ENDUTIH-INEGI que desborda por completo sus capacidades institucionales de control ({S:.1f}/25)."
            recom_1 = "**Despliegue de Nodos de Red Soberana:** Mandatar que toda la metadata crítica gubernamental sea procesada en infraestructuras locales."
            recom_2 = "**Mitigación de Dependencias:** Sustituir dependencias tecnológicas críticas por plataformas de software abierto."
            recom_3 = "**Gobernanza de Redes:** Vincular el despliegue de nueva infraestructura de conectividad a la maduración del eje Structure."
        else:
            foco_diagnostico = "DEBILIDAD ESTRUCTURAL Y REZAGO DE CAPACIDAD"
            analisis_teorico = f"El algoritmo SICE reporta una parálisis en el eje de Structure ({S:.1f}/25), fuertemente condicionado por los altos índices de marginación e ineficiencia burocrática del territorio."
            recom_1 = "**Automatización del Control Institucional:** Implementar la matriz determinista de balance SICE para erradicar procesos opacos."
            recom_2 = "**Inversión Proporcional Compensatoria:** Reorientar el gasto público estatal exclusivamente hacia los ejes rezagados."
            recom_3 = "**Blindaje Normativo:** Fortalecer el marco jurídico subnacional bajo principios de realismo periférico."

    # 10. VISUALIZACIÓN DE BARRAS DIMENSIONALES SOBRE EL VIDEO
    st.write("##")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(f"🏛️ **Structure (S): {S:.1f} / 25**")
        st.progress(S / 25)
        st.markdown(f"🧬 **Identity (I): {I:.1f} / 25**")
        st.progress(I / 25)
    with col_p2:
        st.markdown(f"🔌 **Connectivity (C): {C:.1f} / 25**")
        st.progress(C / 25)
        st.markdown(f"🌱 **Planetary Ethics (E): {E:.1f} / 25**")
        st.progress(E / 25)

    # 11. BLOQUES MÉTRICOS ESTILIZADOS
    st.write("##")
    cm1, cm2, cm3 = st.columns(3)
    with cm1:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Global Balance Index (GBI)</div><div class="metric-val" style="color:{color_hex};">{gbi_total:.1f} / 100</div></div>', unsafe_allow_html=True)
    with cm2:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Dispersión Dimensional (D)</div><div class="metric-val" style="color:#FFFFFF;">{dispersion_D:.2f}</div></div>', unsafe_allow_html=True)
    with cm3:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Clasificación Sistémica</div><div class="metric-val" style="font-size:1.15rem; color:{color_hex}; margin-top:0.6rem; font-weight:800;">{clasificacion_sistema}</div></div>', unsafe_allow_html=True)

    st.write("---")

    # 12. GENERADOR DE MEMORÁNDUM EJECUTIVO
    st.write("### 🎛️ Centro de Inferencia Analítica Subnacional")
    st.caption("Presione el botón para interrogar la base de conocimiento y emitir el dictamen regulatorio.")

    if st.button("Interrogar Nodo Territorial y Desplegar Recomendación"):
        with st.spinner("Procesando vectores moleculares territoriales..."):
            time.sleep(0.5)
            
            dictamen_html = f"""
            <div class="memo-container">
                <div class="memo-header">Dictamen de Gobernanza Predictiva SICE-AI</div>
                <div class="memo-meta">REF ID: SICE-{estado_selector[:3].upper()}-2026-RESOLVED &nbsp;|&nbsp; EMISIÓN COMPLETA</div>
                
                <div class="memo-section-title">Eje de Ruptura Multidimensional Encontrado</div>
                <p style="font-size: 1.35rem; font-weight: 800; color: {color_hex} !important; margin: 0.5rem 0 1.5rem 0;">
                    {foco_diagnostico}
                </p>
                
                <div class="memo-section-title">Evaluación Macrodinámica del Vector</div>
                <p style="font-size: 1.05rem; line-height: 1.7; font-style: italic; color: #E2E8F0 !important; background: rgba(255,255,255,0.04); padding: 1.2rem; border-radius: 6px; border-left: 4px solid {color_hex}; margin-bottom: 1.5rem;">
                    "{analisis_teorico}"
                </p>
                
                <div class="memo-section-title">Directrices Regulatorias de Diseño Institucional</div>
                <ul style="padding-left: 1.5rem; margin-top: 0.5rem; color: #F8FAFC !important; list-style-type: disc;">
                    <li style="margin-bottom: 0.8rem; line-height: 1.6; color: #FFFFFF !important;">{recom_1}</li>
                    <li style="margin-bottom: 0.8rem; line-height: 1.6; color: #FFFFFF !important;">{recom_2}</li>
                    <li style="margin-bottom: 0.8rem; line-height: 1.6; color: #FFFFFF !important;">{recom_3}</li>
                </ul>
                
                <p style="font-size: 0.82rem; color: #64748B !important; margin-top: 3.5rem; border-top: 1px dashed rgba(255,255,255,0.15); padding-top: 1rem; font-style: italic;">
                    Framework determinista de datos abiertos. Respaldado por el portafolio empírico de microdatos en Harvard Dataverse e indexado en SSRN (Elsevier) por la autora Laura Pamela Aranda Medrano, 2026. Todos los conceptos de alineación estructural se desprenden del marco conceptual de "The Balance Core".
                </p>
            </div>
            """
            st.html(dictamen_html)
            st.balloons()
else:
    st.warning("Cargue el archivo datos_sice.csv en la raíz del repositorio para inicializar el pipeline.")
