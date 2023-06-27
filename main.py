import streamlit as st
import pandas as pd
st.set_page_config(page_title= "seu site")

with st.container():

    st.subheader('seu site')
    st.title("Controle de contratos")
    st.write("quer fechar contrato conosco?[ entre em contato!](https://linktr.ee/Junior_vasconcelos)")
    st.write("Informações sobre os contratos fechados ao longo do mes de maio")


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('resultados.py.csv')
    return  tabela

with st.container():
    st.write ()
    dados = carregar_dados()
    qnt_dias = st.selectbox('selecione o periodo',['7D' ,'15D', '20D', '5D'] )
    num_dias = int(qnt_dias.replace('D',"" ))
    dados = carregar_dados()
    dados = dados [-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')

