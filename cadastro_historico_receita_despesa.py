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


def cadastro_historico_receita_despesa():
    try:
       data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
       desc_hist_rec_desp = 'Historico Receita/Despesa Automatizado'
       desc_hist_rec_desp_data = f"{desc_hist_rec_desp} - {data_atual}"

       navegador.get('https://felipe.testes.smart.sgisistemas.com.br/historicos_receitas_despesas')
       print("######### TELA  HISTÓRICOS DE RECEITAS E DESPESAS #########")

       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)

       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_hist_rec_desp_data)
       sleep(2)

       subgrupo = navegador.find_element(By.XPATH, '//*[@id="autocompletar_subgrupo_historico_rd_id"]')
       subgrupo.send_keys(data_atual)
       sleep(2)
       pyautogui.hotkey('down')
       pyautogui.hotkey('tab')
       sleep(5)
       bt_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[9]/div/input[1]')
       sleep(2)
       bt_salvar.click()
       sleep(5)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(3)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


       print("### INICIANDO EXCLUSÃO ###")
       
       filtro = navegador.find_element(By.XPATH, '//*[@id="descricao_ilike"]')
       filtro.send_keys(desc_hist_rec_desp_data)

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]').click()
       sleep(2)
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
       sleep(2)
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[9]/div/a[2]').click()
       sleep(2)
       navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
       sleep(2)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:25]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Excluído com Sucesso!':
         print("### Tela Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

       print("### INICIANDO SEGUNDA INCLUSÃO ###")

       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)

       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_hist_rec_desp_data)
       sleep(2)

       subgrupo = navegador.find_element(By.XPATH, '//*[@id="autocompletar_subgrupo_historico_rd_id"]')
       subgrupo.send_keys(data_atual)
       sleep(2)
       pyautogui.hotkey('down')
       pyautogui.hotkey('tab')
       sleep(3)
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[9]/div/input[1]').click()

       sleep(3)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(3)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

    finally:
        print("Encerrando execução função cadastro_historico_receita_despesa.")







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

cadastro_historico_receita_despesa()