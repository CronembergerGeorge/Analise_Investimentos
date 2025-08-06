import streamlit as st
import plotly.express as px
import pandas as pd
from db import connection
from query import get_tickers, get_columns, get_top_10, get_segmento, get_setor

st.set_page_config(layout="wide")
st.title("Visualizador de Indicadores Financeiros")

st.sidebar.header("Filtros")

setor_selecionado = st.sidebar.selectbox(
    "Selecione o setor",[""] +
    get_setor()
    )

segmento_selecionado = st.sidebar.selectbox(
    "Selecione o segmento",[""] + 
    get_segmento(setor_selecionado)
    )

ticker_selecionados = st.sidebar.multiselect(
    "Selecionar Empresas", 
    get_tickers(setor_selecionado, segmento_selecionado)
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

if st.sidebar.button("Visualizar Tabela"):
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

elif setor_selecionado != "" and segmento_selecionado != "": 
    st.subheader("Gráfico de Barra")

    filtro_coluna = None
    filtro_valor = None

    if segmento_selecionado != "":
        filtro_coluna = "segmento"
        filtro_valor = segmento_selecionado
    if setor_selecionado != "":
        filtro_coluna = "setor"
        filtro_valor = setor_selecionado
    indicador = st.selectbox(
        "Primário", [""] +
        get_columns(),
        key="indicador 1"
        )  
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
            "Primário", [""] +
            get_columns(),
            key="indicador 2"
            )
            
    with col2:
        second_indicador = st.selectbox(
            "Secundário", [""] +
            get_columns(indicador),
            key="indicador 3"
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

