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

#print(get_top_by_column('P/L', 10))
#print(segmento())
print(setor())

