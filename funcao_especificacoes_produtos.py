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

def adicionar_especificacao_produto():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/especificacoes_produtos")
        print('### Abrindo especificação do produto')
        print('### Adicionar')

        # Clique no botão para abrir o formulário de cadastro
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        ).click()

        # Preencha a descrição da especificação
        descricao_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        descricao_element.send_keys('Especificação Automática')
        print('### Passei descrição especificação.')

        print('Texto Curto (até 255 caracteres)')
        # Selecione o tipo "Texto Curto"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        print('Texto Longo (sem limite de caracteres)')
        # Selecione o tipo "Texto Longo"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        print('Número inteiro')
        # Selecione o tipo "Número inteiro"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Defina o número de casas decimais (para o tipo "Número decimal")
        if "Número decimal" in navegador.page_source:
            casas_decimais_element = navegador.find_element(By.XPATH, '//*[@id="casas_decimais"]')
            casas_decimais_element.send_keys('2')
            print('### Passei 2 casas decimais')

        # Clique no botão "Salvar"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]'))
        ).click()
        sleep(2)
        print('Lista Pré-definida')
        # Selecione o tipo "Lista Pré-definida"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Preencha as opções da lista
        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
        opcao_element.send_keys('Primeira opção')
        print('### Passei primeira opção')

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/table/tfoot/tr/td/button').click()

        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_1"]')
        opcao_element.send_keys('Segunda opção')
        print('### Passei segunda opção')

        # Clique no botão "Salvar"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]'))
        ).click()

        print('Sim/Não')
        # Selecione o tipo "Sim/Não"
        sleep(2)
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        print('Lista Pré-definida (Multiselect)')
        # Selecione o tipo "Lista Pré-definida (Multiselect)"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Preencha as opções da lista
        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
        opcao_element.send_keys('Primeira opção')
        print('### Passei primeira opção')

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/table/tfoot/tr/td/button').click()

        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_1"]')
        opcao_element.send_keys('Segunda opção')
        print('### Passei segunda opção')

        # Clique no botão "Salvar"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]'))
        ).click()
        sleep(2)
        # Clique no botão "Excluir"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[2]'))
        ).click()
        sleep(2)

        # Confirme a exclusão
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]'))
        ).click()

        print('Realizado exclusão de especificação do produto')
        print("#######################################################################")

    finally:
        # Feche o navegador
        # navegador.quit()
        print('>> Encerrando função especificacoes_produtos')



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

adicionar_especificacao_produto()

navegador.quit()
