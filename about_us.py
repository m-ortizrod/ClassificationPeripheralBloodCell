# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:31:47 2022

@author: Usuario
"""

import streamlit as st
from tensorflow.keras.utils import load_img
import streamlit.components.v1 as components

target_size = (224,224)

def person(url):#(im_path, name, text):
    #im = load_img(im_path, target_size = target_size)
   #st.markdown ("<h1 style='text-align: center;'>name </h1>", unsafe_allow_html=True)
    #components.html(
      #  """    
       # <div 
        #    style="text-align: center"> 
         #   name
        #</div>
        #""",
        #name)

    #st.header(name)
    #st.markdown ("<b style='text-align: center;'>"{}"</b>".format(name), unsafe_allow_html=True))
    #st.image(im)
    url
    st.image(url, width = 100, use_column_width= True )
    #text = '<b style = 'text-align: center';'{}' </b>'
    #st.write(text, use_column_width = True)
    '[![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://es.linkedin.com/in/mar%C3%ADa-ortiz-rodr%C3%ADguez-595964165)'

def unodinoi(idioma):
    if idioma == 1:
        st.title('About the team')
        col1, col2, col3 = st.columns([100,100,100])

        with col1:
            nombre1 = st.markdown('<p style="text-align: center;"><strong>María Ortiz Rodríguez</strong></p>', unsafe_allow_html=True)

            # text = """**B.S in Experimental Sciences,
           # M.S in Computational Biology, and actually PhD student in Biophysics.
            #Her work is focused on understanding the stoichiometry and dynamics of the human mitochondrial DNA replication machinery.**"""
            #text = '''**Graduated in Experimental Sciences from Universidad Rey Juan Carlos and Master in Computational Biology from Universidad Politécnica de Madrid. Currently PhD student in Molecular Motors Lab at IMDEA Nanoscience, where she studies the mechano-chemistry of the molecular motors using single-molecule techniques.** '''

            image1 = 'https://media.licdn.com/dms/image/C4D03AQG-uP0d65Xmxg/profile-displayphoto-shrink_800_800/0/1633675482831?e=1678320000&v=beta&t=4tSZ3b3ZqM6-1BImm5TFqMpiOMdP_g2JLIQvH6631bk'
            #image = load_img('https://media.licdn.com/dms/image/C4D03AQG-uP0d65Xmxg/profile-displayphoto-shrink_800_800/0/1633675482831?e=1678320000&v=beta&t=4tSZ3b3ZqM6-1BImm5TFqMpiOMdP_g2JLIQvH6631bk')
            person(image1)
            text = st.markdown('<p style="text-align: justify;">Graduated in Experimental Sciences from Universidad Rey Juan Carlos and Master in Computational Biology from Universidad Politécnica de Madrid. Currently PhD student in Molecular Motors Lab at IMDEA Nanoscience, where she studies the mechano-chemistry of the molecular motors using single-molecule techniques.</p>', unsafe_allow_html=True)

            
        with col2:
            nombre2 = st.markdown('<p style="text-align: center;"><strong>Jorge González Sierra</strong></p>', unsafe_allow_html=True)

            image2 = 'https://media.licdn.com/dms/image/C4E03AQEhOy-LzpixAg/profile-displayphoto-shrink_800_800/0/1655383235096?e=1678320000&v=beta&t=WQsyJ1eJvxvnI6Z7-WgOYebRYlPwOtQARVVqAOYTPZQ'
            #text = '''**Graduated in Environmental Sciences from the Universidad Autonoma de Madrid and Master in Industrial and Environmental Biotechnology from the Universidad Complutense de Madrid and MBA from the Universidad Francisco de Vitoria. Currently pursuing a PhD in biofuels for aviation and high value-added bioproducts at the Universidad Rey Juan Carlos de Madrid.**'''
            
            person(image2)
            text = st.markdown('<p style="text-align: justify;">Graduated in Environmental Sciences from the Universidad Autonoma de Madrid and Master in Industrial and Environmental Biotechnology from the Universidad Complutense de Madrid and MBA from the Universidad Francisco de Vitoria. Currently pursuing a PhD in biofuels for aviation and high value-added bioproducts at the Universidad Rey Juan Carlos de Madrid.</p>', unsafe_allow_html=True)

        with col3:
            #nombre3 = st.markdown ("<b style='text-align: center;'>Silvia García Hernández </b>", unsafe_allow_html=True)
            nombre3 = st.markdown('<p style="text-align: center;"><strong>Silvia García Hernández</strong></p>', unsafe_allow_html=True)

            image3 = 'https://media.licdn.com/dms/image/C4D03AQFxqX-hVzyPzQ/profile-displayphoto-shrink_800_800/0/1659343843421?e=1678320000&v=beta&t=GAi23Hg4GSvuf1kPjUCkcZ0r3psZ3Ure9_0SXNedW1U'
            #text = '''**Graduated in Electronic Engineering from the University of La Laguna and Master in Artificial Intelligence from the University of Las Palmas. Currently working as Data Scientist at EVM Group where she leads the technical decisions in Artificial Intelligence for projects under development. As fundamental pillars in the professional field, she has continuous learning and help in the development of technological-social initiatives, which is why she is a member of both AdaLoveDev and Python Canarias, and has made presentations at the AdaLoversConf and CESINF VIII events. She enjoys learning and coding in any field related to Data.**'''
            person(image3)
            text = st.markdown('<p style="text-align: justify;">Graduated in Electronic Engineering from the University of La Laguna and Master in Artificial Intelligence from the University of Las Palmas. Currently working as Data Scientist at EVM Group where she leads the technical decisions in Artificial Intelligence for projects under development. As fundamental pillars in the professional field, she has continuous learning and help in the development of technological-social initiatives, which is why she is a member of both AdaLoveDev and Python Canarias, and has made presentations at the AdaLoversConf and CESINF VIII events. She enjoys learning and coding in any field related to Data.</p>', unsafe_allow_html=True)

    else:
        st.title('Sobre nosotros')
        col1, col2, col3 = st.columns([100,100,100])

        with col1:
            nombre1 = st.markdown('<p style="text-align: center;"><strong>María Ortiz Rodríguez</strong></p>', unsafe_allow_html=True)

            #text = ''' **Graduada en Ciencias Experimentales por la Universidad Rey Juan Carlos y Máster en Biología Computacional por la Universidad Politécnica de Madrid. Actualmente realizando el doctorado en Molecular Motors Manipulation Lab en IMDEA Nanociencia, donde estudia la mecano-química de los motores moleculares mediante el uso de las técnica de moléculas individuales.**'''
            image1 = 'https://media.licdn.com/dms/image/C4D03AQG-uP0d65Xmxg/profile-displayphoto-shrink_800_800/0/1633675482831?e=1678320000&v=beta&t=4tSZ3b3ZqM6-1BImm5TFqMpiOMdP_g2JLIQvH6631bk'
            person(image1)
            text = st.markdown('<p style="text-align: justify;">Graduada en Ciencias Experimentales por la Universidad Rey Juan Carlos y Máster en Biología Computacional por la Universidad Politécnica de Madrid. Actualmente realizando el doctorado en Molecular Motors Manipulation Lab en IMDEA Nanociencia, donde estudia la mecano-química de los motores moleculares mediante el uso de las técnica de moléculas individuales.</p>', unsafe_allow_html=True)

        with col2:
            nombre2 = st.markdown('<p style="text-align: center;"><strong>Jorge González Sierra</strong></p>', unsafe_allow_html=True)

            image2 = 'https://media.licdn.com/dms/image/C4E03AQEhOy-LzpixAg/profile-displayphoto-shrink_800_800/0/1655383235096?e=1678320000&v=beta&t=WQsyJ1eJvxvnI6Z7-WgOYebRYlPwOtQARVVqAOYTPZQ'
            #text = '''**Graduado en Ciencias Ambientales por la Universidad Autonoma de Madrid y Máster en Biotecnologia industrial y ambiental por la Universidad Complutense de Madrid y MBA por la Universidad Francisco de Vitoria. Actualmente realizando el doctorado en biocombustibles para aviación y bioproductos de alto valor añadido en la Universidad Rey Juan Carlos de Madrid.**'''
            person(image2)
            text = st.markdown('<p style="text-align: justify;">Graduado en Ciencias Ambientales por la Universidad Autonoma de Madrid y Máster en Biotecnologia industrial y ambiental por la Universidad Complutense de Madrid y MBA por la Universidad Francisco de Vitoria. Actualmente realizando el doctorado en biocombustibles para aviación y bioproductos de alto valor añadido en la Universidad Rey Juan Carlos de Madrid.</p>', unsafe_allow_html=True)

            
        with col3:
            nombre3 = st.markdown('<p style="text-align: center;"><strong>Silvia García Hernández</strong></p>', unsafe_allow_html=True)

            image3 = 'https://media.licdn.com/dms/image/C4D03AQFxqX-hVzyPzQ/profile-displayphoto-shrink_800_800/0/1659343843421?e=1678320000&v=beta&t=GAi23Hg4GSvuf1kPjUCkcZ0r3psZ3Ure9_0SXNedW1U'
            #text = '''**Graduada en Ingeniería Electrónica por la Universidad de La Laguna y Máster en Inteligencia Artificial por la Universidad de Las Palmas. Actual Científica de Datos en Grupo EVM, donde lidera las decisiones técnicas en materia de Inteligencia Artificial de los proyectos en desarrollo. Como pilares fundamentales en el campo profesional posee el aprendizaje continuo y la ayuda al desarrollo de iniciativas tecnológico-sociales, razón por la cual es socia tanto de AdaLoveDev como de Python Canarias, y ha realizado ponencias en los eventos AdaLoversConf y CESINF VIII. Disfruta aprendiendo y trasteando con código sobre cualquier campo relacionado con Datos.**'''
            person(image3)
            text = st.markdown('<p style="text-align: justify;">Graduada en Ingeniería Electrónica por la Universidad de La Laguna y Máster en Inteligencia Artificial por la Universidad de Las Palmas. Actual Científica de Datos en Grupo EVM, donde lidera las decisiones técnicas en materia de Inteligencia Artificial de los proyectos en desarrollo. Como pilares fundamentales en el campo profesional posee el aprendizaje continuo y la ayuda al desarrollo de iniciativas tecnológico-sociales, razón por la cual es socia tanto de AdaLoveDev como de Python Canarias, y ha realizado ponencias en los eventos AdaLoversConf y CESINF VIII. Disfruta aprendiendo y trasteando con código sobre cualquier campo relacionado con Datos.</p>', unsafe_allow_html=True)
