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


def faturamento_de_venda():
  nr_lcto = 96968
  print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)

  try:
      navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recebimentos")
      print("Localizar campo Nº Lançamento")
      nome_element = navegador.find_element(By.XPATH,'//*[@id="numeros_lancamentos"]')
      sleep(2)
      nome_element.send_keys(nr_lcto)
      pyautogui.hotkey('tab')
      sleep(2)
      nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr/td[1]/label').click()
      sleep(3)
      nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/button').click()
      print('Finalizado Lançamento')
      sleep(8)
#all_handles = navegador.window_handles
#      aba_para_fechar = all_handles[1]
#      navegador.switch_to.window(aba_para_fechar)
      #navegador.close()
      navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")

  finally:
      print("Encerrado função funcao_fatura_lcto")

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

faturamento_de_venda()
