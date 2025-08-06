import pandas as pd
import yfinance as yf
from formatacao import formatar_data, formatar_valor, formatar_percentual, formatar_numeros

#Calcula a relação divida/Ebitda para um ticker
def get_divida_ebitda(ticker):
    ticker = yf.Ticker(ticker) # Cria objeto Ticker
    info = ticker.info # Obtem informações da empresa
    divida = info.get('totalDebt', 0) # Pega divida total, padrao 0
    ebitda = info.get('ebitda', 0) # Pega EBITDA total, padrao 0
    
    if ebitda == 0: # Evita divisao por 0
        return "N/A"
    
    divida_ebitda = divida / ebitda # Realiza o calculo desejado
    return divida_ebitda

def coletar_dados_completos(tickers): # Coleta dados financeiros para uma lista de tickers

    dados = [] # Cria uma lista vazia para armazenas dados
    
    for tck in tickers:
        print(f"Baixando dados para {tck}...") # Mostra o progresso
        t = yf.Ticker(tck)
        info = t.info

        # Tenta obter a data do ultimo preço disponivel
        try: 
            hist = t.history(period='5d') #Baixa o historico de 5 dias
            data_atual = str(hist.index[-1].date()) # seleciona a ultima data
        except:
            data_atual = "N/A" # Define uma saida N/A em caso de falha

        # Indicadores principais
        indicadores = {
            "Ticker": tck.upper(),
            "Nome": info.get("shortName", "N/A"),
            "Setor": info.get("sector", "N/A"),
            "Segmento": info.get("industry", "N/A"),
            "Div Yield (%)": f"{info.get('dividendYield', 0):.2f}%" if info.get('dividendYield') is not None else "N/A",
            "5Y Dividendo": f"{info.get("fiveYearAvgDividendYield", 0):.2f}%" if info.get('dividendYield') is not None else "N/A",
            "52-Week Low": info.get("fiftyTwoWeekLow"),
            "Preço Atual": info.get("currentPrice"),
            "52-Week High": info.get("fiftyTwoWeekHigh"),
            "Beta": info.get("beta"),
            "P/L": info.get("trailingPE"),
            "P/L Future": info.get("forwardPE"),
            "P/VP": info.get("priceToBook"),
            "Crescimento receita": info.get("revenueGrowth", 0),
            "Crescimento lucro": info.get("earningsGrowth", 0),
            "Free Cash Flow": info.get("freeCashflow", 0),
            "EV/EBITDA": info.get("enterpriseToEbitda", 0),
            "Divida/EBITDA": get_divida_ebitda(tck),
            "ROE (%)": (info.get("returnOnEquity", 0) or 0),
            "Margem Líquida (%)": (info.get("profitMargins", 0) or 0),
            "Payout Ratio": info.get("payoutRatio", 0),
            "Ultimo Dividendo ($)": (info.get("lastDividendValue", 0)),
            "Último Pagamento(Data)": formatar_data(info.get("lastDividendDate", None)),
            "Proximo Dividendo(Data)": formatar_data(info.get("DividendDate", None)),
            "Market Cap (B)": round(info.get("marketCap", 0)),
            "Ultima Atualização": data_atual
        }

        # Dados trimestrais (income statement)
        income_statement = t.quarterly_income_stmt 
        if income_statement is not None and not income_statement.empty:
            ultimo_trimestre = income_statement.columns[0]
            receita = income_statement.loc['Total Revenue', ultimo_trimestre] if 'Total Revenue' in income_statement.index else None
            lucro = income_statement.loc['Net Income', ultimo_trimestre] if 'Net Income' in income_statement.index else None
        else:
            receita = lucro = None

        indicadores['Receita'] = receita 
        indicadores['Lucro'] = lucro
        dados.append(indicadores) # Adiciona indicadores Receita e Lucro a lista

    df = pd.DataFrame(dados) # Cria o DataFrame com todos os dados
    colunas_percentuais = [
        'Crescimento receita', 'Crescimento lucro', 
        'ROE (%)', 'Margem Líquida (%)', 'Payout Ratio'
    ]
    colunas_numeros = [
        'P/L', 'P/L Future', 'P/VP', 'Beta', 'EV/EBITDA', 'Divida/EBITDA',
    ]
    colunas_valores = [
        'Preço Atual', 'Receita', 'Lucro', 'Market Cap (B)', 'Ultimo Dividendo ($)', 
        'Free Cash Flow', '52-Week Low', '52-Week High'
    ]
    # Formata valores monetários
    for col in colunas_valores:
        df[col] = df[col].apply(formatar_valor)
    # Formata percentuais
    for col in colunas_percentuais:
        df[col] = df[col].apply(formatar_percentual)
    # Formata números
    #for col in colunas_numeros:
     #   df[col] = df[col].apply(formatar_numeros)
        
    return df