import pyautogui
import sys
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
import random

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0


def pdv_oline():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pdv_online")
        print('### Acesso PDV Online')

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button/span[3]').click()
        sleep(0.5)
        for i in range(10):
            sleep(0.5)
            pyautogui.write('7410')
            pyautogui.hotkey('Enter')
            print("Incluso ", i, "vezes.")
        sleep(0.5)
        
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div[1]/div[1]/div[1]/div[4]/button').click()
        sleep(1)
        
        navegador.find_element(By.XPATH, '//*[@id="vendedor_id"]').click()

        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('space')
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(2)
        finalizar = navegador.find_element(By.XPATH, '//*[@id="btn_finaliza"]')
        sleep(2)
        finalizar.click()
        sleep(20)


        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div')
        b_text = b_element.text
        nr_lcto = b_text[0:99]
        print('#### Número do lançamento: ', nr_lcto)

    finally:
        print('>> Encerrando função PDV Online.')
        # Feche o navegador
        #navegador.quit()






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
usuario_element.send_keys('robo.robo')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

sleep(3)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(3)


pdv_oline()
#navegador.quit()
