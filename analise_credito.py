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


def analise_credito():
  nr_lcto = 93986
  print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/analises_creditos")
    print("Localizar campo Nº Lançamento")
    nome_element = navegador.find_element(By.XPATH, '//*[@id="documentos.numero_lancamento"]')
    nome_element.send_keys(nr_lcto)
    print("Pesquisar lançamento para análise")
    sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[17]/div/button[1]').click()
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="btn_analise_credito"]').click()
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button[2]').click()
    sleep(2)
    print("Aba Financeiro")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[2]/a/strong').click()
    sleep(2)
    print("Aba Vendas")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[3]/a/strong').click()
    sleep(2)
    print("Aba Solicitações")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[4]/a/strong').click()
    sleep(2)
    print("Aba Observações")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[5]/a/strong').click()
    sleep(2)
    print("Histórico de observações")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[5]/div[1]/div/div/div[1]/h4/a/strong').click()
    sleep(2)
    print("Aba Comprometimento Futuro")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[6]/a/strong').click()
    sleep(2)
    print("Aba Cobranças")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[7]/a/strong').click()
    sleep(2)
    print("Aba Histórico SPC")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[8]/a/strong').click()
    sleep(2)
    print("Aba Avalista")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[8]/a/strong').click()
    sleep(2)
    print("Aba Devoluções")
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/ul/li[10]/a/strong').click()
    print("Finalizando Análise de Credito Autorizada")
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="btn_analise_credito"]').click()
    sleep(2)
    navegador.find_element(By.ID, 'btn_finalizar_analise').click()
  finally:
    print("Encerrando função analise_credito")


smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0

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

analise_credito()

#navegador.quit()
