import pyautogui, sys
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
from datetime import datetime
import clipboard
import datetime
import os

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0

navegador = Firefox()
navegador.maximize_window()
navegador.get(smart)
hora_inicio = datetime.datetime.now()
print('#######################################################################')
print('#                NÃO UTILIZE MOUSE E TECLADO                          #')
print('#######################################################################')
sleep(3)
print('### Navegador aberto.')

usuario_element = navegador.find_element(By.NAME, 'usuario')
usuario_element.send_keys('robo.casa')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

sleep(3)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(3)

def cadastro_e_alteracao_de_escolaridade():

    try:
        print("Cadastro e alteração de escolaridade")
        sleep(3)  # Espera até 3 segundos por elementos

        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escolaridades")
        print('### Abrindo cadastro de escolaridade')

        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

        # Preenche o campo "descricao" com o valor "Escolaridade Automática"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Escolaridade Automática')
        print('### Preenchido campo "descricao" com "Escolaridade Automática"')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
        sleep(3)

        # Preenche o campo "descricao" com o valor "Escolaridade Automática Alterada"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Escolaridade Automática Alterada')
        print('### Preenchido campo "descricao" com "Escolaridade Automática Alterada')
        sleep(3)

        # Clique no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[1]').click()
        sleep(3)

        # Obtenha o código da escolaridade
        codigo_escolaridade = navegador.find_element(By.CLASS_NAME, "campo_id")
        print('### Código da escolaridade:', codigo_escolaridade.text)

    finally:
        print('>> Encerrando função cadastro_e_alteracao_de_escolaridade.')
        # Feche o navegador
        #navegador.quit()

cadastro_e_alteracao_de_escolaridade()
navegador.quit()
