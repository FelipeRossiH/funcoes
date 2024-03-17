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
nr_lcto = 0
tela = 0

navegador = Firefox()
navegador.maximize_window()
navegador.get(smart)
hora_inicio = datetime.datetime.now()
cont = 0
erro = 0
print('#######################################################################')
print('#                NÃO UTILIZE MOUSE E TECLADO                          #')
print('#######################################################################')
sleep(3)
print('### Navegador aberto.')

usuario_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'usuario')))
usuario_element.send_keys('robo.robo')
print('### Passei usuário.')


senha_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'senha')))
senha_element.send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/empresas/1/edit")
print('########## TELA CONFIGURAÇÃO DA EMPRESA ##########')
tela = tela + 1
print('Tela: ', tela)
sleep(2)


navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[1]/input[1]').click()
sleep(2)
b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
b_text = b_element.text
msg_confirmacao = b_text[1:99]
print('#### Mensagem confirmação: ', msg_confirmacao)
sleep(8)

if msg_confirmacao == 'Atualizado com Sucesso!':
    print("### Tela configuração de empresa ok.")
else:
    print(">>>>>>>>>>>>>> Erro na tela! Verificar.")












#error_message = navegador.find_elements(By.XPATH, '//*[@id="nome"]')
#if error_message:
#    print("A página foi aberta")
#    #navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[1]/input[1]').click()
#    avegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[1]/input[1]').click()
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#    result_teste = ">>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO"
#cont = cont +1
#navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[1]/input[1]').click()