import random

# Números excluídos
numeros_excluidos = [7, 8, 9, 13, 19, 21, 26, 28, 39, 44, 48, 54, 60]

# Números permitidos (considerando a probabilidade da Mega-Sena)
numeros_permitidos = list(range(1, 61))

# Remover os números excluídos da lista de permitidos
numeros_permitidos = list(set(numeros_permitidos) - set(numeros_excluidos))

# Gerar 8 números aleatórios, considerando as restrições
numeros_aleatorios = random.sample(numeros_permitidos, 8)

# Exibir os números gerados
print("Números da Mega-Sena:")
for numero in sorted(numeros_aleatorios):
    print(numero)
