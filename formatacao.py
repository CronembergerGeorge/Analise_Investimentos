import pandas as pd

def formatar_valor(valor): # Formata valores monetarios com simbolo de dolar e duas casas decimais
    try:
        if pd.isna(valor): #Verifica se o valor é NaN
            return "N/A" 
        valor_float = float(valor) # Converte o valor para float
        return f"${valor_float:,.2f}" # Formata como moeda com 2 casas decimais
    except (ValueError, TypeError): # Captura erros de conversão
        return "N/A" 

def formatar_percentual(valor):
    try:
        if pd.isna(valor):
            return "N/A"
        valor_float = float(valor)
        return f'{valor_float:.2f}%'
    except (ValueError, TypeError):
        return "N/A"

def formatar_numeros(valor):
    try:
        if pd.isna(valor):
            return "N/A"
        valor_float = float(valor)
        return round(valor_float,2)
    except (ValueError, TypeError):
        return "N/A"

def formatar_data(data):
    try:
        if pd.isna(data):
            return "N/A"
        dt = pd.to_datetime(data, unit='s')  # converte timestamp UNIX
        return dt.date()  # retorna só a data (sem tempo)
    except (ValueError, TypeError):
        return "N/A"

def formatar_bilhoes(x, pos):
    if pd.isna(x):
        return "N/A"
    try:
        valor_em_bilhoes = x / 1e9
        return f'{valor_em_bilhoes:,.0f}'
    except (ValueError, TypeError):
        return "N/A"
    
