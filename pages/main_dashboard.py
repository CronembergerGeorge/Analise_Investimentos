import streamlit as st
from pages.dashboard_page import painel_dashboard
from pages.movimentacoes_page import painel_movimentacoes
from pages.atualizar_page import painel_atualizar
from pages.download_page import painel_download
from pages.graficos_page import painel_graficos
from pages.tabelas_page import painel_tabelas

def abrir_fechar_painel(key: str, botoes):
    for botao in botoes:
        st.session_state[botao] = (botao == key) and (not st.session_state[botao])

painels = {
    "Dashboard Carteira": painel_dashboard, 
    "Movimentações": painel_movimentacoes, 
    "Analisar Gráficos": painel_graficos, 
    "Gerar Tabelas": painel_tabelas,  
    "Atualizar Dados": painel_atualizar, 
    "Download Arquivo": painel_download, 
    }
            
def show():
    st.set_page_config(layout="wide")

    st.sidebar.header("~Painel")

    botoes = list(painels.keys())
    
    for botao in botoes:
        if botao not in st.session_state:
            st.session_state[botao] = False
    
    for botao in botoes:
        st.sidebar.button(f"{botao}", on_click=abrir_fechar_painel, args=(botao,botoes))

    painel_ativo = None
    for botao, func in painels.items():
        if st.session_state[botao]:
            painel_ativo = func
            break
    if painel_ativo:
        painel_ativo()
    else:
        st.header("Gráfico de distribuição da Carteira")
                 
if __name__ == "__main__":
    show()