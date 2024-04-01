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


def cadastro_de_produto():
    try:
        data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
        descricao = 'Cadastro automático de produto.'
        descProduto = f"{descricao} - {data_atual}"

        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos")

        btnAdicionar = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
        btnAdicionar.click()

        descricaoProduto = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        descricaoProduto.send_keys(descProduto)

        subgrupo = navegador.find_element(By.XPATH, '//*[@id="autocompletar_subgrupo_produto_id"]')
        subgrupo.send_keys(data_atual)
        sleep(2)

        pyautogui.press('down')
        pyautogui.press('tab')

        marca = navegador.find_element(By.XPATH, '//*[@id="autocompletar_marca_produto_id"]')
        marca.send_keys(data_atual)
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        undMedida = navegador.find_element(By.XPATH, '//*[@id="autocompletar_unidade_medida_id"]')
        undMedida.send_keys('UN')
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        tributacao = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/ul/li[3]/a')
        tributacao.click()
        sleep(2)

        origem = navegador.find_element(By.XPATH, '//*[@id="autocompletar_origem_produto_id"]')
        origem.send_keys('Nacional, exceto as indicadas nos códigos 3 a 5.')
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        ncm = navegador.find_element(By.XPATH, '//*[@id="autocompletar_ncm_id"]')
        ncm.send_keys('9403.91.00')
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        sleep(2)

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/input[1]').click()

        sleep(3)
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        msg_confirmacao = b_text[0:25]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'Adicionado com Sucesso!':
          print("### Cadastrado SubGrupo com sucesso: ")
        else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")    

    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro do produto: {str(e)}")

    finally:
         print("Encerrado função cadastro de produto")
 




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


cadastro_de_produto()