from database.db import connection

def adicionar_dados(pais, data, tipo, operacao, ticker, quantidade, preco_unitario):
    with connection() as con:
        cursor = con.cursor()

        total = quantidade * preco_unitario
        retido = 0
        
        if pais == 'Brasil' and operacao in ['JSCP', 'Rend_Tributavel']:
            retido = 0.15
        elif pais == 'USA' and operacao == 'Dividendos':
            retido = 0.30

        total_liquido = total * (1 - retido)
            
        query = f'''
            INSERT INTO carteira (pais, data, tipo, operacao, ticker, quantidade, preco_unitario, retido, total)
            VALUES (?,?,?,?,?,?,?,?,?)
        '''

        params = (pais, data, tipo, operacao, ticker, quantidade, preco_unitario, retido, total_liquido)
        cursor.execute(query, params)
        con.commit()
    
def editar_dados():
    pass
def excluir_dados(id: int):
    with connection() as con:
        cursor = con.cursor()

        query = f'''
            DELETE FROM carteira
            WHERE id = ?
        '''

        cursor.execute(query, (id,))
        con.commit()

def reajustar_id(id_excluido):
    with connection() as con:
        cursor = con.cursor()
        cursor.execute("UPDATE carteira SET id = id - 1 WHERE id > ?", (id_excluido,))    
        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM carteira) WHERE name='carteira")
        con.commit()
    