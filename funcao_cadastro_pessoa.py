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


def cadastrar_pessoa():
    #navegador = webdriver.Chrome()  # Certifique-se de que você tenha o driver do Chrome configurado
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pessoas/new")
    print('### Acessei Tela Pessoa')

    print('### Abrindo Gerador de CPF. ')
    url = 'https://www.4devs.com.br/gerador_de_cpf'
    print('#### Aguardando ...')

    navegador.execute_script("window.open('');")  # Abre uma nova janela do navegador
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[1])
    navegador.get(url)

    print('### Novo navegador aberto.\n#### Gerador de CPF\n##### 3 segundos para prosseguir')
    sleep(5)

    navegador.find_element(By.ID, 'bt_gerar_cpf').click()
    sleep(3)
    navegador.find_element(By.ID, 'texto_cpf').click()
    sleep(3)
    navegador.find_element(By.CLASS_NAME, "clipboard-copy").click()
    print('### CPF copiado.')
    CPFcopiado = clipboard.paste()
    sleep(3)
    navegador.close()
    navegador.switch_to.window(janelas[0])
    print('### Gerador de CPF encerrado.')

    nome_element = navegador.find_element(By.NAME, 'pessoa[nome]')
    nome_element.send_keys('Nome automatizado')
    print('### Passei nome.')

    nome_element = navegador.find_element(By.NAME, 'pessoa[apelido]')
    nome_element.send_keys('Apelido automatizado')
    print('### Passei apelido.')

    sleep(3)
    navegador.find_element(By.NAME, 'pessoa[cpf_cnpj]').click()
    pyautogui.hotkey('ctrl', 'v')
    sleep(3)
    print('### CPF inserido: ', CPFcopiado)

    nome_element = navegador.find_element(By.NAME, 'pessoa[data_nascimento_fundacao]')
    nome_element.send_keys('19/02/1990')
    print('### Passei data de nascimento.')

    navegador.find_element(By.NAME, 'pessoa[identidade]')

    elemento = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[17]/ul/li[2]/a')
    sleep(3)
    elemento.click()
    sleep(2)

    navegador.find_element(By.ID, 'tipo_endereco_id_0').click()
    nome_element = navegador.find_element(By.ID, 'tipo_endereco_id_0')
    nome_element.send_keys('R')
    print('### Passei tipo de endereço.')

    nome_element = navegador.find_element(By.ID, 'autocompletar_cep_id_0')
    nome_element.send_keys('89805-545')
    print('### Passei CEP.')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')

    nome_element = navegador.find_element(By.ID, 'numero_0')
    nome_element.send_keys('322')
    print('### Passei número de endereço.')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')

    elemento = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[19]/div/input[2]')
    elemento.click()

    hora_fim = datetime.datetime.now()
    print('Fim de execução: ', hora_fim)
    tempo_total = (hora_fim - hora_inicio)
    sleep(2)

    print('###### Pessoa física cadastrada com sucesso\n##### CPF cadastrado: ', CPFcopiado, 'Tempo de execução: ', tempo_total)
    print('Encerrado função cadastro_pessoa')

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

cadastrar_pessoa()

navegador.quit()
