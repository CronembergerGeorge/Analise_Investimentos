import streamlit as st
from services.coleta import coletar_dados_completos
from database.db import salvar_dados
from config.config import tickers


def painel_atualizar():
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