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


def funcao_gera_sped_fiscal():

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped")
    tme = 30
    print("Abrindo gerador Sped Fiscal")
    #elemento = WebDriverWait(navegador, tme).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="data_inicial"]')))
    nome_element = navegador.find_element(By.ID, 'data_inicial')
    nome_element.clear()
    nome_element.send_keys('01102023')
    print("Passei data inicial")
    sleep(2)
    nome_element = navegador.find_element(By.ID, 'data_final')
    nome_element.clear()
    nome_element.send_keys('31102023')
    print("Passei data final")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div/div[5]/span/div/div[1]/table/tbody/tr[1]/td[2]')
    actions = ActionChains(navegador)
    actions.double_click(nome_element).perform()
    print("Passei filial 1")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '//*[@id="btn-gerar-sped"]').click()
  finally:
    sleep(20)
    print("Encerrando funcao_gera_sped_fiscal")


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

funcao_gera_sped_fiscal()
