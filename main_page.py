# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:16:06 2022

@author: Usuario
"""
import streamlit as st
import imagen_subida as ims
from keras.models import load_model
from os import system
#Cargar el modelo
import os
import patoolib
from shutil import rmtree
from os import remove

if os.path.isdir("./model_subir/model") == True:
    rmtree("./model_subir/model/")
if os.path.isfile("./model_subir/test_model.zip") == True:
    remove("./model_subir/test_model.zip")
os.system("cat ./model_subir/vgg19_trainable_true_best_model_pruebita.7z.* > ./model_subir/test_model.zip")

 
patoolib.extract_archive("./model_subir/test_model.zip",outdir="./model_subir/model/")
#model = load_model('../../../model/classification/vgg19_trainable_true_best_model.h5')
model = load_model('./model_subir/model/vgg19_trainable_true_best_model.h5')

size = (224, 224)

def main_page(clicked, label_names):
    title = ims.change_title(clicked)
    labs = ims.change_labels(clicked)
    column1, column2 = st.columns(2)
    holder_up = st.empty()

    with column1:
        st.write('')
        uploaded_image = holder_up.file_uploader('')

    holder_add_text = st.empty()
    with column2:
        additional_text = '' #holder_add_text.write('In order to estimate which is the classification of your image, drop your file at the left')
        
    if uploaded_image:
        #container = st.container()
        add_tex = ims.additional_text_chart(clicked) #
        st.write(add_tex)
        result_texts = ims.result_text(clicked)
        ims.resultados(uploaded_image, model, size, label_names, labs, result_texts)
        #container.markdown(res)
        holder_up.empty()
        holder_add_text.empty()