from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
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


def abrir_pagina_e_verificar(url, nome_elemento):
    cont = 0
    erro = 0
    navegador.get(url)
    print('### Abrindo cadastro de pessoas')

    error_message = navegador.find_elements(By.NAME, nome_elemento)

    if error_message:
        print("A página foi aberta")
    else:
        erro = erro + 1
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
        result_teste = ">>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO"

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
navegador = Firefox()
navegador.maximize_window()
navegador.get(smart)
#hora_inicio = datetime.datetime.now()
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

# Exemplo de uso da função
#navegador = webdriver.Firefox()  # Inicialize o navegador (Lembre-se de instalar o Selenium e o ChromeDriver)
url = "https://felipe.testes.smart.sgisistemas.com.br/pessoas"
nome_elemento = "filtros[nome]"
abrir_pagina_e_verificar(url, nome_elemento)
