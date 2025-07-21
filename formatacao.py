import pandas as pd
def formatar_valor(valor):
    try:
        if pd.isna(valor):
            return "N/A"
        valor_float = float(valor)
        return f"${valor_float:,.2f}"
    except (ValueError, TypeError):
        return "N/A"

def formatar_percentual(valor):
    try:
        if pd.isna(valor):
            return "N/A"
        valor_float = float(valor)
        return f'{valor_float:.2%}'
    except (ValueError, TypeError):
        return "N/A"

def formatar_numeros(valor):
    try:
        if pd.isna(valor):
            return "N/A"
        valor_float = float(valor)
        return f'{valor_float:,.2f}'
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

