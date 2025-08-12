import streamlit as st
import plotly.express as px
import pandas as pd
from query import get_tickers, get_columns, get_top_10, get_segmento, get_setor
from exportar import exportar_excel
from coleta import coletar_dados_completos
from config import tickers
from db import salvar_dados

st.set_page_config(layout="wide")

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

st.sidebar.header("Filtros")

setor_selecionado = st.sidebar.selectbox(
    "Selecione o setor",[""] +
    get_setor()
    )
segmento_selecionado = st.sidebar.selectbox(
    "Selecione o setor",[""] +
    get_segmento(setor_selecionado)
    )

if setor_selecionado != "" and segmento_selecionado != "":
    st.title("Visualizador de Indicadores Financeiros - Gráficos")

    graf1, graf2 = st.columns(2)
    
    with graf1:   
        filtro_coluna = None
        filtro_valor = None

        if setor_selecionado != "":
            filtro_coluna = "setor"
            filtro_valor = setor_selecionado
        if segmento_selecionado != "":
            filtro_coluna = "segmento"
            filtro_valor = segmento_selecionado
        indicador = st.selectbox(
            "Indicador Primário", [""] +
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
            "Indicador Primário", [""] +
            get_columns(),
            key="indicador 2"
            )
            
    with col2:
        second_indicador = st.selectbox(
            "Indicador Secundário", [""] +
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

if st.sidebar.button("Atualizar dados"):
    with st.spinner("Coletando dados..."):
        dados = coletar_dados_completos(tickers)
        colunas_ordenadas = [
        'Ticker', 'Nome', 'Setor', 'Segmento', '5Y Dividendo', 'Div Yield (%)',
        '52-Week Low', 'Preço Atual', '52-Week High', 
        'Beta', 'P/L', 'P/L Future', 'P/VP', 
        'ROE (%)', 'Margem Líquida (%)',
        'Payout Ratio', 'Receita', 'Lucro',
        'Free Cash Flow', 'EV/EBITDA', 'Divida/EBITDA',
        'Crescimento receita', 'Crescimento lucro',
        'Ultimo Dividendo ($)', 'Último Pagamento(Data)', 'Proximo Dividendo(Data)',
        'Market Cap (B)',
        'Ultima Atualização'
        ]
        dados = dados[colunas_ordenadas]
        # Salvar os dados no banco de dados SQLite

        salvar_dados(dados)
    st.dataframe(dados)

caminho = exportar_excel()

with open(caminho, 'rb') as file:
    st.sidebar.download_button(
        label = "Download Arquivo",
        data=file,
        file_name="investimentos_.xlsx",
        mime='application/vdn.openxmlformats-officedocument.spreadsheetml.sheet'
        )