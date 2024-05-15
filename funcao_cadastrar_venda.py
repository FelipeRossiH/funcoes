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

from selenium.common.exceptions import NoSuchElementException
def cadastrar_venda(numero_cliente, numero_produto):
    try:
        global nr_lcto
        hora_inicio = datetime.datetime.now()
        print("Tempo iniciado")
        print('########## TELA PEDIDO DE VENDA ##########')
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")

        # Preencher o campo "Cliente"
        nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
        nome_element.send_keys(numero_cliente)
        print('### Passei Cliente', numero_cliente)
        sleep(3)
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
        sleep(1)
        nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
        sleep(1)
        nome_element.send_keys('1')
        print('### Passei quantidade.')
        pyautogui.hotkey('ENTER')
        sleep(1)

        # Preencher o campo "Forma de Pagamento"
        nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
        nome_element.send_keys('V')
        sleep(1)
        pyautogui.hotkey('ENTER')
        print('### Passei forma de pagamento carnê')

        # Preencher o campo "Quantidade de Parcelas"
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
        sleep(1)
        nome_element.send_keys('0')
        sleep(1)
        print('### Passei quantidade de parcelas.')
        
        # Clicar no botão "Salvar"
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        #print("Aguarda 10 segundos para liberação")
        for segundo_atual in range(6, 0, -1):
            #print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)

        # Preencher campos de liberação
        navegador.find_element(By.ID, 'login_liberacao_venda').click()
        sleep(0.5)
        nome_element = navegador.find_element(By.ID, 'login_liberacao_venda')
        sleep(0.5)
        nome_element.send_keys('projeto.robo')
        pyautogui.hotkey('tab')
        print('### Passei usuário de liberação')

        navegador.find_element(By.ID, 'senha_liberacao_venda').click()
        nome_element = navegador.find_element(By.ID, 'senha_liberacao_venda')
        nome_element.send_keys('@rlequin@2020')
        pyautogui.hotkey('tab')
        print('### Passei senha de liberação')
        pyautogui.hotkey('ENTER')
        
        #print("Aguarda 3 segundos - 2ªvez")
        for segundo_atual in range(3, 0, -1):
            #print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)
    
        # Clicar no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button').click()
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        

        # Obter número do lançamento
        while True:
            try:
                b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
                b_text = b_element.text
                nr_lcto = b_text[14:19]
                print('#### Número do lançamento: ', nr_lcto)
                break
            except NoSuchElementException:
                #print("Aguardando elemento...")
                sleep(1)
        hora_fim = datetime.datetime.now()
        print("Tempo Finalizado")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    finally:
        hora_fim = datetime.datetime.now()
        tempo_total = (hora_fim - hora_inicio)
        print("Tempo de execução", tempo_total)  
        print("Encerrado função funcao_cadastrar_venda")
        # navegador.quit()

# def cadastrar_venda(numero_cliente, numero_produto):
#     try:
#         global nr_lcto
#         hora_inicio = datetime.datetime.now()
#         print(f"Tempo iniciado: {hora_inicio}")
#         print('########## TELA PEDIDO DE VENDA ##########')
#         #navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")

#         # Preencher o campo "Cliente"
#         print(f"{datetime.datetime.now()}: ### Preenchendo Cliente {numero_cliente}")
#         sleep(3)

#         # Preencher o campo "Produto"
#         print(f"{datetime.datetime.now()}: ### Preenchendo Produto {numero_produto}")
#         sleep(2)

#         # Preencher o campo "Quantidade"
#         print(f"{datetime.datetime.now()}: ### Preenchendo Quantidade")
#         sleep(1)

#         # Preencher o campo "Forma de Pagamento"
#         print(f"{datetime.datetime.now()}: ### Preenchendo Forma de Pagamento")
#         sleep(1)

#         # Preencher o campo "Quantidade de Parcelas"
#         print(f"{datetime.datetime.now()}: ### Preenchendo Quantidade de Parcelas")
#         sleep(2)

#         # Clicar no botão "Salvar"
#         print(f"{datetime.datetime.now()}: ### Salvando")
#         for segundo_atual in range(12, 0, -1):
#             #print(f"{datetime.datetime.now()}: Tempo restante: {segundo_atual} segundos")
#             sleep(1)

#         # Preencher campos de liberação
#         print(f"{datetime.datetime.now()}: ### Preenchendo Usuário de Liberação")
#         sleep(0.5)

#         print(f"{datetime.datetime.now()}: ### Preenchendo Senha de Liberação")
        
#         print(f"{datetime.datetime.now()}: Aguardando 3 segundos - 2ª vez")
#         for segundo_atual in range(1, 0, -1):
#             #print(f"{datetime.datetime.now()}: Tempo restante: {segundo_atual} segundos")
#             sleep(1)
    
#         # Clicar no botão "Salvar" novamente
#         print(f"{datetime.datetime.now()}: ### Salvando novamente")
#         sleep(0.3)

#         # Obter número do lançamento
#         while True:
#             try:
#                 print(f"{datetime.datetime.now()}: #### Obtendo Número do Lançamento")
#                 break
#             except NoSuchElementException:
#                 print(f"{datetime.datetime.now()}: Aguardando elemento...")
#                 sleep(1)
#         hora_fim = datetime.datetime.now()
#         print(f"Tempo Finalizado: {hora_fim}")

#     except Exception as e:
#         print(f"Ocorreu um erro: {str(e)}")

#     finally:
#         hora_fim = datetime.datetime.now()
#         tempo_total = (hora_fim - hora_inicio)
#         print(f"Tempo de execução: {tempo_total}")  
#         print("Encerrado função funcao_cadastrar_venda")
#         # navegador.quit()


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
usuario_element.send_keys('robo.robo')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)

cadastrar_venda("12546", "7410")
#faturamento_de_venda()



navegador.quit()
