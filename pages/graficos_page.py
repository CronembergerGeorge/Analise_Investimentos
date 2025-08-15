import pandas as pd
import streamlit as st
import plotly.express as px

from database.query import get_columns, get_segmento, get_setor, get_top_10

    #st.sidebar.header("Filtros")
    #ticker_selecionados = st.sidebar.multiselect(
    #    "Selecionar Empresas", 
    #    get_tickers(setor_selecionado, segmento_selecionado)
    #)

    #indicadores_selecionados = st.sidebar.multiselect(
    #    "Selecionar indicadores",
    #    get_columns()
    #)
    #ordem = st.sidebar.radio(
    #    "Ordem do Gráfico",
    #    options = ["Maior valor", "Menor valor"],
    #    index=0
    #)
def painel_graficos():
    pass
if st.sidebar.button("Graficos"):
        
        st.title("Visualizador de Indicadores Financeiros - Gráficos")

        graf1, graf2 = st.columns(2)
        
        with graf1: 
            setor_selecionado = st.selectbox(
                "Selecione o setor",[""] +
                get_setor()
                )
        with graf2:
            segmento_selecionado = st.selectbox(
                "Selecione o setor",[""] +
                get_segmento(setor_selecionado)
                )              

        filtro_coluna = None
        filtro_valor = None
        st.subheader("Grafico de Barras")
        indicador = st.selectbox(
            "Indicador Primário", [""] +
            get_columns(),
            key="indicador_Barra"
            )  
        if setor_selecionado != "":
            filtro_coluna = "setor"
            filtro_valor = setor_selecionado
        if segmento_selecionado != "":
            filtro_coluna = "segmento"
            filtro_valor = segmento_selecionado
        if indicador != "":
            st.subheader("Gráfico Vertical")
            top10_data = get_top_10([indicador], filtro_coluna, filtro_valor, limit=10)
            df = pd.DataFrame(top10_data, columns=["Ticker", indicador])
            fig = px.bar(
                df,
                x="Ticker",
                y=indicador,
                title=f"Top 10 por {indicador} filtrado por {filtro_coluna}"
                )        
            st.plotly_chart(fig,use_container_width=True)
            st.subheader("Gráfico Horizontal")
            fig = px.bar(
                df,
                x=indicador,
                y="Ticker",
                title=f"Top 10 por {indicador} filtrado por {filtro_coluna}",
                orientation='h'
                )        
            st.plotly_chart(fig,use_container_width=True)

        st.subheader("Gráfico Scatter")

        col1, col2 = st.columns(2)
        with col1:
            indicador = st.selectbox(
                "Indicador Primário", [""] +
                get_columns(),
                key="indicador_Scatter_1"
                )
                
        with col2:
            second_indicador = st.selectbox(
                "Indicador Secundário", [""] +
                get_columns(indicador),
                key="indicador_Scatter_2"
                )
        if second_indicador != "":
            top10_data = get_top_10([indicador, second_indicador], filtro_coluna, filtro_valor, limit=10)
            df = pd.DataFrame(top10_data,columns=["Ticker", indicador, second_indicador])
            fig = px.scatter(
                df,
                x = indicador,
                y = second_indicador,
                text="Ticker",
                title=f"{indicador} vs {second_indicador}",
                )
            st.plotly_chart(fig, use_container_width = True)
