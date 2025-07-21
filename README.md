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

---

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
├── README.md
