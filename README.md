# 📊 Análise de Investimentos com Python

Este projeto realiza a **coleta, organização e armazenamento** de dados financeiros de ações da bolsa americana, com foco em análise fundamentalista. Ele utiliza a biblioteca `yfinance` para extrair dados como dividendos, lucro, receita, indicadores de valuation e muito mais.

---

🧰 Tecnologias e Bibliotecas

- Python 3.13.3
- [yfinance] – Coleta de dados financeiros
- pandas – Manipulação de dados
- SQLite (via sqlite3) – Banco de dados local
- openpyxl – Exportação de planilhas Excel (.xlsx)
- matplotlib – Gráficos de amostra
- Plotly – Visualização gráfica interativa
- Streamlit – Interface web interativa

---

## 📦 Funcionalidades
✅ Coleta de dados para uma lista personalizada de ações (config.py)
✅ Indicadores financeiros: P/L, ROE, Beta, Margem líquida, EV/EBITDA, Dívida/EBITDA, FCF, entre outros
✅ Dividendos: último valor, data do pagamento, dividend yield e média 5 anos
✅ Crescimento de receita e lucro
✅ Exportação para banco de dados SQLite (stocks e carteira)
✅ Exportação para planilha Excel (.xlsx)
✅ Interface interativa via Streamlit com filtros por Setor, Segmento e Ticker
✅ Visualização gráfica interativa (Plotly):
✅ Gráficos de barras verticais e horizontais (Top 10 indicadores)
✅ Gráficos de dispersão (scatter) entre indicadores selecionados
✅ Gestão de movimentações da carteira (compra, venda, dividendos, JSCP, rendimento tributável)
✅ Edição e exclusão de operações da carteira
✅ Cálculo automático de retenção de impostos para Brasil e USA 

---
📊 Visualização de Dados
**Gráficos Estáticos (amostra_graficos.py)**

- Utiliza matplotlib para gerar gráficos locais de amostra.
- Dados utilizados: data/investimentos.xlsx
- Tipos de gráficos disponíveis:
- Barras Horizontal: Top 10 empresas por Market Cap (em bilhões de dólares)
- Barras Vertical: Dividend Yield (%) das 10 maiores empresas por Market Cap
- Dispersão: Relação entre P/L e Crescimento do Lucro, com tickers destacados
- Ideal para exportação de imagens ou análise rápida local.

**Gráficos Interativos (graficos_page.py / Streamlit)**

- Utiliza Plotly para criar gráficos interativos via interface Streamlit.
- Funcionalidades:
- Filtro por Setor e Segmento
- Seleção de indicadores e tickers específicos
- Top 10 empresas por indicador escolhido
- Visualização interativa de barras (vertical e horizontal) e scatter plot
- Permite explorar os dados dinamicamente: hover, zoom, seleção de indicadores e atualização instantânea dos gráficos.

## 📁 Estrutura
```text

analise_investimentos/
│
├── config/
│   └── config.py           # Lista de tickers configurada
│
├── data/
│   ├── investimentos.db    # Banco SQLite
│   └── investimentos.xlsx  # Exportação Excel
│
├── database/
│   ├── db.py               # Conexão e manipulação SQLite
│   ├── inputs.py           # Inserção, edição e exclusão de movimentações
│   ├── query.py            # Consultas SQL
│   └── table.py            #
├── pages/
│   ├── main_page.py        # Menu e controle dos painéis
│   ├── dashboard_page.py   # Dashboard (em desenvolvimento)
│   ├── movimentacoes_page.py # Controle de movimentações
│   ├── atualizar_page.py   # Atualização de dados via yFinance
│   ├── download_page.py    # Download da carteira em Excel
│   ├── tabelas_page.py     # Filtragem e visualização de tabelas
│   └── graficos_page.py    # Visualização de gráficos interativos
│
├── services/
│   ├── coleta.py           # Coleta de dados via yFinance
│   └── exportar.py         # Exportação de dados para Excel
│
├── utils/
│   ├── amostra_graficos.py # Gráficos de amostra (matplotlib)
│   └── formatacao.py       # Funções auxiliares de formatação
│
├── main.py                 # Script principal para execução do Streamlit
└── README.md

