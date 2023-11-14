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
import random
numero_titulo_gerado = 99783
def funcao_gera_cobranca():
    print("Recebido da funcao_gera_titulo: ", numero_titulo_gerado)
    try:
        print("########## CONTROLE DE COBRANÇAS #########")
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cobrancas")
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a[1]').click()
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="data_vencimento_inicial"]')
        nome_element.clear()
        nome_element.send_keys('01092022')
        print("Passei data inicial")
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="data_vencimento_final"]')
        nome_element.clear()
        nome_element.send_keys('31122500')
        print("Passei data final")
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="numero_titulo"]')
        nome_element.send_keys(numero_titulo_gerado)
        navegador.find_element(By.XPATH, '//*[@id="pesquisa_titulos_cobrancas"]').click()
        sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div[4]/div[2]/div[2]/table/thead/tr/th[1]/label').click()
        sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="gerar_cobrancas"]').click()
        sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="botao_gerar_modal"]').click()


    finally:
      print("Encerrando funcao_gera_cobranca")
















smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
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
