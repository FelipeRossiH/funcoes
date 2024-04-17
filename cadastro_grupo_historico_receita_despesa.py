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


def cadastro_grupo_receita_despesa():
   
    try:
       data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
       desc_grupo_hist_rec_desp = 'Grupo Historico Receita/Despesa Automatizado'
       desc_grupo_hist_rec_desp_data = f"{desc_grupo_hist_rec_desp} - {data_atual}"
       
       navegador.get('https://felipe.testes.smart.sgisistemas.com.br/grupos_historicos_rd')
       print("######### TELA GRUPOS DE HISTÓRICOS DE RECEITAS E DESPESAS #########")

       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)
       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_grupo_hist_rec_desp_data)
       sleep(0.5)
       navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
       sleep(3)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Grupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

       print('### INICIANDO EXCLUSÃO ###')

       filtro = navegador.find_element(By.XPATH, '//*[@id="descricao_ilike"]')
       filtro.send_keys(desc_grupo_hist_rec_desp_data)

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]/span').click()
       sleep(2)
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr/td/a').click()
       sleep(2)
       btn_exclusao = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/a[2]')
       btn_exclusao.click()
       sleep(2)
       btn_confirma = navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]')
       btn_confirma.click()

       sleep(3)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:25]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Excluído com Sucesso!':
         print("### Tela cadastro Grupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


       print('### INICIANDO SEGUNDA INCLUSÃO ###')


       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)
       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_grupo_hist_rec_desp_data)
       sleep(0.5)
       navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
       sleep(3)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Grupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")




    finally:
       print("Encerrado função cadastro_grupo_receita_despesa.")






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
usuario_element.send_keys('robo.casa')
print('### Passei usuário.')
senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')
sleep(3)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(3)


cadastro_grupo_receita_despesa()