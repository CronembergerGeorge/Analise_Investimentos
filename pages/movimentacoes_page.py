import datetime
import pandas as pd
import streamlit as st
from database.query import get_filter_table, get_operation_by_ticker, get_tickers, get_tickers_movement
from database.inputs import adicionar_dados, excluir_dados, editar_dados, reajustar_id

def get_dados():
    with st.form('movimentacoes_form'): #pais, data, tipo, operacao, ticker, quantidade, preco_unitario
        pais = st.selectbox("Pais", ['Brasil', 'USA'])
        data = st.date_input("Data da Operação", value=datetime.date.today())
        tipo = st.selectbox("Tipo", ['Stock', 'Reits', 'ETF', 'Açoes', 'Fiis', 'Cripto']) # 'Stock', 'Reits', 'ETF', 'Açoes', 'Fiis', 'Cripto'
        operacao = st.selectbox("Operacao", ['Compra', 'Venda', 'Dividendos', 'JSCP', 'Rend_Tributavel']) #'Compra', 'Venda', 'Dividendos', 'JSCP', 'Rend_Tributavel'
        ticker_disponiveis = get_tickers()
        ticker = st.selectbox('Ticker', ticker_disponiveis)
        if pais == 'Brasil':
            quantidade = st.number_input('Quantidade', min_value=0, step=1)
        else:
            quantidade = st.number_input('Quantidade', min_value=0.0, step=0.1)
        preco_unitario = st.number_input('Preço Unitário', min_value=0.0, step=0.1)

        submitted = st.form_submit_button("Salvar")
        if submitted:
            adicionar_dados(pais, data, tipo, operacao, ticker, quantidade, preco_unitario)
            st.success("Operação salva com sucesso!")

def mostrar_dados():

    tickers_disponiveis = get_tickers_movement()
    ticker_selecionado = st.selectbox("Selecione o ticker", [""] + tickers_disponiveis)

    if ticker_selecionado:
        dados = get_operation_by_ticker(ticker_selecionado)

        if dados:
            df = pd.DataFrame(dados, columns=['id', 'pais', 'data', 'tipo', 'operacao', 'ticker', 'quantidade', 'preco_unitario', 'retido', 'total'])
            st.dataframe(df, use_container_width=True, height=400)
        else:
            st.info("Nenhuma operação encontrada para esse Ticker")
                    
        with st.form("form_excluir_operacao"):
            id_excluir = st.selectbox("Selecione o ID desejado", df['id'])
            submitted = st.form_submit_button("Excluir operação")

            if submitted and id_excluir is not None:
                excluir_dados(id_excluir)
                reajustar_id(id_excluir)
                st.success(f"Operação removida com sucesso '{id_excluir}'")
            
movimentacoes_list = {
    "Adicionar": get_dados,
    "Editar": editar_dados,
    "Excluir": mostrar_dados
    
    }
def painel_movimentacoes():
    st.subheader("Movimentações da carteira")

    options = list(movimentacoes_list.keys())
    
    movimentacao = st.selectbox(
        "Selecione a movimentação desejada", [""] + 
        options
        )

    if movimentacao:
        func = movimentacoes_list[movimentacao]
        func()