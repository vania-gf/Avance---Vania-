# python -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_trio.py

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 1: Menú vertical
with st.sidebar:
    opciones = option_menu("Selecciona una sección: ",['Presentación', 'Experiencia', 'Gráficos'] , 
        icons=['0-circle','1-circle', '2-circle'], menu_icon="filetype-py", default_index=0)

### Opción 2: Menú horizontal
opciones_2 = option_menu(
    menu_title="Selecciona una sección: ", 
    options=['Presentación', 'Experiencia', 'Gráficos'], 
    icons=['0-circle','1-circle', '2-circle'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if opciones == 'Presentación':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre del blog</h1>", unsafe_allow_html=True)

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("ellie.png", caption='Ellie', width=300)

    texto = """
    Aquí escribe una presentación creativa sobre ti.
    ¿Quién eres? 
    ¿De dónde eres? 
    ¿Qué estudias?
    ¿Qué te gusta de tu carrera? 
    ¿Qué te gustaría hacer en el futuro?
    ¿Qué te gusta hacer en tu tiempo libre?
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b
    col1, col2 = st.columns(2)
    
    texto_2 = """
    Aquí escribe una presentación creativa sobre ti.
    ¿Quién eres? 
    ¿De dónde eres? 
    ¿Qué estudias? 
    ¿Qué te gusta de tu carrera? 
    ¿Qué te gustaría hacer en el futuro? 
    ¿Qué te gusta hacer en tu tiempo libre?
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
    
    col2.image("ellie.png", caption='Ellie', width=300)

    # Alumno c
    col1, col2 = st.columns(2)
    
    col1.image("ellie.png", caption='Ellie', width=300)
    
    texto_3 = """
    Aquí escribe una presentación creativa sobre ti.
    ¿Quién eres? 
    ¿De dónde eres? 
    ¿Qué estudias?
    ¿Qué te gusta de tu carrera? 
    ¿Qué te gustaría hacer en el futuro?
    ¿Qué te gusta hacer en tu tiempo libre?
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_3}</div>", unsafe_allow_html=True)
    
elif  opciones == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_4 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )

    # Alumno b
    texto_5 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio?
    ¿Qué te ha enseñado la programación?
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
             )

    # Alumno c
    texto_6 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Gráfico_1':
        st.subheader("📊 Gráfico 1: Lenguas aisladas")
        texto_7 = """
        Interpretación del Gráfico 1
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("aisladas_base_datos.png", width=800)

    elif grafico_seleccionado == 'Gráfico_2':
        st.subheader("📊 Gráfico 2: Familias lingüísticas")
        texto_8 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("lengua_familia_GB.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa 1: Distribución geográfica")
        texto_9 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
            
        with open("mapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    