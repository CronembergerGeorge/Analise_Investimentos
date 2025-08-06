import yfinance as yf
import pandas as pd
import sqlite3
from tabulate import tabulate
from coleta import coletar_dados_completos


conn = sqlite3.connect('data/investimentos.db')
# Baixar dados de ações usando yfinance
tickers = [
    'ABBV', 'ABT', 'ADC', 'ADP', 'AEP', 'ALL', 'AMGN', 'AMSF', 'AMT', 'ARTNA',
    'ATO', 'AVB', 'AVGO', 'AWK', 'BAC', 'BBY', 'BXP', 'CAT', 'C',
    'CINF', 'CL', 'CMS', 'CME', 'CNP', 'COST', 'CSCO', 'CTRE', 'CVS', 'CVX',
    'CUBE', 'DLR', 'DOW', 'DUK', 'DVN', 'EGP', 'ENB', 'EQIX', 'EQR', 'EPRT',
    'ESS', 'EXR', 'FDX', 'GILD', 'GD', 'GS', 'GWRS', 'HMC', 'HON',
    'HPQ', 'HSBC', 'IBM', 'INVH', 'JNJ', 'JPM', 'KIM', 'KMB', 'KO', 'KRC',
    'LIN', 'LMT', 'LRCX', 'LYB', 'MAIN', 'MAA', 'MCD', 'MDT', 'MET', 'MMM',
    'MS', 'MSFT', 'NEE', 'NGG', 'NUE', 'O', 'OHI', 'OKE', 'ORCL', 'PEP', 'PG',
    'PLD', 'PSA', 'PSX', 'PZZA', 'QCOM', 'REG', 'RGCO', 'SLG', 'SO', 'SPG',
    'STAG', 'T', 'TROW', 'TTE', 'UL', 'UNP', 'UPS', 'VICI', 'VTR', 'VZ',
    'WEC', 'WELL', 'WPC', 'XOM'
]
"""
# Teste Unitario
tickers = ['ABBV']
"""
# Iterar sobre os tickers e coletar informações
dados = coletar_dados_completos(tickers)
# Converter a lista de dados em um DataFrame
dados = pd.DataFrame(dados)

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
dados.index = range(1, len(dados) + 1)  # Ajustar o índice para começar em 1
# Salvar o DataFrame no banco de dados
dados.to_sql('stocks', conn, if_exists='replace', index=True, index_label='ID')
# Consultar os dados do banco de dados SQLite
consulta = pd.read_sql_query("SELECT * FROM stocks",conn)

# Salvar dados em um arquivo xlsx
dados.to_excel('data/investimentos.xlsx', index=False)
print("Dados salvos com sucesso")
# Exibir os dados consultados no prompt (Alternativa)

#print(tabulate(consulta, headers='keys', tablefmt='fancy_grid', stralign='center'))

# Fechar a conexão com o banco de dados
conn.close()
