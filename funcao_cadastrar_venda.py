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

nr_lcto = 0
def cadastrar_venda(numero_cliente, numero_produto):


    try:
        global nr_lcto
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")
        print('### Acessei Tela de Vendas')

        # Preencher o campo "Cliente"
        nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
        nome_element.send_keys(numero_cliente)
        print('### Passei Cliente', numero_cliente)
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Preencher o campo "Produto"
        nome_element = navegador.find_element(By.ID, 'coluna_descricao_produto')
        sleep(2)
        nome_element.send_keys(numero_produto)
        print('### Passei produto.')
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('ENTER')

        # Preencher o campo "Quantidade"
        sleep(3)
        nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
        sleep(2)
        nome_element.send_keys('1')
        print('### Passei quantidade.')
        pyautogui.hotkey('ENTER')
        sleep(3)

        # Preencher o campo "Forma de Pagamento"
        nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
        nome_element.send_keys('V')
        sleep(3)
        pyautogui.hotkey('ENTER')
        print('### Passei forma de pagamento carnê')

        # Preencher o campo "Quantidade de Parcelas"
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
        sleep(2)
        nome_element.send_keys('0')
        sleep(2)
        print('### Passei quantidade de parcelas.')

        # Clicar no botão "Salvar"
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        sleep(20)

    #    Preencher campos de liberação
        navegador.find_element(By.ID, 'login_liberacao_venda').click()
        nome_element = navegador.find_element(By.ID, 'login_liberacao_venda')
        nome_element.send_keys('projeto.casa')
        pyautogui.hotkey('tab')
        print('### Passei usuário de liberação')

        navegador.find_element(By.ID, 'senha_liberacao_venda').click()
        nome_element = navegador.find_element(By.ID, 'senha_liberacao_venda')
        nome_element.send_keys('@rlequin@2020')
        pyautogui.hotkey('tab')
        print('### Passei senha de liberação')
        pyautogui.hotkey('ENTER')
        sleep(10)

        # Clicar no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button').click()
        sleep(10)
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        sleep(10)

        # Obter número do lançamento
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        nr_lcto = b_text[14:19]
        print('#### Número do lançamento: ', nr_lcto)
        sleep(2)
        return nr_lcto

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    finally:
        print("Encerrado função funcao_cadastrar_venda")
        #navegador.quit()

def faturamento_de_venda():
  print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)


  #smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
  cont = 0
  erro = 0


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

cadastrar_venda("12546", "7410")
faturamento_de_venda()

navegador.quit()
