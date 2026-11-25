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
    opciones = option_menu("MENÚ: ",['Presentación', 'Experiencia', 'Gráficos'] , 
        icons=['house-door-fill','person-lines-fill', 'graph-up'], menu_icon="filetype-py", default_index=0)

### Opción 2: Menú horizontal
# opciones_2 = option_menu(
#    menu_title="Selecciona una sección: ", 
#    options=['Presentación', 'Experiencia', 'Gráficos'], 
#    icons=['0-circle','1-circle', '2-circle'], 
#    menu_icon="cast", default_index=0, orientation="horizontal")

if opciones == 'Presentación':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: #8f0b24'>Nuestro primer blog 🌐</h1>", unsafe_allow_html=True)

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
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

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
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
    
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
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_3}</div>", unsafe_allow_html=True)
    
elif  opciones == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: #8f0b24'>Nuestra experiencia 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_4 = """
    Vania: "Para mí, aprender a programar resultó un poco caótico. Al principio me sentí un poco confundida y frustrada, ya que era la primera vez que llevaba un curso de este tipo y todo me resultaba completamente nuevo.
    Luego, con el paso de las clases, la programación me enseño a ser más consciente de toda la lógica que hay detrás de los programas que usamos diariamente,
    además de darme los conceptos básicos para entender cómo funciona el código. 
    Lo que más me gustó de programar es saber que puedo aplicar estas herramientas en mi vida profesional ypoder usarlas para ayudar a más personas.
    Por eso, en el futuro me gustaría seguir aprendiendo y mejorando mis habulidades en este ámbito".
    """
    st.markdown(f"<div style='text-align: justify; font-size: 17px;'>{texto_4}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 No son lo mismo pero hablan el mismo idioma: Strings y Listas")
    st.video("https://youtu.be/qiLo8mehgQ8")
    
    # Formato Google Drive
    st.subheader("🎥 Condicionales sin rodeos: La lógica detrás de if, elif y else")
    st.video("https://youtu.be/QMJT7jpJgBg")
    col1, col2, col3 = st.columns([1, 2, 1])

    #with col2:  
        #st.link_button("🎥 Texto del botón",
                #       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                #       use_container_width=True
      #      )

    # Alumno b
    texto_5 = """
    ​Gabriela: "Al principio no sabía nada de programación ni conceptos teóricos, 
    lo que me generaba un poco de estrés al no saber cómo resolver los ejercicios. 
    Sin embargo, programar me enseñó desde la lógica básica como condicionales, bucles, listas y strings hasta comentar el código, 
    importar librerías y limpiar textos usando stopwords. 
    Disfruté mucho dar color y forma a nubes de palabras, 
    gráficos y mapas para presentar datos de manera visual y clara". Además, aprendí a planificar soluciones con documentación y diagramas de flujo aplicadas a proyectos de comunicación. A futuro, me gustaría usar estos gráficos y crear bases de datos para la página de un emprendimiento, logrando así una mejor organización y logística.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 17px;'>{texto_5}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Código SOS: AND, OR y NOT al rescate")
    st.video("https://youtu.be/6ofXrrw5Ats?si=vWkmzEfj1vJPHdQt")
        
    # Formato Google Drive
    st.subheader("🎥 ¡Antes de despachar, if , elif y else deben trabajar!")
    st.video("https://youtu.be/jk8IWn7kIIQ?si=omBO-3PIrNYvPkb7")
    col1, col2, col3 = st.columns([1, 2, 1])
    
   # with col2:  
    #    st.link_button("🎥 Texto del botón",
      #                 "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
       #                use_container_width=True
   #          )

    # Alumno c
    texto_6 = """
    Nahomi: "Al principio aprender a programar fue un poco complicado, puesto que era un entorno completamente ajeno para mí. 
    No comprendía bien cómo operaban ciertas funciones y eso producía que yo cometiera errores al momento de estudiar. 
    Además, considero que, principalmente, la programación me enseñó el lenguaje básico de Python y a tener mucha paciencia. 
    Asimismo, lo que más me gustó de estas experiencias es justo el proceso de programar, si bien es un proceso estresante y tardado, 
    también creo que es divertido el seguir asegurarte de que todo se encuentre bien. En un futuro, me gustaría utilizar estos conocimientos como los mapas o las tablas para complementar proyectos venideros".
    """
    st.markdown(f"<div style='text-align: justify; font-size: 17px;'>{texto_6}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 ¡Aprendamos sobre los valores booleanos son One piece!")
    st.video("https://www.youtube.com/watch?v=Chs67IEBkBs")
        
    # Formato Google Drive
    st.subheader("🎥 ¿Qué harían los Chiikawas? Aprendamos a usar if, elif y else")
    st.video("https://www.youtube.com/watch?v=X9cWQ4BqizE")
    #col1, col2, col3 = st.columns([1, 2, 1])
    
    #with col2:  
     #   st.link_button("🎥 Texto del botón",
      #                 "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
       #                use_container_width=True
        #    )
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: #8f0b24'>Nuestros gráficos logrados💪</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ["Nube de palabras",'Gráfico_1', 'Gráfico_2',"Grafíco_3", 'Mapa_1'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Nube de palabras':
        st.subheader("📊 Nube de palabras: Palabras locas 🔠")
        
        texto_7 = """
        Para la realización de la nube de palabras, trabajé con el primer capítulo del libro Bestiario.Se optó por trabajar con munúsculas para poder indentificar de manera uniforme los términos y evitar la repetición de palabras.
        Mediante .replace() se eliminaron comas, puntos, guiones, paréntesis, signos de interrogación y otros signos de puntuación que normalmente aparecen en los libros. Esto permitió filtrar los términos que no resultan relevantes para el análisis.
        Se tomaron en cuenta preposiciones, conectores,determinantes y palabras que se solían repetir y no sumaban información importante para el análisis. Se conservaron las palabras de mayor importancia en el texto para el análisis.
        Las decisiones tomadas me permmitieron poder filtrar elementos que no eran de mucha importancia como números o el encabezado de la pagina. De esta manera, se logró mostrar los datos relevantes en la nube de palabras. Por otro lado, la elección organizada de los nombres de las variables me ayudó a mantener un orden claro al momento del procesamiento del texto.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_7}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("descarga.png", width=800)

        texto_8 = """
        Elegí trabajar con minúsculas para que una misma palabra se contara de manera uniforme, independientemente de cómo estuviera escrita en el capítulo. Reemplacé por espacios los puntos, comas, puntos y coma, dos puntos, signos de interrogación y exclamación, comillas, paréntesis, guiones y puntos suspensivos, para separar correctamente las palabras. Conservé las tildes y la ñ porque forman parte de su escritura y permiten distinguir significados. Para crear la lista de stopwords seleccioné artículos, preposiciones, conjunciones y pronombres frecuentes, como «el», «de», «y» y «yo», que aportan poca información sobre el contenido de la historia. Estas decisiones permiten agrupar las apariciones de una misma palabra y reducir la presencia de términos gramaticales en el análisis. De esta manera, las frecuencias muestran cuántas veces aparecen las palabras conservadas, y la nube representa con mayor tamaño aquellas que más se repiten en el texto depurado.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_8}</div>", unsafe_allow_html=True)
            
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("nube_gabriela.png", width=800)

        texto_9 = """
        Para desarrollar el análisis en Google Colab, convertí el primer capítulo de Demian de PDF a .txt y lo guardé en la variable libro. Luego normalicé el texto pasándolo a minúsculas (.lower()) y eliminando los signos de puntuación para evitar que una misma palabra se contabilizara como elementos distintos. Tras separar el contenido en una lista de palabras (.split()), la depuré mediante un bucle for con una lista personalizada de stopwords que excluyó artículos, preposiciones, pronombres y verbos muy frecuentes de bajo aporte temático —como era o había, detectados tras una primera prueba—, aunque conservé negaciones como no y nunca por su peso en el sentido de las ideas.
        Con la lista ya filtrada, construí un diccionario (frecuencia_palabras) para contabilizar cuántas veces aparecía cada término en el capítulo. Finalmente, generé una nube de palabras (WordCloud) a partir de estos resultados, configurando un fondo negro, la paleta de colores Pastel1 y los ejes ocultos, logrando así una visualización en la que el tamaño de cada palabra refleja directamente su presencia e importancia dentro del texto.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_9}</div>", unsafe_allow_html=True)
            
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
               st.image("nube_palabras_1_Nahomi.png", width=800)
    
    elif grafico_seleccionado == 'Gráfico_1':
        st.subheader("📊 Gráfico 1: Histogramas")
        
        texto_10 = """
        Cuando Mallorca es local, el equipo alcanzó su mayor cantidad de goles con un gol en 9 partidos. Por otro lado, al jugar como visitante registró la mayor cantidad de goles recibidos con dos goles recibidos en 9 partidos.
        Al comparar los resultados de los gráficos, podemos observar que Mallorca anotó de 1 a 3 goles como local, mientras que, de goles recibidos como visitante fueron entre 2 a 3. Se evidencia una gran diferencia de sus resultados cuando se trata de jugar en casa y fuera de su territorio.
        En conclusión, los resultado muestran que cunado juegan como local tienen un mejor ataque, mientras que cuando son visitantes presentan flaqueza en su defensiva
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_10}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("histograma_vania.png", width=800)
        
        texto_11 = """
        En los 19 partidos como local, el Betis anotó entre 0 y 4 goles por encuentro. Las cantidades más frecuentes fueron 1 y 2 goles, con 6 partidos cada una. En los 19 partidos como visitante, recibió entre 0 y 5 goles por encuentro. En este segundo gráfico también predominaron los valores de 1 y 2 goles, con 7 partidos cada uno. El equipo se quedó sin marcar como local en 2 encuentros y mantuvo su portería a cero como visitante en 3. Ambos gráficos muestran una concentración en 1 y 2 goles, aunque los goles recibidos como visitante alcanzaron un máximo mayor, debido a un partido en el que recibió 5 goles.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_11}</div>", unsafe_allow_html=True)

        col_izq, col_der = st.columns(2)
        with col_izq:
                st.image("histograma_1_gabriela.png", width=800)
        with col_der:
                st.image("histograma_2_gabriela.png", width=200)

        texto_12 = """
        En el primer histograma se observa que Alaves anotó un gol en 8 de sus 19 partidos
        como local, siendo este el resultado más frecuente. También consiguió marcar dos goles
        en 7 encuentros, mientras que en 3 partidos no anotó y solo en uno llegó a marcar
        tres goles. En el segundo histograma, Alavés recibió un gol en 9 partidos como visitante,
        siendo, en este caso, el resultado más frecuente, seguido por los 6 encuentros en los
        que recibió tres goles. Por otro lado, en 2 partidos recibió dos goles y en otros 2
        consiguió terminar el encuentro sin recibir ninguno. Al comparar ambos gráficos, se puede
        observar que los goles anotados como local se concentran principalmente entre uno y dos,
        mientras que en los goles recibidos como visitante destacan tanto los partidos en los que
        recibió uno y tres. En general, los resultados muestran una mayor uniformidad en la
        cantidad de goles que Alavés anota como local, mientras que como visitante existe más
        variabilidad en los goles. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_12}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("Histograma_nahomi.png", width=800)
        
    elif grafico_seleccionado == 'Gráfico_2':
        st.subheader("📊 Gráfico 2: Pastel 😋")
        texto_13 = """
        Se puede concluir que del total de partidos jugados siendo locales, Mallorca acumuló un 47.4% de victorias, un 31.6% de empates y un 21.1% de derrotas. Estos resultados muestran, que el equipo teniendo la posición de local obtuvo buenos resultados, ya que casi la mitad de los datos pertenecen a la categoría de "Ganados", los cuales le ayudaron a sumar puntos en la competencia.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_13}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("grafico_pastel_vania.png", width=800)

        texto_14 = """
        En los 19 partidos del Betis como local se registraron 10 victorias, 6 empates y 3 derrotas. Las victorias representan el 52,6 % del total y constituyen el resultado más frecuente. Los empates equivalen al 31,6 %, mientras que las derrotas representan el 15,8 % y son la categoría menos frecuente. En conjunto, el Betis ganó o empató 16 de sus 19 encuentros como local, por lo que predominaron los partidos en los que evitó la derrota.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_14}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("pastel_gabriela.png", width=800)

        texto_15 = """
        El gráfico circular muestra que, de los 19 partidos que Alavés disputó como local, ganó 7, lo que representa el 36.8 % del total. Por otro lado, perdió 6 encuentros
        y empató otros 6, por lo que ambas categorías representan el mismo porcentaje, con un 31.6 % cada una. Aunque las victorias son el resultado más frecuente, la
        diferencia frente a las derrotas y los empates es pequeña, pues solo existe un partido de diferencia entre cada categoría. En resumen, los resultados como local
        presentan una distribución bastante equilibrada, sin que una de las tres posibilidades predomine sobre las demás.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_15}</div>", unsafe_allow_html=True)
            
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Gráficopastel1_Nahomi.png", width=800)

    elif grafico_seleccionado == 'Grafíco_3':
        st.subheader("📊 Gráfico 3: Gráfico de barras")
        texto_16 = """
        A partir del gráfico se puede interpretar que el promedio de tarjetas rojas que recobieron los equipos cuando jugaron como locales es de 0, ya que ningún equipo presento expulsiones. En conclusión, los resultados demuestran que recibir tarjetas rojas cuando se juega como local representa un escenario poco común durante el torneo.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_16}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("grafico_barras_vania.png", width=800)

        texto_17 = """
        El gráfico compara el promedio de tarjetas amarillas recibidas como visitante por los 20 equipos de La Liga, redondeado al entero más cercano. Trece equipos presentan un promedio redondeado de 2 tarjetas por partido y los otros 7 registran 3. El Betis pertenece al grupo con un promedio redondeado de 2 tarjetas amarillas por encuentro. El redondeo agrupa medias originales diferentes en un mismo valor entero, por lo que dos barras de igual longitud no representan necesariamente promedios exactos iguales.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_17}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("barras_gabriela.png", width=800)

        texto_18 = """
        En el gráfico se observa que el promedio de tarjetas amarillas recibidas por los equipos cuando juegan como visitantes
        se encuentra entre 2 a 3 tarjetas por partido. De los 20 equipos analizados, 13 presentan un promedio de 2 (redondeando)
        tarjetas amarillas, por lo que este es el valor que más repite en el gráfico. Por otro lado, Alaves, Espanyol, Getafe,
        Sevilla, Sociedad, Vallecano y Villarreal alcanzan un promedio de 3 tarjetas (redondeando), Lo que le corresponde a los
        7 equipos restantes. En síntesis, los el gráfico muestran que no existe mucha diferencia entre los equipos, ya que todos
        sus promedios se concentran únicamente en dos valores (también por el redondeo).
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_18}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Barras_horizontales1.png", width=800)


    else:
        st.subheader("🗺️ Mapa: Distribución geográfica")
        texto_19 = """
        Para la creación de la ventana emergente del mapa se eligió una distribución lineal y centrada dentro del bloque (div), generando una lectura más ordenada
        de los datos de los pilotos Sebastian Vettel y Carlos Sainz en la temporada 2016 de F1. La información sigue una jerarquía visual, primero la imagen circular para identificar a 
        cada piloto, seguida de un salto de linea(br) y su nombre en negrita(b). Luego se incluyó la escudería correspondiente de cada piloto en 2016. Finalmente, se añadió el total del
        puntaje acumulado de cada corredor, diferenciando así los perfiles con sus rendimientos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_19}</div>", unsafe_allow_html=True)
            
        with open("mapa_vania.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    
        texto_20 = """
        Para el diseño del mapa interactivo se utilizó la librería Folium, debido a que permite representar información geográfica mediante marcadores y ventanas emergentes. Se seleccionó una distribución organizada para presentar los datos de los pilotos Nico Rosberg y Lewis Hamilton, considerando su participación en la temporada 2016 de Fórmula 1.
        En las ventanas emergentes se utilizaron etiquetas HTML como h3 para destacar el nombre de cada piloto, img para incorporar su fotografía y p para presentar 
        información relacionada con la escudería, la ciudad de nacimiento y el puntaje total obtenido durante la temporada. Asimismo, se emplearon etiquetas b para resaltar los nombres de cada dato y facilitar su identificación.
        La información se organizó de manera ordenada, 
        colocando primero el nombre y la fotografía del piloto, seguido de sus datos principales. 
        También se personalizaron los marcadores mediante diferentes colores e iconos para distinguir a cada participante en el mapa. Finalmente, se incorporó OpenStreetMap como mapa base, incluyendo sus respectivas atribuciones, con el propósito de facilitar la ubicación geográfica de las ciudades de nacimiento y mejorar la presentación visual de los resultados.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_20}</div>", unsafe_allow_html=True)
            
        with open("F1_gabriela.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)

        texto_21 = """
        Para el diseño de la ventana emergente (popup) decidí organizar la información de manera que los datos de cada piloto se pueda
        observar con facilidad. Primero coloqué el nombre del piloto como encabezado, ya que es la información más importante. Después, añadí la escudería.
        Debajo añadí su imagen para que las personas puedan identificarlo y que el popup se vea más visual y dinámico. Decidí que la fotografía sea
        circular, porque considero que se ve más estético y permite que la imagen se destaque, además de que, creo yo, combina con la información
        que va centrada. Luego, el puntaje total. La información que creí más relevante la coloqué en negrita. También decidí centrar todos los elementos
        para que la distribución se vea más ordenada, estética y que la información no se vea amontonada.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 16px;'>{texto_21}</div>", unsafe_allow_html=True)
                    
        with open("mapa_pilotos_Nahomi.html", "r", encoding="utf-8") as mapa:
                        html_content = mapa.read()
            
        components.html(html_content,height=600)
