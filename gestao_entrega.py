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

nr_lcto = 96948
def gestao_entrega():
  print('Recebido da função cadastrar_venda o lançamento: ', nr_lcto)
  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/reservas_produtos")
    print('Abrir + Filtros.')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/form/div/div[2]/div[2]/div/div[17]/a').click()
    print('Localiza campo Nº Lançamento. ')
    nome_element = navegador.find_element(By.XPATH, '//*[@id="numero_lancamento"]')
    nome_element.send_keys(nr_lcto)
    print('Passei número do lançamento: ', nr_lcto)
    print('Filtrar...')
    navegador.find_element(By.XPATH, '//*[@id="pesquisar-reservas"]').click()
    sleep(3)
    print('Marcar lançamento...')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div[3]/table/tbody/tr/td[1]/label').click()
    sleep(2)
    print('Gerar romaneio...')
    navegador.find_element(By.XPATH, '//*[@id="btn_gerar_romaneio"]').click()
    sleep(2)
    print('Confirmando geração... ')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/button[2]').click()
    sleep(3)
    print('Alterar situação...')
    sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[2]/div[1]/button').click()
    sleep(2)
    print('Finalizar... ')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[2]/div[1]/ul/li[1]/a').click()
    navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
    sleep(10)
    campo_nr_romaneio = navegador.find_element(By.XPATH, '//*[@id="id"]')
    nro_romaneio = campo_nr_romaneio.get_attribute("value")
    sleep(2)
    print("Nº Romaneio: ", nro_romaneio)

  finally:
    print('Encerrando função gestao_entrega')


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

gestao_entrega()
