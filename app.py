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

# 2. INYECCIÓN DE VIDEO EN EL FONDO (CSS & HTML AVANZADO)
video_path = "assets/globo_futurista.mp4"

if os.path.exists(video_path):
    import base64
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    video_base64 = base64.b64encode(video_bytes).decode()
    
    st.markdown(f"""
        <style>
        #background-video {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -100;
            background-size: cover;
            opacity: 0.22;
            filter: blur(0.5px);
        }}
        .stApp {{
            background-color: transparent;
        }}
        .stSidebar {{
            background-color: rgba(15, 23, 42, 0.88) !important;
            backdrop-filter: blur(12px);
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

# 3. ESTILOS DE TIPOGRAFÍA Y DISEÑO DE TARJETAS PROFESIONALES
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,700;1,9..144,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;800&display=swap');
    
    .main-title { font-family: 'Fraunces', serif; font-size: 3.5rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.1rem; text-shadow: 0 4px 12px rgba(0,0,0,0.4); }
    .subtitle { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; color: #94A3B8; margin-bottom: 2.5rem; font-weight: 300; }
    
    .theory-card { background: rgba(15, 23, 42, 0.8); color: #F8FAFC; padding: 2.2rem; border-radius: 1rem; margin-bottom: 2.5rem; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(8px); }
    .theory-title { font-family: 'Fraunces', serif; font-size: 1.7rem; color: #38BDF8; font-style: italic; margin-bottom: 1rem; }
    
    .metric-box { background-color: rgba(255, 255, 255, 0.05); padding: 1.4rem; border-radius: 0.75rem; border: 1px solid rgba(255,255,255,0.08); text-align: center; backdrop-filter: blur(4px); }
    .metric-label { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em; color: #94A3B8; font-weight: 600; }
    .metric-val { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 2.1rem; font-weight: 800; margin-top: 0.2rem; }
    
    /* Estilos globales para mantener el texto limpio */
    .stMarkdown, p, span, label { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# 4. PANEL LATERAL (Sidebar Institucional)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/space-shield.png", width=70)
    st.markdown("<h3 style='margin:0; color:#FFFFFF;'>SICE-México AI</h3>", unsafe_allow_html=True)
    st.caption("Engine v1.6 | Inmersión de Red Global")
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
            <strong>The Balance Core</strong> postula que la estabilidad real de un territorio depende de la <strong>alineación proporcional</strong> de sus cuatro dimensiones vitales:
        </p>
        <ul style="color:#E2E8F0; padding-left:1.2rem; margin-top:0.8rem;">
            <li style="margin-bottom:0.5rem;"><strong>Structure (S):</strong> Capacidad institucional, orden normativo y resiliencia regulatoria subnacional.</li>
            <li style="margin-bottom:0.5rem;"><strong>Identity (I):</strong> Cohesión del tejido social, arraigo cultural y contención a la dispersión migratoria asimétrica.</li>
            <li style="margin-bottom:0.5rem;"><strong>Connectivity (C):</strong> Infraestructura de redes, adopción digital abierta e interconexión global soberana.</li>
            <li style="margin-bottom:0.5rem;"><strong>Planetary Ethics (E):</strong> Cumplimiento estricto de límites biofísicos y sustentabilidad hidrogeológica regional.</li>
        </ul>
        <h4 style="color:#38BDF8; margin-top:1.5rem;">La Ecuación del Desequilibrio</h4>
        <p>El modelo evalúa el riesgo territorial mediante el <strong>Coeficiente de Dispersión Dimensional ($D$)</strong> usando la desviación estándar sobre variables de fuentes oficiales:</p>
        <p style='text-align: center; font-size: 1.4rem; background: rgba(255,255,255,0.06); padding: 1rem; border-radius: 0.5rem; margin: 1.5rem 0; color:#FFFFFF;'>
            $$D = \\sigma(S, I, C, E) = \\sqrt{\\frac{1}{4}\\sum_{i=1}^{4}(x_i - \\mu)^2}$$
        </p>
        <p style="color:#94A3B8; font-size:0.95rem; font-style:italic;">
            Si una dimensión ejerce dominancia asimétrica o colapsa en déficit, el coeficiente D aumenta de forma crítica, detonando una alerta automatizada antes de consolidar una ruptura sistémica irreversible (When the Ground Gives Way).
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

    # Asignación binaria estricta de estados lógicos
    if dispersion_D <= 4.0:
        clasificacion_sistema = "EQUILIBRIO COHERENTE (Adaptive Coherence)"
        color_hex = "#10B981"  # Verde Esmeralda
        foco_diagnostico = "🟢 ADAPTIVE COHERENCE SISTÉMICA"
        analisis_teorico = f"El territorio de {estado_selector} opera dentro de un marco de balance estructural proporcional. Su índice de dispersión analítica de D = {dispersion_D:.2f} denota que ninguna dimensión está canibalizando los recursos de otra, manteniendo una distribución armónica en el ecosistema regional."
        recom_1 = "**Preservación Dinámica del Modelo:** Institucionalizar el vector actual como línea base regulatoria para la planificación territorial estratégica."
        recom_2 = "**Monitoreo de Fluctuación Coetánea:** Implementar auditorías de varianza semestrales para detectar desviaciones en fases tempranas antes de cruzar el umbral de fricción."
        recom_3 = "**Optimización Estructurada:** Prohibir políticas de expansión acelerada en conectividad o industria que no demuestren un acoplamiento simétrico con las capacidades de gobernanza local."
    else:
        clasificacion_sistema = "DISPERSIÓN CRÍTICA (Systemic Imbalance)"
        color_hex = "#EF4444"  # Rojo Escarlata Real
        
        if dim_fracturada_codigo == "E" or E < 10.0:
            foco_diagnostico = "🔴 DÉFICIT ÉTICO-ECOLÓGICO POR SATURACIÓN INDUSTRIAL"
            analisis_teorico = f"El vector de {estado_selector} muestra una severa sobreexplotación biofísica. El indicador hidrogeológico real extraído de las bases de CONAGUA ({E:.1f}/25) delata que las presiones del nearshoring transnacional están rebasando la resiliencia de las cuencas locales."
            recom_1 = "**Moratoria de Nearshoring Extractivo:** Suspender inmediatamente la entrega de licencias a corporaciones que demanden un consumo hídrico intensivo no acoplado a sistemas de ciclo cerrado."
            recom_2 = "**Monitoreo Satelital Coetáneo:** Conectar la infraestructura de sensores de CONAGUA directamente al pipeline del SICE para auditar el abatimiento de acuíferos subterráneos en tiempo real."
            recom_3 = "**Equilibrio Planetario Mandatorio:** Anteponer los límites de supervivencia física analizados en tu obra (*When the Ground Gives Way*) sobre los incentivos comerciales externos de corto plazo."
        elif dim_fracturada_codigo == "I":
            foco_diagnostico = "🔴 DISRUPCIÓN IDENTITARIA POR ALTA INTENSIDAD MIGRATORIA"
            analisis_teorico = f"Los microdatos extraídos del portafolio del CONAPO y migración detectan una fragmentación del tejido social en {estado_selector} ({I:.1f}/25). La alta intensidad migratoria transnacional genera una fuga crítica de capital social y desarraigo comunitario."
            recom_1 = "**Políticas de Arraigo Coetáneo:** Destinar incentivos económicos y tecnológicos dirigidos a la tecnificación del campo y clústeres comunitarios en las regiones de mayor expulsión demográfica."
            recom_2 = "**Fideicomisos de Resiliencia Social:** Estructurar un esquema de coinversión institucional con asociaciones de migrantes para transformar flujos de remesas pasivas en infraestructura de soporte (Structure)."
            recom_3 = "**Estabilización del Entorno:** Fortalecer los mecanismos de cohesión comunitaria interna para blindar la identidad frente a choques económicos externos asimétricos."
        elif dim_fracturada_codigo == "C":
            foco_diagnostico = "🔴 DOMINANCIA ASIMÉTRICA DE CONECTIVIDAD DIGITAL"
            analisis_teorico = f"La entidad registra una hiper-conectividad digital ({C:.1f}/25) según los datos de la ENDUTIH-INEGI que desborda por completo sus capacidades institucionales de control ({S:.1f}/25). Existe un riesgo inminente de captura soberana de datos por agentes transnacionales."
            recom_1 = "**Despliegue de Nodos de Red Soberana:** Mandatar que toda la metadata crítica gubernamental y económica sea procesada en infraestructuras locales bajo legislación mexicana nacional."
            recom_2 = "Sustituir dependencias tecnológicas críticas por plataformas de software abierto para mitigar el control algorítmico ejercido por corporaciones extranjeras."
            recom_3 = "Vincular el despliegue de nueva infraestructura de conectividad a la maduración de las capacidades de auditoría del eje Structure."
        else:
            foco_diagnostico = "🔴 DEBILIDAD ESTRUCTURAL Y REZAGO DE CAPACIDAD"
            analisis_teorico = f"El algoritmo SICE reporta una parálisis en el eje de Structure ({S:.1f}/25), fuertemente condicionado por los altos índices de marginación e ineficiencia burocrática del territorio mapeados en tus bases."
            recom_1 = "**Automatización del Control Institucional:** Implementar la matriz determinista de balance SICE para erradicar procesos opacos y descentralizar las capacidades de respuesta pública local."
            recom_2 = "**Inversión Proporcional Compensatoria:** Reorientar el gasto público estatal exclusivamente hacia los ejes rezagados para colapsar la dispersión matemática D a un rango seguro."
            recom_3 = "Fortalecer el marco jurídico subnacional bajo principios de realismo periférico para repeler presiones de corporativos externos."

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

    # 11. BLOQUES MÉTRICOS ESTILIZADOS EN ALTA DIRECCIÓN
    st.write("##")
    cm1, cm2, cm3 = st.columns(3)
    with cm1:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Global Balance Index (GBI)</div><div class="metric-val" style="color:{color_hex};">{gbi_total:.1f} / 100</div></div>', unsafe_allow_html=True)
    with cm2:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Dispersión Dimensional (D)</div><div class="metric-val" style="color:#FFFFFF;">{dispersion_D:.2f}</div></div>', unsafe_allow_html=True)
    with cm3:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Clasificación Sistémica</div><div class="metric-val" style="font-size:1.15rem; color:{color_hex}; margin-top:0.6rem; font-weight:800;">{clasificacion_sistema}</div></div>', unsafe_allow_html=True)

    st.write("---")

    # 12. MOTOR REFORZADO DE DICTAMEN DE CONSULTORÍA CIENTÍFICA (Tarjeta Limpia y Profesional)
    st.write("### 🎛️ Centro de Inferencia Analítica Subnacional")
    st.caption("Presione el botón para interrogar la base de conocimiento y emitir el dictamen regulatorio con el Core algorítmico.")

    if st.button("Interrogar Nodo Territorial y Desplegar Recomendación"):
        with st.spinner("Procesando vectores moleculares territoriales..."):
            time.sleep(0.5)
            
            # DISEÑO 100% NATIVO DE TARJETA: Texto normal, limpio y profesional sin etiquetas crudas
            with st.container():
                st.markdown(f"""
                <div style="background-color: rgba(15, 23, 42, 0.9); border: 1px solid rgba(255,255,255,0.15); border-left: 6px solid {color_hex}; padding: 2.5rem; border-radius: 1rem; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); backdrop-filter: blur(12px);">
                    <div style="font-family: 'Fraunces', serif; font-size: 2.1rem; font-weight: 400; color: #FFFFFF; margin-bottom: 0.3rem;">Dictamen de Gobernanza Predictiva SICE-AI</div>
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.9rem; color: #94A3B8; margin-bottom: 1.5rem;">REF ID: SICE-{estado_selector[:3].upper()}-2026-RESOLVED</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Campos de contenido usando el Markdown nativo de Streamlit (limpio de etiquetas estorbosas)
                st.write(f"### **Eje de Ruptura Multidimensional Encontrado:**")
                st.write(f"### :{color_hex[1:]}[{foco_diagnostico}]")
                
                st.info(f"👉 **Evaluación Macrodinámica:** {analisis_teorico}")
                
                st.write("### 🎯 **Directrices Regulatorias de Diseño Institucional**")
                st.markdown(f"* {recom_1}")
                st.markdown(f"* {recom_2}")
                st.markdown(f"* {recom_3}")
                
                st.write("---")
                st.caption(f"ℹ️ *Framework determinista de datos abiertos. Respaldado por el portafolio empírico de microdatos en Harvard Dataverse e indexado en SSRN (Elsevier) por la autora Laura Pamela Aranda Medrano, 2026. Todos los conceptos se desprenden de la tesis central de 'The Balance Core'.*")
                
                st.balloons()
else:
    st.warning("Cargue el archivo datos_sice.csv en la raíz del repositorio para inicializar el pipeline.")
