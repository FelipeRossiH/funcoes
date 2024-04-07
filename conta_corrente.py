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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.common.exceptions import TimeoutException

def conta_corrente():

    try:
        navegador.get('https://felipe.testes.smart.sgisistemas.com.br/contas_correntes')
        print("######### CONTA CAIXA POR USUÁRIO ##########")
        

        btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
        btn_adicionar.click()

        banco = WebDriverWait(navegador,10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="autocompletar_banco"]'))
        )
        banco.send_keys('Banco do Brasil S/A')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        agencia = navegador.find_element(By.XPATH, '//*[@id="autocompletar_agencia_id"]')
        agencia.send_keys('3004')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        global numero_conta_cadastro
        numero_conta_cadastro = random.randint(1,5000000)
        sleep(2)
        numero_conta = navegador.find_element(By.XPATH, '//*[@id="numero_conta"]')
        numero_conta.send_keys(numero_conta_cadastro)

        digito_conta = navegador.find_element(By.XPATH, '//*[@id="digito_conta"]')
        digito_conta.send_keys('0')

        compe = navegador.find_element(By.XPATH, '//*[@id="compe"]')
        compe.send_keys('001')

        btn_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]')
        btn_salvar.click()

    finally:
        print("Encerrando cadastro de conta corrente")








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
usuario_element.send_keys('robo.robo')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

sleep(3)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(3)


conta_corrente()