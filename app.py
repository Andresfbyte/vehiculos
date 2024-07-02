import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_button= st.button('construir diagrama de dispersion')

if hist_button: # al hacer clic en el boton 
    # escribir un mensaje 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histogramgiga
    fig = px.histogram(car_data, x='odometer') 
    
    #mostrar un grafico plotly interactivo 
    st.plotly_chart(fig, use_container_width=True)
    
if disp_button: # al hacer clic en el boton
    # escribir mensaje
    st.write ('creacion de un diagrama de dispersion')
    #crear un diagrama de dispersion
    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    #mostrar un grafico plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)