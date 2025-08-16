import streamlit as st
import pandas as pd

from database.query import get_setor, get_segmento, get_columns, get_tickers, get_filter_table
from utils.formatacao import formatar_para_exportar

def painel_tabelas():
    st.title("Visualizador de Indicadores Financeiros - Tabelas")
    graf1, graf2 = st.columns(2)
        
    with graf1: 
        setor_selecionado = st.selectbox(
        "Selecione o setor",[""] +
        get_setor()
        )
        indicadores_selecionados = st.multiselect(
        "Selecionar indicadores",
        get_columns()
        )
    with graf2:
        segmento_selecionado = st.selectbox(
        "Selecione o Segmento",[""] +
        get_segmento(setor_selecionado)
        )        
        ticker_selecionados = st.multiselect(
        "Selecionar Empresas", 
        get_tickers(setor_selecionado, segmento_selecionado)
        )

    if indicadores_selecionados or ticker_selecionados:
        dados = get_filter_table(
            tickers = ticker_selecionados if ticker_selecionados else None,
            indicadores = indicadores_selecionados if indicadores_selecionados else None,
            setor = setor_selecionado if setor_selecionado else None,
            segmento = segmento_selecionado if segmento_selecionado else None
            )

        if dados:
            df = pd.DataFrame(dados, columns=["Ticker"] + indicadores_selecionados)
            df = formatar_para_exportar(df)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhum dado encontrado para os filtros selecionados")
    else:
        st.info("Selecione ao menos um indicador")
            

    
    