from database.db import connection

def get_setor():
    with connection() as con:
        cursor = con.cursor()
        query = f'''
            SELECT DISTINCT setor
            FROM stocks
            WHERE setor IS NOT NULL
            ORDER BY setor
            '''
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]
    
def get_segmento(setor:str=None):
    with connection() as con:
        cursor = con.cursor()
        query = f'''
            SELECT DISTINCT segmento
            FROM stocks
            WHERE 1=1
            '''
        params = []
        if setor:
            query += " AND setor = ?"
            params.append(setor)

        query += ' ORDER BY Ticker'
        
        cursor.execute(query, params)    
        return [row[0] for row in cursor.fetchall()]
    
def get_tickers(setor:str=None, segmento:str=None):
    with connection() as con:
        cursor = con.cursor()
        query = f'''
            SELECT Ticker
            FROM stocks
            WHERE 1=1
        '''
        params = []
        if setor:
            query += ' AND setor = ?'
            params.append(setor)
        if segmento:
            query += ' AND segmento = ?'
            params.append(segmento)

        query += ' ORDER BY Ticker'
        cursor.execute(query, params)
        return [row[0] for row in cursor.fetchall()]
    
def get_top_10(column:list[str], filter_col:str= None, filter_val: str=None, limit=10):
    with connection() as con:
        cursor = con.cursor()
        select_cols = ", ".join([f'"{col}"' for col in ['Ticker'] + column])
        query = f'''
            SELECT {select_cols}
            FROM stocks
            WHERE {" AND ".join([f'"{col}" IS NOT NULL' for col in column])}
        '''
        params = []
        if filter_col and filter_val:
            query += f'AND "{filter_col}" = ?'
            params.append(filter_val)
        query += f'ORDER BY "{column[0]}" ASC LIMIT ?'
        params.append(limit)

        cursor.execute(query,params)
        return cursor.fetchall()
        
def get_columns(indicador:str = None):
    excluir = ["ID","Nome","Setor", "Segmento", "Ticker","52-Week Low", "52-Week High", "Ultimo Dividendo ($)", "Último Pagamento(Data)", "Proximo Dividendo(Data)", "Ultima Atualização",indicador]
        
    with connection() as con:
        cursor = con.cursor()
        query = f'''
                PRAGMA table_info(stocks)
        '''
        cursor.execute(query)
        return [col for col in [row[1] for row in cursor.fetchall()] if col not in excluir]
    