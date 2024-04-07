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


def conta_caixa_por_usuario():
    try:
        navegador.get('https://felipe.testes.smart.sgisistemas.com.br/contas_caixas_usuarios')
        print("######### CONTA CAIXA POR USUÁRIO ##########")
        sleep(2)
        usuario = navegador.find_element(By.XPATH, '//*[@id="autocompletar_usuario_id"]')
        usuario.send_keys('robo.robo')
        print("Selecionei usuário")
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        print("Confirmei usuário")
        sleep(3)
        contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        contas_caixas.click()
        print("Abri multiselect de Contas Caixa")
        selecao_todos = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/ul/li[2]/a/label/input')
        selecao_todos.click()
        print("Marquei todas")
        contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        contas_caixas.click()
        print("Fechei multiselect")

        contas_caixas_permitidas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/button/span')
        contas_caixas_permitidas.click()
        print("Abri multiselct de Contas Caixa permitidas")
        selecao_todos_permitidos = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/ul/li[2]/a/label/input')
        selecao_todos_permitidos.click()
        print("Marquei todas das permitidas")

        contas_caixas_permitidas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/button/span')
        contas_caixas_permitidas.click()
        print("Fechei multiselect")

        btn_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/input')
        btn_salvar.click()
        print("Salvar")

        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')))
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')   
        b_text = b_element.text
        msg_confirmacao = b_text[0:30]
        print('#### Mensagem confirmação: ', msg_confirmacao)

        if msg_confirmacao == 'Salvo com sucesso.':
            print("### Conta caixa liberada com sucesso")
        else:
            print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


        print("######### SEGUNDA EXECUÇÃO ##########")
        sleep(2)
        usuario = navegador.find_element(By.XPATH, '//*[@id="autocompletar_usuario_id"]')
        usuario.send_keys('robo.robo')
        print("Selecionei usuário")
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        print("Confirmei usuário")
        sleep(3)
        contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        contas_caixas.click()
        print("Abri multiselect de Contas Caixa")
        sleep(2)
        selecao_unico = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/ul/li[4]/a/label')
        selecao_unico.click()
        sleep(2)
        contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        contas_caixas.click()
        sleep(2)

        contas_caixas_permitidas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/button/span')
        contas_caixas_permitidas.click()
        print("Abri multiselct de Contas Caixa permitidas")

        selecao_unico_permitido = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/ul/li[4]/a/label')
        selecao_unico_permitido.click()

        btn_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/input')
        btn_salvar.click()
        print("Salvar")    

        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')))
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')   
        b_text = b_element.text
        msg_confirmacao = b_text[0:30]
        print('#### Mensagem confirmação: ', msg_confirmacao)

        if msg_confirmacao == 'Salvo com sucesso.':
            print("### Conta Caixa liberada com sucesso")
        else:
            print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

        

    finally:
        print("Encerrando função liberação Conta Caixa por Usuário")




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

conta_caixa_por_usuario()

