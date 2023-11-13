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
import random

def gera_titulo():

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/titulos")
    print("########## TELA TÍTULO ##########")

    print("Adicionar novo título à receber")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

    #print("Buscar tipos de título")
    #navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div[2]/div/div/div/div/span[2]/span').click()
    sleep(2)

    tp_titulo = navegador.find_element(By.XPATH,'//*[@id="autocompletar_tipo_titulo_id"]')
    sleep(3)
    tp_titulo.send_keys('Receber')
    #pyautogui.hotkey('R','e','c','e','b','e','r')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    print("Selecionar título à receber")
    sleep(2)

    print("Preencher cliente")
    cod_cliente_fornecedor = navegador.find_element(By.XPATH, '//*[@id="autocompletar_pessoa_cliente_fornecedor_id"]')
    cod_cliente_fornecedor.send_keys('12547')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei cliente 12547")

    #gerador aleatorio para numero de titulos
    numero_titulo_gerado = random.randint(1,5000000)
    sleep(2)

    numero_titulo = navegador.find_element(By.XPATH, '//*[@id="numero_titulo"]')
    sleep(2)
    numero_titulo.send_keys(str(numero_titulo_gerado))
    print("Numero do título: ", numero_titulo_gerado)

    print("Informar título Realizado")
    navegador.find_element(By.XPATH, '//*[@id="previsto_realizado"]').click()
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')

    print("Informar forma de pagamento")
    frm_pgto = navegador.find_element(By.XPATH, '//*[@id="autocompletar_forma_pagamento_id"]')
    frm_pgto.send_keys('Vazio - Carnê Loja TIR')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei forma de pagamento Vazio - Carnê Loja TIR")
    sleep(2)

    print("Informar Portador")
    portador = navegador.find_element(By.XPATH, '//*[@id="autocompletar_portador_titulo_id"]')
    portador.send_keys('Carteira')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei portardor Carteira")
    sleep(2)

    print("Informar Histórico de Receita e Despesa")
    historico_rec_desp = navegador.find_element(By.XPATH, '//*[@id="autocompletar_historico_receita_despesa_id"]')
    historico_rec_desp.send_keys('Venda Financiada')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei Histório de Receita/Despesa Venda Financiada")
    sleep(2)

    print("Informar valor de parcelas")
    vlr_parcela = navegador.find_element(By.XPATH, '//*[@id="valor_cada_titulo"]')
    vlr_parcela.send_keys('10000')
    pyautogui.hotkey('tab')
    dt_primeiro_vcto = navegador.find_element(By.XPATH, '//*[@id="primeira_data_vencimento"]')
    dt_primeiro_vcto.send_keys('01092022')

    print("Informar quantidade de parcelas")
    qtd_parcelas = navegador.find_element(By.XPATH, '//*[@id="quantidade_parcelas"]')
    qtd_parcelas.clear()
    qtd_parcelas.send_keys('0')
    pyautogui.hotkey('tab')
    print("Passei 10 parcelas")

    print("Infomar observação do título")
    obs_titulo = navegador.find_element(By.XPATH, '//*[@id="observacao_geral"]')
    obs_titulo.send_keys('Inserção automática do título: ', numero_titulo_gerado)
    print("Inserido observação")


    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[1]').click()
    print("Salvo título ", numero_titulo_gerado)
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")


  finally:
    print("Encerrando função gera_titulo.")







































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

gera_titulo()
