import sqlite3
import os
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(__file__), "..","data", "investimentos.db")

def connection():
    return sqlite3.connect(DB_PATH, timeout=10)

def salvar_dados(dados: pd.DataFrame, tabela: str = "stocks"):
    dados.index = range(1, len(dados) + 1)
    with connection() as conn:
        dados.to_sql(tabela, conn, if_exists='replace', index=True, index_label='ID')
    print(f"Dados salvos na tabela com sucesso!")
    