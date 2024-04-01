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
import datetime
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.common.exceptions import TimeoutException
import clipboard


def cadastro_departamento():
    try:
        data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
        descricao = 'Departamento de Teste'

        cadDepartamento = f"{descricao} - {data_atual}"

        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/departamentos_produtos")
        print("Acessei cadastro de Departamentos")
        btnAdicionar = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
        btnAdicionar.click()
        #print("Cliquei em adicionar")
        descricaoDepto = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="descricao"]'))
        )
        descricaoDepto.send_keys(cadDepartamento)
        #print("Adicionei descrição")
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
        #print("Cliquei salvar cadastro")
        sleep(5)
        
        #print("Tempo de mensagem de confirmação")
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        msg_confirmacao = b_text[0:25]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'Adicionado com Sucesso!':
          print("### Cadastrado Departamento com sucesso: ", cadDepartamento)
        else:
          print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro do departamento: {str(e)}")

    finally:
        print("Encerrado função cadastro de departamento")

def cadastro_grupo():
    try:

        data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
        descricao = 'Grupo de Teste'

        cadGrupo = f"{descricao} - {data_atual}"
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_produtos")
        #print("Acessei cadastro de Grupo")
        btnAdicionar = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
        btnAdicionar.click()
        #print("Cliquei em Adicionar")

        descricaoGrupo = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="descricao"]'))
        )
        descricaoGrupo.send_keys(cadGrupo)
        #print("Informei descrição")
        sleep(2)
        dptoProduto = navegador.find_element(By.XPATH, '//*[@id="autocompletar_departamento_produto_id"]')
        #print("Localizei campo Departamento do Produto")
        dptoProduto.click()
        #print("Cliquei no campo Departamento do Produto")
        dptoProduto.send_keys(data_atual)
        sleep(3)
        pyautogui.press('down')
        pyautogui.press('tab')

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
        sleep(3)
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        msg_confirmacao = b_text[0:25]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'Adicionado com Sucesso!':
          print("### Cadastrado Grupo com sucesso: ", cadGrupo)
        else:
          print(">>>>>>>>>>>>>> Erro na tela! Verificar.")



    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro do grupo: {str(e)}")

    finally:
        print("Encerrado função cadastro de grupo")

def cadastro_subgrupo():
   try:
       data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
       descricao = 'SubGrupo de Teste'
       cadSubgrupo = f"{descricao} - {data_atual}"

       navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subgrupos_produtos")
       print("Acessei cadastro de Grupo")
       btnAdicionar = WebDriverWait(navegador, 10).until(
           EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
       )
       btnAdicionar.click()
       #print("Cliquei em Adicionar")

       descricaoSubgrupo = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="descricao"]'))
        )
       descricaoSubgrupo.send_keys(cadSubgrupo)
       #print("Informei descrição")
       sleep(2)

       grupoProduto = navegador.find_element(By.XPATH, '//*[@id="autocompletar_grupo_produto_id"]')
       #print("Localizei campo Grupo do Produto")
       grupoProduto.click()
       #print("Cliquei no campo Departamento do Produto")
       grupoProduto.send_keys(data_atual)
       sleep(3)
       pyautogui.press('down')
       pyautogui.press('tab')

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
       sleep(3)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:25]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Cadastrado SubGrupo com sucesso: ", cadSubgrupo)
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")
      
   except Exception as e:
        print(f"Ocorreu um erro durante o cadastro do grupo: {str(e)}")

   finally:
        print("Encerrado função cadastro de grupo")
      
def cadastro_marca():
   try:
       data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
       descricao = 'Marca de Teste'
       cadMarca = f"{descricao} - {data_atual}"

       navegador.get('https://felipe.testes.smart.sgisistemas.com.br/marcas_produtos')
       print("Acessei cadastro de Marca")
       btnAdicionar = WebDriverWait(navegador, 10).until(
           EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
       )
       btnAdicionar.click()
       #print("Cliquei em Adicionar")

       descricaoMarca = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="descricao"]'))
        )
       descricaoMarca.send_keys(cadMarca)
       
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
       sleep(3)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
       b_text = b_element.text
       msg_confirmacao = b_text[0:25]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Cadastrado SubGrupo com sucesso: ", cadMarca)
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")    



   except Exception as e:
        print(f"Ocorreu um erro durante o cadastro da marca: {str(e)}")

   finally:
        print("Encerrado função cadastro da marca")
      
    






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

cadastro_departamento()
cadastro_grupo()
cadastro_subgrupo()
cadastro_marca()
