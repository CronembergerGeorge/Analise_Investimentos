from db import connection

def all():   
    with connection() as con:
        cursor = con.cursor()
        cursor.execute('''
                SELECT * FROM stocks
                ORDER BY ID ASC
                ''')
        return cursor.fetchall()

def setor():
    with connection() as con:
        cursor = con.cursor()
        cursor.execute('''
                    SELECT setor, COUNT(*) as qnt_stocks
                    FROM stocks
                    GROUP BY setor
                    ORDER BY setor
                    ''')
        return '\n'.join([f'{row[0]} : {row[1]}' for row in cursor.fetchall()])

def segmento():
    with connection() as con:
        cursor = con.cursor()
        cursor.execute('''
                   SELECT segmento, COUNT(*) as qnt_stocks
                   FROM stocks
                   GROUP BY segmento
                   ORDER BY segmento
                   ''')    
        return '\n'.join([f'{row[0]} : {row[1]}' for row in cursor.fetchall()])
    
def get_top_by_column(column="", limit=10):
    with connection() as con:
        cursor = con.cursor()
        query = f'''   
            SELECT Ticker, "{column}"
            FROM stocks
            WHERE "{column}" < 20
            ORDER BY "{column}" ASC
            LIMIT ?
        '''
        cursor.execute(query,(limit,))
        return '\n'.join([f'{row[0]} : {row[1]}' for row in cursor.fetchall()])

def get_columns():
    excluir = ["ID","Nome"]
        
    with connection() as con:
        cursor = con.cursor()
        query = f'''
                PRAGMA table_info(stocks)
        '''
        cursor.execute(query)
        return [col for col in [row[1] for row in cursor.fetchall()] if col not in excluir]
        #return '\n'.join([f'{row[1]}' for row in cursor.fetchall()])

def get_tickers():
    with connection() as con:
        cursor = con.cursor()
        query = f'''
                SELECT DISTINCT Ticker
                FROM stocks
                ORDER BY Ticker
        '''
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]
        

#print(get_top_by_column('P/L', 10))
#print(segmento())
#print(setor())
#print(get_columns())
print(get_tickers())
