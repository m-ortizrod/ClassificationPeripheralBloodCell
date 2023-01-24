# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 09:25:09 2022

@author: Usuario
"""
from keras.models import load_model
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array, array_to_img
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg19 import preprocess_input, decode_predictions
import matplotlib.pyplot as plt

import numpy as np
from IPython.display import Image, display
import matplotlib.cm as cm

import streamlit as st
from tensorflow.keras.utils import load_img
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import streamlit_toggle as tog
import explicability as ex 

from bokeh.plotting import figure
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum


last_conv_layer_name = "block5_conv4"

def resultados(uploaded_image, model, size, label_names, labs, result_text):
    #st.image(uploaded_image, caption='Celula Sanguinea')
    
    image = load_img(uploaded_image, target_size = size)
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1, 224, 224, 3)

    label = model.predict(img)
    #st.text([np.argmax(label)])
    score = label[0]  


    #st.write(add_text_chart)
    #st.write('La imagen a analizar es la mostrada a continuación. Se podrá analizar la probabilidad de pertenencia a cada tipo de célula sanguínea, así como observar el mapa de calor generado en el apartado de explicabilidad.')
    
    col1, mid, col2 = st.columns([300,300,300]) 
    
    with mid:
        st.image(uploaded_image, width=220, use_column_width=False)

#with col2:
    
    placeholder = st.container()
    tab1, tab2 = placeholder.tabs(labs)#(["Result", "Explicability"])


    with tab1: 
    
        #st.write('Aquí se muestra la probabilidad de la imagen seleccionada de pertenecer a cada clase de célula sanguínea según el modelo de Inteligencia Artificial entrenado.')
        st.write(result_text[0])
        st.write(' ')
        #Bokeh pie chart
        pie = {label_names[0]: np.round(score[0]*100, 2),
               label_names[1]: np.round(score[1]*100, 2),
               label_names[2]: np.round(score[2]*100, 2),
               label_names[3]: np.round(score[3]*100, 2),
               label_names[4]: np.round(score[4]*100, 2),
               label_names[5]: np.round(score[5]*100, 2),
               label_names[6]: np.round(score[6]*100, 2),
               label_names[7]: np.round(score[7]*100, 2)}
        datita = pd.Series(pie).reset_index(name='value').rename(columns={'index': 'country'})
        datita['angle'] = datita['value']/datita['value'].sum() * 2*np.pi
        datita['color'] = Category20c[len(datita)]
        p = figure(height=350, title="", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))
        p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=datita)
        st.bokeh_chart(p)
        
        #=====================
                
        col1, col2, col3, col4, = st.columns([250,250,250,250])
        col1.metric(label_names[0], str(np.round(score[0]*100, 2))+"%")
        col1.metric(label_names[1], str(np.round(score[1]*100, 2))+"%")
        col2.metric(label_names[2], str(np.round(score[2]*100, 2))+"%")
        col2.metric(label_names[3], str(np.round(score[3]*100, 2))+"%")
        col3.metric(label_names[4], str(np.round(score[4]*100, 2))+"%")
        col3.metric(label_names[5], str(np.round(score[5]*100, 2))+"%")
        col4.metric(label_names[6], str(np.round(score[6]*100, 2))+"%")
        col4.metric(label_names[7], str(np.round(score[7]*100, 2))+"%")
        
#chart = pd.DataFrame(np.array(score)*100, label_names)
        #st.bar_chart(chart, use_container_width=True )


        #p = figure(title = '',
        #           x_range = label_names)
        #p.vbar(x = label_names, top = np.array(score)*100)
        #st.bokeh_chart(p, use_container_width= True)

      #  fig, ax = plt.subplots()
       # ax.bar(label_names, np.array(score)*100, color = 'red')
      #  st.pyplot(use_container_width = True)

    with tab2: #Explicabilidad
        
        #st.write('El mapa de calor generado con el algoritmo GRADCAM es el mostrado a continuación. En él se puede observar qué parte de la imagen de entrada ha sido la parte más relevante para el modelo de Inteligencia Artificial en cuanto a clasificación se refiere.')
        st.write(result_text[1])
        col3, col4, col5 = st.columns([300,300,300])
        
        with col4:
            img_array = preprocess_input(ex.get_img_array(uploaded_image, size))

            model.layers[-1].activation = None
            heatmap = ex.make_gradcam_heatmap(img_array, model, last_conv_layer_name)
            
            st.image(ex.save_and_display_gradcam(uploaded_image, heatmap), use_column_width=True)
            
        

def idioma():
    idiomita = tog.st_toggle_switch(label = "", 
                         key = 'he', 
                         default_value = True, 
                         label_after = False, 
                         inactive_color="#ffffff", 
                         active_color="#ffffff", 
                         track_color="#18202b"
                         )
    return idiomita


def change_title(idioma):
    if idioma == 1:
        title = st.title('Peripheral blood cells classification')
        #lab = ["Result", "Explicability"]
        
    else:
        title = st.title('Clasificación de imágenes de células sanguíneas periféricas ')
        #lab = ["neeee", "bruuu"]
    return title
        

            
def change_labels(idioma):
    if idioma == 1:
        labs = ["📈 Result", "📝 Explicability"]
    else:
        labs = ["📈 Resultados", "📝 Explicabilidad"]
        
    return labs




def add_bg_from_url():
    st.markdown(
         """
         <style>
         .stApp {
             background-image: linear-gradient(gray,white);

             background-size: cover
         }
         </style>
         """,
         unsafe_allow_html=True
     )

        
    
def button_image():
    st.markdown(
        f"""
        <button type="submit">
            <img src="https://i.ibb.co/CW5Wvry/buttonpng.png" alt="buttonpng" border="0" />
          </button>
        """)
    
    
def additional_text_chart(idioma):
    if idioma == 1:
        text = 'The following image is going to be analysed. In **Results** you can observe the probability that this cell has to belong to a determined blood cell type, and the color map in **Explicability**'
    else:      
        text = 'La imagen a analizar es la mostrada a continuación. Se podrá analizar la probabilidad de pertenencia a cada tipo de célula sanguínea, así como observar el mapa de calor generado en el apartado de explicabilidad.'
        
    return text

def result_text(idioma):
    if idioma == 1:
        textito_res = 'Here appears the probability of the input image to belong to each blood cell type depending of our IA trained model.'
        textito_exp = 'The color map was generated with GRADCAM algorithm. Here you can observe which part of the input image has been the most relevant part for the IA model in terms of classification.'
        textito = [textito_res, textito_exp]
    else:
        textito_res = 'Aquí se muestra la probabilidad de la imagen seleccionada de pertenecer a cada clase de célula sanguínea según el modelo de Inteligencia Artificial entrenado.'
        textito_exp = 'El mapa de calor generado con el algoritmo GRADCAM es el mostrado a continuación. En él se puede observar qué parte de la imagen de entrada ha sido la parte más relevante para el modelo de Inteligencia Artificial en cuanto a clasificación se refiere.'
        textito = [textito_res, textito_exp]
    return textito

def botoncitos(idioma):
    if idioma == 1:
        label_pj = 'About the project 📕'
        label_us = '  About us  🧝‍♂️  '
        labelcillos = [label_pj, label_us]
    else:
        label_pj = 'Sobre el proyecto 📕'
        label_us = '  Sobre nosotros  🧝‍♂️  '
        labelcillos = [label_pj, label_us]
    return labelcillos