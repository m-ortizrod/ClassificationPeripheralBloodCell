# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:25:05 2022

@author: Usuario
"""

import imagen_subida as ims
import streamlit as st
from keras.models import load_model
from tensorflow.keras.utils import load_img
import sys
import os
import about_pj as pj
import about_us as us
import main_page as mp
#Fondo de streamlit
ims.add_bg_from_url() 

if 'param' not in st.session_state:
    st.session_state.param = 1

def about_project():
    pj.textito(language_button)
    
def ab_us():
    us.unodinoi(language_button)

def language():
    language_button = ims.idioma()
    return language_button

def main_page(param):
    
    if param == 1:
        mp.main_page(language_button, label_names)  
    
    elif param == 2:
        pj.textito(language_button)
    
    elif param == 3:
        us.unodinoi(language_button)
    

#SIDEBAR OPTIONS ======================================
with st.sidebar:

    #cambiar color de los botones
    m = st.markdown("""
                           <style>
                           div.stButton > button:first-child {
                               background-color: #18202b;
                               color:#ffffff;
                               }
                           div.stButton > button:hover {
                               background-color: #522100;
                               color:#ffffff;
                               }
                           </style>""", unsafe_allow_html=True)

    param = 1
        
    col1, col2, col3, col4, col5 = st.columns([20,60,40,60,20])

    with col2:
        st.image('./images/spain_flag.png', width = 60)
    with col3:
        language_button = language()
    with col4:
        st.image('./images/united_kingdom_flag.png', width = 60)
        
    st.markdown("***")
    
    _, colb, _ = st.columns([10,60,20])#([50,80,50])
    with colb:
        botones = ims.botoncitos(language_button)
        home = st.button('  Home  🏠  ')
        project_button = st.button(label = botones[0])#(label = 'About the project 📕')
        us_button = st.button(label = botones[1])#'  About us  🧝‍♂️  ')
        
    st.markdown('---')

#=======================================================



if language_button == 1:
    label_names = ['Basophil', 'Eosinophil', 'Erythroblast', 'Immature gralulocyte', 'Lymphocyte', 'Monocyte', 'Neutrophil', 'Platelet']
else:
    label_names = ['Basófilo', 'Eosinófilo', 'Eritoblasto', 'Granulocitos inmaduros', 'Linfocito', 'Monocito', 'Neutróofilo', 'Plaqueta']
    


if home:
    st.session_state.param = 1
    st.experimental_rerun()
elif project_button:
    st.session_state.param = 2
elif us_button:
    st.session_state.param = 3
    
main_page(st.session_state.param)
    
    
