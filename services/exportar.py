import pandas as pd
from database.db import connection 
from utils.formatacao import formatar_para_exportar

def exportar_excel():
    conn = connection()
    dados = pd.read_sql_query("SELECT * FROM stocks", conn)
    conn.close()
    
    dados = formatar_para_exportar(dados)
    
    dados.to_excel('data/investimentos.xlsx', index=False)
    return 'data/investimentos.xlsx'