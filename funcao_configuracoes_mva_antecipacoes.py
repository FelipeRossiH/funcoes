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

def configuracoes_mva_antecipacoes():
    try:
        print('#######################################################################')
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_mva_antecipacoes")
        print('### Configuração MVA Antecipação (%)')

        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

        # Clique no botão para abrir a lista de produtos
        produtos_button = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/button')
        produtos_button.click()

        # Espera até que a lista de produtos seja clicável
        produtos_list = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/ul'))
        )

        # Clique nas opções desejadas na lista de produtos
        for i in range(3, 6):
            option_xpath = f'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/ul/li[{i}]/a/label/input'
            navegador.find_element(By.XPATH, option_xpath).click()

        # Clique novamente no botão para fechar a lista de produtos
        produtos_button.click()

        # Encontre o campo "autocompletar_produtos" e preencha-o
        nome_element = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produtos"]')
        nome_element.send_keys('7410')
        sleep(2)
        print('### Passei produto.')

        # Use pyautogui para pressionar teclas
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')

        # Encontre o campo "percentual_mva_antecipacao" e preencha-o
        nome_element = navegador.find_element(By.XPATH, '//*[@id="percentual_mva_antecipacao"]')
        nome_element.send_keys('100')
        print('### Passei % de MVA Antecipação.')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/input[2]').click()

        # Encontre o campo "percentual_mva_antecipacao" novamente e preencha-o com outro valor
        nome_element = navegador.find_element(By.XPATH, '//*[@id="percentual_mva_antecipacao"]')
        nome_element.send_keys('0')
        print('### Passei % de MVA Antecipação alterado.')
        sleep(1)
        # Clique no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/input[1]').click()
        sleep(1)
        # Clique no link para excluir o cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
        sleep(1)
        # Clique no botão "Excluir"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/a[2]').click()

        # Confirme a exclusão
        navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
        print('### Excluído cadastro')

    finally:
        # Feche o navegador
        #navegador.quit()
        print('>> Encerrando funcao_configuracoes_mva_antecipacoes.')


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


configuracoes_mva_antecipacoes()

navegador.quit()
