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

def login():
    try:
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

    finally:
      print('>> Login OK.')
      print('>> Encerrando funcao_login')

login()
