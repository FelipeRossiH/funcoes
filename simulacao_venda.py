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


# def simulacao_venda():
#     try:
#         print("######### TELA SIMULAÇÃO DE VENDAS #########")
#         navegador.get('https://felipe.testes.smart.sgisistemas.com.br/simulacoes_vendas')
#         produto = navegador.find_element(By.XPATH, '//*[@id="coluna_descricao_produto"]')
#         produto.click()
#        #WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="coluna_descricao_produto"]')))
        
#         #auto_completar_produto = navegador.find_element('//*[@id="autocompletar_produto_id_0"]')
#         from selenium.common.exceptions import NoSuchElementException
#         try:
#             auto_completar_produto = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produto_id_0"]')
#         except NoSuchElementException:
#             print("O elemento não foi encontrado.")
#         auto_completar_produto.send_keys('7410')
#         sleep(2)
#         pyautogui.hotkey('down')
#         pyautogui.hotkey('tab')
#         sleep(2)


        
#         forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/button/span[1]')
#         forma_pgto.click()
        
#         opcao_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/input')
#         opcao_forma_pgto.send_keys('Vazio - Carnê Loja TIR')
#         opcao_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/ul/li[30]/a/span[1]')
#         navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/ul/li[30]/a/span[1]').click()
#         pyautogui.hotkey('down')
#         pyautogui.hotkey('tab')
#         sleep(6)


#         try:
#             parcelas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/ul/li[30]/a/span[1]')    
#             print('Achei parcelas')
#             # Rolar a página até o elemento ficar visível
#             navegador.execute_script("arguments[0].scrollIntoView(true);", parcelas)
#             # Clicar no elemento para ativá-lo
#             parcelas.click()
#             parcelas.clear()  # Limpar o conteúdo atual do campo, se houver
#             parcelas.send_keys('6')  # Enviar as chaves para o campo de entrada
#         except NoSuchElementException:
#             print("O elemento não foi encontrado.")

#         finally:
#             print("Encerrando tela simulaççao de venda.")
def simulacao_venda():
    try:
        print("######### TELA SIMULAÇÃO DE VENDAS #########")
        navegador.get('https://felipe.testes.smart.sgisistemas.com.br/simulacoes_vendas')
        produto = navegador.find_element(By.XPATH, '//*[@id="coluna_descricao_produto"]')
        produto.click()

        # Procurar pelo elemento de auto completar produto
        from selenium.common.exceptions import NoSuchElementException
        try:
            auto_completar_produto = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produto_id_0"]')
        except NoSuchElementException:
            print("O elemento não foi encontrado.")
        
        # Enviar chaves para o campo de auto completar produto
        auto_completar_produto.send_keys('7410')
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(2)

        # Clicar no botão de forma de pagamento
        forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/button/span[1]')
        forma_pgto.click()
        
        # Enviar chaves para o campo de opção de forma de pagamento
        opcao_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/input')
        opcao_forma_pgto.send_keys('Vazio - Carnê Loja TIR')
        
        # Clicar na opção de forma de pagamento
        opcao_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/ul/li[30]/a/span[1]')
        opcao_forma_pgto.click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(6)

        parcelas = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
        parcelas.send_keys('0')
        pyautogui.hotkey('tab')
        sleep(6)

        btn_gerar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[10]/input')
        btn_gerar.click()
        sleep(6)
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        msg_confirmacao = b_text[41:48]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'sucesso':
            print("### Pedido gravado com sucesso.")
        else:
            print(">>>>>>>>>>>>>> Erro na tela! Verificar.")



    finally:
        print("Encerrando tela simulação de venda.")









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

simulacao_venda()