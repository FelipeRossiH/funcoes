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

def configuracoes_tipos_montagens_produtos():
    #navegador = webdriver.Chrome()  # Certifique-se de que você tenha o driver do Chrome configurado

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_montagens_produtos")
        print('### Abrindo configuração de tipo de montagem por produto')

        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()
        print('### Selecionando escopo')
        print('Escopo Filial')
        navegador.find_element(By.XPATH,'//*[@id="escopo_type"]').click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        tp_mont = navegador.find_element(By.XPATH,'//*[@id="autocompletar_tipo_montagem_id"]')
        sleep(3)
        tp_mont.send_keys('Cliente')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div/div').click()
        sleep(3)
        inf_campo = navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div/div/ul[1]/li[1]/div')
        pyautogui.hotkey('B','a','s','e')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/input[2]').click()
        sleep(3)
        print('Escopo Departamento')
        navegador.find_element(By.XPATH,'//*[@id="escopo_type"]').click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        inf_campo = navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[7]/div/div/div/div/ul[1]/li[1]/div')
        inf_campo.click()
        sleep(3)
        pyautogui.hotkey('M','O','V','E')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/input[2]').click()
        sleep(3)
        print('Escopo Grupo do Produto')
        navegador.find_element(By.XPATH,'//*[@id="escopo_type"]').click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        inf_campo = navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[6]/div/div/div/div/ul[1]/li[1]/div')
        inf_campo.click()
        sleep(3)
        pyautogui.hotkey('P','L','A','N','E','J','A')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/input[2]').click()

        sleep(3)
        print('Escopo Subgrupo do Produto')
        navegador.find_element(By.XPATH,'//*[@id="escopo_type"]').click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        inf_campo = navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/div/div/div/ul[1]/li[1]/div')
        inf_campo.click()
        sleep(3)
        pyautogui.hotkey('H','O','M','E')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/input[2]').click()

        sleep(3)
        print('Produto')
        navegador.find_element(By.XPATH,'//*[@id="escopo_type"]').click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        inf_campo = navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/div/div/ul[1]/li[1]/div')
        inf_campo.click()
        sleep(3)
        pyautogui.hotkey('7','4','1','1')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(3)
        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/input[2]').click()
        print('### TODOS OS ESCOPOS FORAM CADASTRADOS')
        sleep(3)
        navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/a[2]').click()
        navegador.find_element(By.XPATH,'/html/body/div[8]/div/div/div[2]/button[2]').click()
        print('Realizado exclusão')
        sleep(3)
        print("#######################################################################")
    finally:
        #navegador.quit()
        print('>> Encerrando função configuracoes_tipos_montagens_produtos')

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

configuracoes_tipos_montagens_produtos()

navegador.quit()
