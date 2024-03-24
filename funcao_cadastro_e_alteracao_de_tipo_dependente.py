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

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0

def cadastro_e_alteracao_de_tipo_dependente():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_dependentes")
        print('### Abrindo cadastro de tipo de dependente')

        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

        # Preenche o campo "descricao" com o valor "Tipo dependente automático"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Tipo dependente automático')
        print('### Preenchido campo "descricao" com "Tipo dependente automático"')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[2]').click()
        sleep(3)

        # Preenche o campo "descricao" com o valor "Tipo dependente alterada"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Tipo dependente alterada')
        print('### Preenchido campo "descricao" com "Tipo dependente alterada"')
        sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
        sleep(2)
        descricao = navegador.find_element(By.XPATH, '//*[@id="tipos_dependentes.descricao_ilike"]')
        sleep(0.5)
        descricao.click()
        descricao.send_keys('Tipo dependente automáticoTipo dependente alterada')
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]').click()
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/a[2]').click()
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
        sleep(1)

        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        msg_confirmacao = b_text[0:25]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'Excluído com Sucesso!':
          print("### Tela cadastro de escolaridade ok.")
        else:
          print(">>>>>>>>>>>>>> Erro na tela! Verificar.")
          erro = erro+1

    finally:
        print('>> Encerrando função cadastro_e_alteracao_de_tipo_dependente.')
        # Feche o navegador
        #navegador.quit()

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


cadastro_e_alteracao_de_tipo_dependente()
#navegador.quit()
