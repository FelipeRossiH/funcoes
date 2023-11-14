#teste de leitura de planilhas


import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo Excel
planilha = pd.read_excel(r'C:\Users\felip\Downloads\CopiadeAcompanhamento-Testes.xlsx')

# Exemplo de leitura de uma coluna específica
coluna_x = planilha['ColunaF']
coluna_y = planilha['ColunaG']

# Criação do gráfico de linha
plt.plot(coluna_x, coluna_y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Linha')
plt.show()

# Criação do gráfico de dispersão
plt.scatter(coluna_x, coluna_y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')
plt.show()

# Criação do gráfico de barras
plt.bar(coluna_x, coluna_y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Barras')
plt.show()
