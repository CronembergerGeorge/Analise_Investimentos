import streamlit as st
import plotly.express as px
import pandas as pd
from db import connection
from query import get_tickers, get_columns

st.title("Visualizador de Indicadores Financeiros")

st.sidebar.header("Filtros")

ticker_selecionados = st.sidebar.multiselect(
    "Selecionar Empresas",
    get_tickers()
)

indicadores_selecionados = st.sidebar.multiselect(
    "Selecionar indicadores",
    get_columns()
)

ordem = st.sidebar.radio(
    "Ordem do Gráfico",
    options = ["Maior valor", "Menor valor"],
    index=0
)

if st.sidebar.button("Visualizar Dados"):
    if not ticker_selecionados or not indicadores_selecionados:
        st.warning("Selecione pelo menos um Ticker e um Indicador")
    else:
        colunas = ", ".join(['Ticker'] + [f'"{col}"' for col in indicadores_selecionados])
        placeholders = ", ".join(['?'] * len(ticker_selecionados))
        
        query = f'''
        SELECT {colunas}
        FROM stocks
        WHERE Ticker IN ({placeholders})
        '''
        
        with connection() as con:
            df = pd.read_sql_query(query, con, params = ticker_selecionados)
            
        st.dataframe(df)
        
        if len(indicadores_selecionados) == 1:
            indicador = indicadores_selecionados[0]
            df_sorted = df.sort_values(by=indicador, ascending=(ordem == "Menor valor"))
            
            fig = px.bar(
                df_sorted,
                x="Ticker",
                y=indicador,
                title=f"{indicador} por Ticker ({ordem})",
                text_auto=True
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Selecione apenas 1 indicador para visualizar o grafico")