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


def lancamento_entrada():
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entrada")
    print("Acessei tela Entrada")

    global numero_lancamento_entrada
    numero_lancamento_entrada = random.randint(1,5000000)
    sleep(2)

    numero_lancamento = navegador.find_element(By.XPATH, '//*[@id="numero_documento"]')
    sleep(2)
    numero_lancamento.send_keys(str(numero_lancamento_entrada))
    print("Numero do Documento: ", numero_lancamento_entrada)

    serie = navegador.find_element(By.XPATH, '//*[@id="serie_documento"]')
    serie.send_keys('1')
    print("Serie 1")

    fornecedor = navegador.find_element(By.XPATH, '//*[@id="autocompletar_pessoa_cliente_fornecedor_id"]')
    fornecedor.send_keys('FORNECEDOR DE TESTE')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    sleep(3)
    print("Informei Fornecedor de Teste(12551)")
    sleep(2)

    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[1]/h4').click
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[1]/h4').click
    #print("Abri/Fecha")

    nome_element = navegador.find_element(By.XPATH, '//*[@id="coluna_descricao_produto"]')
    nome_element.click()
    #print("fiz o click")
    nome_element = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produto_id_0"]')
    sleep(2)    
    nome_element.send_keys('7410')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    sleep(3)
    print("Passei Produto de Teste(7410)")
    
    qtde_nota = navegador.find_element(By.XPATH, '//*[@id="coluna_quantidade_nota"]')
    qtde_nota.send_keys('10')
    print("Informei 10 unidades do item.")
    sleep(2)
    pyautogui.hotkey('tab')
    sleep(2)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    
    sleep(2)
    pyautogui.write('10')
    pyautogui.hotkey('tab')
    print("Informei 10 unidades de lançamento.")
    
    navegador.find_element(By.XPATH, '//*[@id="concluir_quantidade_por_local"]').click()
    sleep(3)
    cst_icms = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[2]/div/div[2]/table/tbody/tr/td[11]')
    sleep(2)
    cst_icms.click()
    sleep(2)
    inf_cst = navegador.find_element(By.XPATH, '//*[@id="autocompletar_cst_icms_id_0"]')
    sleep(0.5)
    inf_cst.send_keys('41')
    print("Cliquei na coluna CST ICMS")
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    print("Informei CST 41.")

    sleep(1)

    vlr_unit = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div[1]')
    sleep(0.5)
    vlr_unit.click()
    sleep(0.5)
    pyautogui.hotkey('backspace')
    print("Apaguei valor unitário.")
    sleep(1)
    pyautogui.write('15000000')
    #vlr_unit.send_keys('15000000')
    sleep(1)
    pyautogui.hotkey('tab')
    sleep(3)
    print("Informei novo valor unitário.")
    sleep(1)

    forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[22]/div/div[2]/div/div[1]/div/div[1]/div/div/div/button/span[1]')
    forma_pgto.click()
    sleep(0.5)
    busca_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[22]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/input')
    sleep(0.5)
    busca_forma_pgto.send_keys('BOLETO')
    sleep(0.5)
    pyautogui.hotkey('Enter')
    sleep(3)
    print("Informei forma de pagamento BOLETO")

    qtde_parcelas = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
    sleep(0.5)
    qtde_parcelas.click()
    sleep(0.5)
    pyautogui.hotkey('backspace')
    sleep(0.5)
    qtde_parcelas.send_keys('3')
    print("Informei 3 parcelas")
    sleep(1)

    navegador.find_element(By.XPATH, '//*[@id="emitir_documento"]').click()
    sleep(0.5)
    navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button[2]').click()
    print("Finalizado lançamento.")
    sleep(8)

    abas = navegador.window_handles

    for indice, aba in enumerate(abas):
        navegador.switch_to.window(aba)
        print(f"Índice da janela: {indice}")
        if indice > 0:
            navegador.close()
    sleep(2)
    abas = navegador.window_handles
    if len(abas) > 0:
        navegador.switch_to.window(abas[0])
    #    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")

    sleep(0.5)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/form/div/div[2]/div[2]/table/tbody/tr/td[1]/label').click()
    sleep(0.5)
    navegador.find_element(By.XPATH, '//*[@id="tipo_custo"]').click()
    sleep(1)
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('tab')
    sleep(1)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/form/div/div[3]/button').click()
    sleep(3)
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")
    

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
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
usuario_element.send_keys('robo.robo')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

sleep(3)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(3)

lancamento_entrada()

navegador.quit()