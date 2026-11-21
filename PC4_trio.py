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
        icons=['house-door-fill','person-lines-fill', 'graph-up'], menu_icon="filetype-py", default_index=0)

### Opción 2: Menú horizontal
# opciones_2 = option_menu(
#    menu_title="Selecciona una sección: ", 
#    options=['Presentación', 'Experiencia', 'Gráficos'], 
#    icons=['0-circle','1-circle', '2-circle'], 
#    menu_icon="cast", default_index=0, orientation="horizontal")

if opciones == 'Presentación':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: #2C2966'>NUESTRO PRIMER BLOG</h1>", unsafe_allow_html=True)

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("Vania_imagen.png", caption='Vania', width=300)

    texto = """
    ¡Hola! Soy Vania Gonzales y estudio Publicidad  ㅤ♡. 
    Lo que más me gusta de mi carrera es entender al público para conectar ideas creativas con las personas y lograr comunicar un mensaje óptimo.
    En mi tiempo libre disfruto mucho de las manualidades. Me encanta la repostería, ya que hornear me permite crear cosas dulces y compartirlas con los demás. 
    También tejo crochet, que me relaja y me deja crear proyectos propios.
    Y me gusta la fotografía, porque me permite capturar detalles que a veces pasan desapercibidos.
    Además, mi color favorito es el verde palta. 
    Y me encanta escuchar música, especialmente a Shawn Mendes y Lauryn Hill, que están siempre en mi playlist.
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b
    col1, col2 = st.columns(2)
    
    texto_2 = """
    ¡Hola! Soy Gabriela Chirinos y estudio Publicidad, actualmente curso quinto ciclo ㅤ♡.
    Me considero creativa, organizada e independiente.  
    Me gusta conocer lugares nuevos, tomar fotografías y visitar galerías y museos. 
    Mi color favorito es el rojo y mis géneros musicales preferidos son el rock y el pop, especialmente a Måneskin, que es una de mis bandas favoritas. 
    Me inspira la publicidad que genera cambios sociales mediante ideas innovadoras.  
    A futuro, quiero crear campañas que dejen huella, 
    destacar por mi trabajo y participar en grandes eventos y colaboraciones.
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)
    
    col2.image("Gabriela_imagen.png", caption='Gabriela', width=300)

    # Alumno c
    col1, col2 = st.columns(2)
    
    col1.image("Nahomi_imagen.png", caption='Nahomi', width=300)
    
    texto_3 = """
    ¡Hola! Mi nombre es Nahomi y soy estudiante de Comunicación Audiovisualㅤ♡. 
    Me gusta ver series y películas. También disfruto ver anime, y entre mis favoritos están One Piece y Lovely Complex. 
    Otra de mis actividades favoritas es escuchar música, en especial K-pop y J-pop. 
    Entre mis pasatiempos está la lectura, aunque últimamente no tengo tanto tiempo para dedicarle como me gustaría. 
    Además, me encanta pasar tiempo con mis amigos, ya sea para jugar en internet, conversar o simplemente disfrutar de su compañía. 
    Por último, actualmente, estoy aprendiendo a dibujar y 
    a tejer a crochet.    
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    
elif  opciones == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nuestra experiencia 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_4 = """
    Para mí, aprender a programar resultó un poco caótico. Al principio me sentí un poco confundida y frustrada, ya que era la primera vez que llevaba un curso de este tipo y todo me resultaba completamente nuevo.
    Luego, con el paso de las clases, la programación me enseño a ser más consciente de toda la lógica que hay detrás de los programas que usamos diariamente,
    además de darme los conceptos básicos para entender cómo funciona el código. 
    Lo que más me gustó de programar es saber que puedo aplicar estas herramientas en mi vida profesional ypoder usarlas para ayudar a más personas.
    Por eso, en el futuro me gustaría seguir aprendiendo y mejorando mis habulidades en este ámbito.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 Semejanzas y diferencias(strings y listas)")
    st.video("https://youtu.be/qiLo8mehgQ8")
    
    # Formato Google Drive
    st.subheader("🎥 Estructuras condicionales(if-elif-else)")
    st.video("https://youtu.be/QMJT7jpJgBg")
    col1, col2, col3 = st.columns([1, 2, 1])

    #with col2:  
        #st.link_button("🎥 Texto del botón",
                #       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                #       use_container_width=True
      #      )

    # Alumno b
    texto_5 = """
    ​Al principio no sabía nada de programación ni conceptos teóricos, 
    lo que me generaba un poco de estrés al no saber cómo resolver los ejercicios. 
    Sin embargo, programar me enseñó desde la lógica básica como condicionales, bucles, listas y strings hasta comentar el código, 
    importar librerías y limpiar textos usando stopwords. 
    Disfruté mucho dar color y forma a nubes de palabras, gráficos y mapas para presentar datos de manera visual y clara. Además, aprendí a planificar soluciones con documentación y diagramas de flujo aplicadas a proyectos de comunicación. A futuro, me gustaría usar estos gráficos y crear bases de datos para la página de un emprendimiento, logrando así una mejor organización y logística.

    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
             )

    # Alumno c
    texto_6 = """
    Al principio aprender a programar fue un poco complicado, puesto que era un entorno completamente ajeno para mí. 
    No comprendía bien cómo operaban ciertas funciones y eso producía que yo cometiera errores al momento de estudiar. 
    Además, considero que, principalmente, la programación me enseñó el lenguaje básico de Python y a tener mucha paciencia. 
    Asimismo, lo que más me gustó de estas experiencias es justo el proceso de programar, si bien es un proceso estresante y tardado, 
    también creo que es divertido el seguir asegurarte de que todo se encuentre bien. En un futuro, me gustaría utilizar estos conocimientos como los mapas o las tablas para complementar proyectos venideros.
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

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nuestros gráficos logrados💪</h1>", unsafe_allow_html=True)
    
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
    
