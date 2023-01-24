# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:16:06 2022

@author: Usuario
"""
import streamlit as st
import imagen_subida as ims


#ABout the project!
#def add_bg_from_url():
#    st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
#             background-attachment: fixed;
#             background-size: cover
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#add_bg_from_url() 

def textito(idioma):
    
    if idioma == 1:
        st.title('About the project')
        container = st.container()
        st.markdown('<p style="text-align: justify;"><strong>This project of Peripheral Blood Cells Classification have been made by Silvia García, María Ortiz and Jorge González (more information in <em>About us</em> button), for Final Master''s Thesis of the 3th Edition master''s degree in Deep Learning from SaturdaysAI.</strong></p>', unsafe_allow_html=True)
        
        st.markdown('<p style="text-align: justify;">In this project, attention has been focused on the automation of the classification of peripheral blood cells using the <em>Transfer Learning</em> methodology, which consists of using a pre-trained artificial intelligence model, in this case the <em>vgg19</em> model, and training it with an image dataset composed of 8 different classes (basophils, eosinophils, erythroblasts, immature granulocytes, lymphocytes, monocytes, neutrophils, and platelets) of different cell types.</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: justify;">The <em>vgg19</em> pre-trained network architecture; a variant of the <em>vgg</em> model, consisting of 19 layers (16 convolutional and 3 connected layers, 5 MaxPool layers and one Softmax layer). The following image represents the structure of this network:</p>', unsafe_allow_html=True)

        st.image('./images/vgg19.png', use_column_width= True)
        st.markdown('<p style="text-align: justify;">The results obtained were quite promising with a percentage of accuracy in the classification higher than 99% in all classes.</p>', unsafe_allow_html=True)

        st.image('./images/confusion_matrix.png', use_column_width= True)
        st.markdown('<p style="text-align: justify;">This confusion matrix indicates the accuracy of the model when classifying cell types. As can be seen, the <em>vgg19</em> model predicts the different images with great accuracy.</p>', unsafe_allow_html=True)


        st.markdown('<p style="text-align: justify;">Tensorflow Projector (<a href = "https://projector.tensorflow.org/" >https://projector.tensorflow.org/</a>) is a visual tool that allows us to interact and analyze multidimensional data (embeddings) and project them into a two- or three-dimensional space. Each embedding is represented by a point that has a certain position in space and these will form certain clusters based on a similarity score. Thanks to this tool, we are able to observe how the model is capable of distinguishing the different classes (ig, leukocytes, etc), and where it has the greatest problems in distinguishing them through the appearance of certain points of different classes within a cluster of a different class.</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: justify;">Dimensionality reduction methods such as <em>t-stochastic neighbor embedding</em> (<em>t-SNE</em>) allow us to visualize our embeddings in a three-dimensional way, constructing a probability distribution over pairs of embeddings in space, such that the most similar ones are more likely to be included in each other. the same cluster, reducing the dimensionality of the sample.</p>', unsafe_allow_html=True)

  
        st.image('./images/tensor.png', use_column_width= True)
        st.markdown('<p style="text-align: justify;">As can be seen in this figure, there are various insertions of certain groups within clusters belonging to other classes. In this case, the model is more confused giving a correct classification when dealing with neutrophils and immature granulocytes. Other notable insertions are erythroblasts, which are confused with platelets, neutrophils with basophils, and immature granulocytes with monocytes. Even so, the precision of the model when classifying the different cell types is very high.</p>', unsafe_allow_html=True)


        
    else:
        st.title('Acerca del proyecto')
        container = st.container()
        #text_ini = '**Este trabajo de clasificación de células sanguíneas periféricas es un proyecto realizado por Silvia García, María Ortiz y Jorge González (más información en el apartado  *Sobre nosotros*), para el Trabajo de Fin de Máster de la tercera edición del máster en Deep Learning de SaturdaysAI.**'
        st.markdown('<p style="text-align: justify;"><strong>Este trabajo de clasificación de células sanguíneas periféricas es un proyecto realizado por Silvia García, María Ortiz y Jorge González (más información en el apartado  <em>Sobre nosotros</em>), para el Trabajo de Fin de Máster de la tercera edición del máster en Deep Learning de SaturdaysAI.</strong></p>', unsafe_allow_html=True)

        st.markdown('<p style="text-align: justify;">En este proyecto, se ha centrado la atención a la automatización de la clasificación de células sanguíneas periféricas utilizando la metodología de <em>Transfer Learning</em>, la cual consiste en utilizar un modelo de inteligencia artificial pre-entrenado, en este caso el modelo <em>vgg19</em>, y entrenarlo con un dataset de imágenes compuesto por 8 clases diferentes (basófilos, eosinófilos, eritroblastos, granulocitos inmaduros, linfocitos, monocitos, neutrófilos y plaquetas) de diferentes tipos celulares.</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: justify;">La arquitectura de red pre-entrenada <em>vgg19</em>; una variante del modelo <em>vgg</em>, que consta de 19 capas (16 de convolución y 3 capas conectadas, 5 capas de MaxPool y una de Softmax). La siguiente imagen representa la estructura de esta red:</p>', unsafe_allow_html=True)

        #st.write(text_ini)
       # text1 = 'En este proyecto, se ha centrado la atención a la automatización de la clasificación de células sanguíneas periféricas utilizando la metodología de *Transfer Learning*, la cual consiste en utilizar un modelo de inteligencia artificial pre-entrenado, en este caso el modelo *vgg19*, y entrenarlo con un dataset de imágenes compuesto por 8 clases diferentes (basófilos, eosinófilos, eritroblastos, granulocitos inmaduros, linfocitos, monocitos, neutrófilos  y plaquetas)  de diferentes tipos celulares.'
        # =  'La arquitectura de red pre-entrenada *vgg19*; una variante del modelo *vgg*, que consta de 19 capas (16 de convolución y 3 capas conectadas, 5 capas de MaxPool y una de Softmax). La siguiente imagen representa la estructura de esta red:'
       # st.write(text1)
        #st.write(text2)
        st.image('./images/vgg19.png', use_column_width= True)
        st.markdown('<p style="text-align: justify;">Los resultados obtenidos, fueron bastante prometedores con un porcentaje de precisión en la clasificación superior al 99% en todas las clases.</p>', unsafe_allow_html=True)

        #text3 = 'Los resultados obtenidos, fueron bastante prometedores con un porcentaje de precisión en la clasificación superior al 99% en todas las clases.'
        #st.write(text3)
        st.image('./images/confusion_matrix.png', use_column_width= True)
        st.markdown('<p style="text-align: justify;">Esta matriz de confusión nos indica la precisión del modelo a la hora de clasificar los tipos celulares. Como se puede observar, el modelo <em>vgg19</em> predice con gran exactitud las diferentes imágenes.</p>', unsafe_allow_html=True)

        st.markdown('<p style="text-align: justify;">Tensorflow Projector (<a href = "https://projector.tensorflow.org/" >https://projector.tensorflow.org/</a>) es una herramienta visual que nos permite interactuar y analizar datos multidimensionales (embeddings) y proyectarlos en un espacio bi o tridimensional. Cada embedding es representado por un punto que tiene una posición determinada en el espacio y estos formarán determinados clusters basándose en una puntuación de similitud. Gracias a esta herramienta, somos capaces de observar cómo el modelo es capaz de distinguir las diferentes clases (ig, leucocitos, etc), y dónde tiene los mayores problemas para distinguirlas mediante la aparición de ciertos puntos de diferentes clases dentro de un cluster de una clase diferente.</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: justify;">Métodos de reducción de dimensionalidad como <em>t-stochastic neighbor embedding</em> (<em>t-SNE</em>) nos permiten visualizar nuestros embeddings de manera tridimensional, construyendo una distribución de probabilidad sobre parejas de embeddings en el espacio, de forma que los más similares son más probables de incluirse en un mismo cluster, reduciendo la dimensionalidad de la muestra.</p>', unsafe_allow_html=True)

        #text4 = 'Esta matriz de confusión nos indica la precisión del modelo a la hora de clasificar los tipos celulares. Como se puede observar, el modelo *vgg19* predice con gran exactitud las diferentes imágenes.'
        #st.write(text4)
        #text5 = 'Tensorflow Projector (https://projector.tensorflow.org/) es una herramienta visual que nos permite interactuar y analizar datos multidimensionales (embeddings) y proyectarlos en un espacio bi o tridimensional. Cada embedding es representado por un punto que tiene una posición determinada en el espacio y estos formarán determinados clusters basándose en una puntuación de similitud. Gracias a esta herramienta, somos capaces de observar cómo el modelo es capaz de distinguir las diferentes clases (ig, leucocitos, etc), y dónde tiene los mayores problemas para distinguirlas mediante la aparición de ciertos puntos de diferentes clases dentro de un cluster de una clase diferente. '
        #st.write(text5)
        #text6 = 'Métodos de reducción de dimensionalidad como t-stochastic neighbor embedding (t-SNE) nos permiten visualizar nuestros embeddings de manera tridimensional, construyendo una distribución de probabilidad sobre parejas de embeddings en el espacio, de forma que los más similares son más probables de incluirse en un mismo cluster, reduciendo la dimensionalidad de la muestra. '
        #st.write(text6)
        st.image('./images/tensor.png', use_column_width= True)
        st.markdown('<p style="text-align: justify;">Como se puede observar en esta figura, existen diversas inserciones de ciertos grupos dentro de clusters pertenecientes a otras clases. En este caso, el modelo se encuentra más confuso dando una clasificación correcta cuando se trata de neutrófilos y granulocitos inmaduros. Otras inserciones destacables son los eritroblastos, que son confundidos con plaquetas, los neutrófilos con basófilos, y los granulocitos inmaduros con monocitos. Aun así, la precisión del modelo a la hora de clasificar los diferentes tipos celulares es muy alta.</p>', unsafe_allow_html=True)

        #text7 = 'Como se puede observar en esta figura, existen diversas inserciones de ciertos grupos dentro de clusters pertenecientes a otras clases. En este caso, el modelo se encuentra más confuso dando una clasificación correcta cuando se trata de neutrófilos y granulocitos inmaduros. Otras inserciones destacables son los eritroblastos, que son confundidos con plaquetas, los neutrófilos con basófilos, y los granulocitos inmaduros con monocitos. Aun así, la precisión del modelo a la hora de clasificar los diferentes tipos celulares es muy alta.'
        #st.write(text7)