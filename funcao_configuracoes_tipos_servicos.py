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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0

def configuracao_tipo_servico():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_servicos")
        print('### Abrindo Configuração por Tipo de Serviço')

        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()
        print('### Selecionando Tipo de Serviço')

        # Espera até que o campo de seleção de tipo de serviço esteja clicável
        tipo_servico_element = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo_servico"]'))
        )
        tipo_servico_element.click()

        # Use o pyautogui para pressionar as teclas de seta para baixo várias vezes
        for _ in range(5):
            pyautogui.hotkey('down')

        # Use o pyautogui para pressionar a tecla "tab" duas vezes
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')

        print('#### Selecionado Garantia Estendida - Zurich')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[2]').click()
        print('### Salvo cadastro')

        # Espera até que o botão "Excluir" esteja visível
        excluir_button = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/a[2]'))
        )
        excluir_button.click()

        # Espera até que o botão de confirmação esteja clicável
        confirm_button = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]'))
        )
        confirm_button.click()
        print('### Excluído cadastro')

    finally:
        # Feche o navegador
        print('>> Encerrando função configuracoes_tipos_servicos.')

navegador = Firefox()
navegador.maximize_window()
navegador.get(smart)
hora_inicio = datetime.datetime.now()
print('#######################################################################')
print('#                NÃO UTILIZE MOUSE E TECLADO                          #')
print('#######################################################################')
sleep(3)
print('### Navegador aberto.')

usuario_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'usuario')))
usuario_element.send_keys('robo.casa')
print('### Passei usuário.')


senha_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'senha')))
senha_element.send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)
configuracao_tipo_servico()
