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



def abrir_cadastro_pessoas(navegador):
    smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
    erro = 0
    cont = 0
    try:
     navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pessoas")
     print('### Abrindo cadastro de pessoas')
     error_message = navegador.find_elements(By.NAME, "filtros[nome]")
     if error_message:
         print("A página foi aberta")
     else:
         erro = erro + 1
         print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
         result_teste = ">>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO"
     cont = cont + 1

    finally:
        print('>> Encerrando função abrir_cadastro_pessoas.')
        
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

navegador = Firefox()
abrir_cadastro_pessoas(navegador)


navegador.quit()
