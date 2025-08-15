import streamlit as st

from services.exportar import exportar_excel

#Downlaod arquivo completo
#Downlaod da carteira

def painel_download():
    caminho = exportar_excel()
    with open(caminho, 'rb') as file:
        st.sidebar.download_button(
            label = "Download Arquivo",
            data=file,
            file_name="investimentos_.xlsx",
            mime='application/vdn.openxmlformats-officedocument.spreadsheetml.sheet'
            )