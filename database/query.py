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

def get_tickers_movement():
    with connection() as con:
        cursor = con.cursor()

        query = f'''
            SELECT DISTINCT ticker
            FROM carteira
        '''

        cursor.execute(query)
        resultados = cursor.fetchall()
        return [r[0] for r in resultados]

def get_operation_by_ticker(ticker: str):
    with connection() as con:
        cursor = con.cursor()

        query = f'''
            SELECT *
            FROM carteira
            WHERE ticker = ?
            ORDER BY data ASC
        '''

        cursor.execute(query, (ticker,))
        resultados = cursor.fetchall()
        return resultados if resultados else {}
    
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

def get_filter_table(tickers: list[str] = None, indicadores: list[str] = None, setor: str = None, segmento: str = None):

    if indicadores is None:
        indicadores = []

    with connection() as con:
        cursor = con.cursor()
        select_col = ['Ticker'] + indicadores
        select_cols_sql = ", ".join([f'"{col.strip()}"' for col in select_col])

        where_clauses = []
        params = []

        for col in indicadores:
            where_clauses.append(f'"{col.strip()}" IS NOT NULL')

        if setor:
            where_clauses.append('"setor" = ?')
            params.append(setor)
        if segmento:
            where_clauses.append('"segmento" = ?')
            params.append(segmento)
        if tickers:
            ticker_clean = [tck.strip() for tck in tickers]
            placeholders = ", ".join(["?"] * len(ticker_clean))    
            where_clauses.append(f'"Ticker" IN ({placeholders})') 
            params.extend(ticker_clean)  

        query = f'''
            SELECT {select_cols_sql}
            FROM stocks
        '''
        if where_clauses:
            query += ' WHERE ' + ' AND '.join(where_clauses)

        order_by = indicadores[0].strip() if indicadores else 'Ticker'
        query += f' ORDER BY "{order_by}" ASC'
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

