import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from formatacao import formatar_bilhoes

# Carregar os dados
df = pd.read_excel("data/investimentos.xlsx")

def get_top10():

    df['Market Cap (B)'] = df['Market Cap (B)'].replace('[$,]', '', regex=True).astype(float)     # Limpar e converter a coluna 'Market Cap (B)'
    df['Div Yield (%)'] = df['Div Yield (%)'].replace('%', '', regex=True).astype(float)
    df['Crescimento lucro'] = df['Crescimento lucro'].replace('%', "", regex=True).astype(float)

    top10 = df.sort_values(by='Market Cap (B)', ascending=False).head(10)     # Selecionar as 10 maiores empresas por Market Cap

    return top10

def bars_market_cap(ax=None): # Gráfico de barras Horizontal

    top10 = get_top10()
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')
        show_plot = True
    else:
        show_plot = False
    bars = ax.barh(top10['Ticker'], top10['Market Cap (B)'], color='#2ecc71')  # Cor verde e bordas pretas

    # Configurar os eixos
    ax.set_xlabel('Market Cap (Billion $)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Top 10 Empresas por Market Cap', fontsize=12, fontweight='bold')
    ax.set_title('Maiores Empresas por Capitalização de Mercado', fontsize=14, fontweight='bold', pad=15)

    # Inverter o eixo y para que a maior empresa fique no topo
    ax.invert_yaxis()

    # Formatar o eixo x para evitar notação científica e mostrar bilhões
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(formatar_bilhoes))  # Chama a função que formata a saida em Bilhoes

    ax.grid(True, axis='x', linestyle='--', alpha=0.7)    # Adicionar grade para melhor legibilidade


    # Ajustar o estilo da grade e fundo
    ax.set_facecolor('#f5f5f5')  # Fundo cinza claro
    ax.spines['top'].set_visible(False)  # Remover borda superior
    ax.spines['right'].set_visible(False)  # Remover borda direita

    # Adicionar rótulos de dados nas barras
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.02*width, bar.get_y() + bar.get_height()/2, f'{width/1e9:,.0f} B',
                 ha='left', va='center', fontsize=10, color='black')

    if show_plot:
        plt.tight_layout()  # Ajustar o layout para evitar sobreposição
        plt.show()    # Exibir o gráfico

def vertical_dy_market_cap(ax=None): # Gráfico de barras Vertical
    top10 = get_top10()
    
    top10 = top10.sort_values(by='Div Yield (%)', ascending=True).reset_index(drop=True)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')
        show_plot = True
    else:
        show_plot = False    
    
    bar = ax.bar(top10['Ticker'], top10['Div Yield (%)'], color = 'green')
    
    ax.set_xlabel('Empresas', fontsize = 12, fontweight = 'bold')
    ax.set_ylabel('Dividend Yield (%)', fontsize = 12, fontweight = 'bold')
    ax.set_title('Dividendos das 10 maiores empresas por Market Cap', fontsize= 14, fontweight = 'bold', pad= 10)
    
    ax.invert_xaxis()
    ax.grid(True,axis='y', linestyle='--', alpha=0.5)
    ax.set_facecolor("white")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for bar in bar:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.2, f'{height:.1f}%',
        ha='center', va='top', fontsize=8, color='black')
     
    if show_plot:
        plt.tight_layout()
        plt.show()
      
def dispersao_pl_cgar(ax=None): # Gráfico de dispersao P/L vs. Crescimento Lucro
    top10 = get_top10()
    
    top10 = top10.sort_values(by='Crescimento lucro', ascending=True).reset_index(drop=True)
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')
        show_plot = True
    else:
        show_plot = False 
    
    ax.scatter(top10['P/L'], top10['Crescimento lucro'], color = 'green', edgecolors='black', s=100)
    
    for i in range(len(top10)):
        ax.text(top10['P/L'].iloc[i], top10['Crescimento lucro'].iloc[i], top10['Ticker'].iloc[i],
                 fontsize=10, ha='right', va='bottom')
        
    ax.set_xlabel('P/L', fontsize=12, fontweight='bold')
    ax.set_ylabel('Crescimento Lucro', fontsize=12, fontweight='bold')
    ax.set_title('P/L vs Crescimento Lucro', fontsize=12, fontweight='bold', pad=10)
    
    ax.grid(True,linestyle='--', alpha=0.6)
    if show_plot:
        plt.tight_layout()
        plt.show()
        
def plot_graficos():
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18,8), facecolor='white')
    bars_market_cap(axes[0])
    vertical_dy_market_cap(axes[1])
    dispersao_pl_cgar(axes[2])
    
    plt.tight_layout()
    plt.show()

plot_graficos()