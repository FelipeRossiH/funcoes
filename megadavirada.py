import random
from selenium import webdriver

# Configurar o WebDriver do Selenium (certifique-se de ter o WebDriver instalado)
# Substitua 'caminho_do_seu_webdriver' pelo caminho real do seu WebDriver
webdriver_path = 'Firefox'
driver = webdriver.Firefox(executable_path=webdriver_path)

# Números permitidos
numeros_permitidos = [10, 5, 3, 20, 33, 34, 36, 58]

# Números excluídos
numeros_excluidos = [7, 8, 9, 13, 19, 21, 26, 28, 39, 44, 48, 54, 60]

# Gerar 8 números aleatórios, considerando as restrições
numeros_aleatorios = random.sample(set(numeros_permitidos) - set(numeros_excluidos), 8)

# Exibir os números gerados
print("Números da Mega-Sena:")
for numero in sorted(numeros_aleatorios):
    print(numero)

# Fechar o navegador
driver.quit()
