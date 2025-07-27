# 📊 Análise de Investimentos com Python

Este projeto realiza a **coleta, organização e armazenamento** de dados financeiros de ações da bolsa americana, com foco em análise fundamentalista. Ele utiliza a biblioteca `yfinance` para extrair dados como dividendos, lucro, receita, indicadores de valuation e muito mais.

---

## 🧰 Tecnologias e Bibliotecas

- Python 3.13.3
- [yfinance]
- pandas
- SQLite (via `sqlite3`)
- openpyxl (para exportação `.xlsx`)

---

## 📦 Funcionalidades
✅ Coleta de dados para uma lista personalizada de ações  
✅ Indicadores financeiros: P/L, ROE, Beta, Margem líquida, etc.  
✅ Dividendos: último valor, data do pagamento, yield e média 5Y  
✅ Crescimento de receita e lucro  
✅ Métricas como EV/EBITDA, Dívida/EBITDA, FCF  
✅ Exportação para banco de dados SQLite  
✅ Exportação para planilha Excel (.xlsx)  
✅ Visualização gráfica de indicadores financeiros importantes (via matplotlib)  

---
📊 Visualização de Dados - gráficos.py
- O arquivo gráficos.py oferece a geração de gráficos que facilitam a análise visual dos dados coletados:
- Gráfico de barras horizontal: Top 10 empresas por Market Cap, mostrando capitalização de mercado em bilhões de dólares.
- Gráfico de barras vertical: Dividend Yield (%) das 10 maiores empresas por Market Cap.
- Gráfico de dispersão: Relação entre P/L (Preço/Lucro) e Crescimento do Lucro, destacando os tickers no gráfico para facilitar identificação.

## 📁 Estrutura
```text

analise_investimentos/
│
├── data/
│ └── investimentos.db # Banco de dados SQLite
│ └── investimentos.xlsx # Exportação para Excel
│
├── coleta.py # Script principal de coleta
├── formatacao.py # Funções auxiliares para formatar valores
├── main.py # Script principal de execução
├── graficos.py
├── README.md
