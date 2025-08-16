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
    
def criar_tabela():
    with connection() as con:
        cursor = con.cursor()

        query = f'''
            CREATE TABLE IF NOT EXISTS carteira (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pais TEXT NOT NULL,
                data TEXT NOT NULL,
                tipo TEXT CHECK(tipo IN ('Stock', 'Reits', 'ETF', 'Açoes', 'Fiis', 'Cripto')),
                operacao TEXT CHECK(operacao IN ('Compra', 'Venda', 'Dividendos', 'JSCP', 'Rend_Tributavel')) NOT NULL,
                ticker TEXT NOT NULL,
                quantidade REAL NOT NULL,
                preco_unitario REAL NOT NULL,
                retido REAL NOT NULL DEFAULT 0,
                total REAL NOT NULL
                )
        '''
        cursor.execute(query)
        con.commit()

def excluir_tabela():
    with connection() as con:
        cursor = con.cursor()

        query = f'''
            DROP TABLE carteira
        '''
        cursor.execute(query)
        con.commit()
    