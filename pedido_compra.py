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

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_compras")
print('########## TELA PEDIDO DE COMPRA ##########')
tela = tela + 1
print('Tela: ', tela)
sleep(2)
print("Acessei tela de Pedido de Compra")

navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()
sleep(3)
print("Cliquei adicionar.")

navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div[4]/div/div/select').click()
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print("Informei Tipo de Pedido de Compra.")

fornecedor = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div[5]/div/div/div/div/span[1]/input[2]')
fornecedor.send_keys('FORNECEDOR DE TESTE')
sleep(3)
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print("Informei Fornecedor de Teste(12551).")
sleep(2)

navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/button').click()
sleep(2)

produto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/span[1]/input[2]')
produto.send_keys('7410')
sleep(3)
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
sleep(5)
print("Informei Produto de Teste(7410).")
qtde_produto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div[2]/div/div[3]/div/div/input')
qtde_produto.send_keys('100')
pyautogui.hotkey('tab')
print("Informei a quantidade de 100 itens.")
pyautogui.write('10000')
print("Informei valor unitário.")
navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div[3]/div/button[1]/span[2]').click()
sleep(2)

navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/div[2]/div[1]/div/div[1]/div/div/select').click()
cont = 0
for i in range (1,22):
    pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print("Passei forma de pagamento BOLETO.")
forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/div[2]/div[1]/div/div[3]/div[1]/div/div/input')
forma_pgto.click()
pyautogui.hotkey('backspace')
pyautogui.hotkey('3')
pyautogui.hotkey('tab')
print("Informa a quantidade de parcelas(3).")

observacao_pedido = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[9]/div/div[2]/div[3]/div/div/textarea')
observacao_pedido.send_keys("Observação com automação")
print("Informei observação de teste.")
sleep(2)
navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
sleep(5)


b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
b_text = b_element.text
msg_confirmacao = b_text[0:99]
print('#### Mensagem confirmação: ', msg_confirmacao)
sleep(8)

if msg_confirmacao == 'Adicionado com Sucesso!':
    print("### Pedido gravado com sucesso.")
else:
    print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


