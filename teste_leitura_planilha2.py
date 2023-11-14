#teste2 leitura de planilhas

import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo Excel
planilha = pd.read_excel(r'C:\Users\felip\Downloads\CopiadeAcompanhamento-Testes.xlsx')

# Leitura de várias colunas
colunas = ['ColunaC', 'ColunaE', 'ColunaF']
dados = planilha[colunas]

# Leitura de várias linhas
linhas = planilha.loc[2216:2230]  # Lê as 10 primeiras linhas (0 a 9)

# Criação do gráfico de linhas
plt.plot(linhas[colunas])
plt.xlabel('Índice da Linha')
plt.ylabel('Valores')
plt.title('Gráfico de Linhas')
plt.legend(colunas)
plt.show()

# Criação do gráfico de barras
linhas.T.plot(kind='bar')
plt.xlabel('Colunas')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')
plt.legend(linhas.index)
plt.show()

# Criação do gráfico de dispersão
for coluna in colunas:
    plt.scatter(linhas.index, linhas[coluna], label=coluna)

plt.xlabel('Índice da Linha')
plt.ylabel('Valores')
plt.title('Gráfico de Dispersão')
plt.legend()
plt.show()
