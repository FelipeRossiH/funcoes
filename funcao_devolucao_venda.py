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


def devolucao_venda():
    nr_lcto = 97196
    print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/devolucoes_documentos")
        print("######### DEVOLUÇÃO DE VENDA ##########")
        print("Localizar campo Nº Lançamento")
        nome_element = navegador.find_element(By.ID, 'autocompletar_numero_lancamento')
        print("Informado lançamento: ", nr_lcto)
        nome_element.send_keys(nr_lcto)
        pyautogui.hotkey('tab')
        print("Informando operação devolução")
        sleep(3)
        navegador.find_element(By.ID, 'operacao_documento_id').click()
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('Enter')
        sleep(3)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="quantidade"]')
        nome_element.send_keys(1)
        pyautogui.hotkey('tab')
        print("Localizar e informar justificativa")
        navegador.find_element(By.ID, 'titulo_campo_justificativa_id').click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('Enter')
        print("Informando observação")
        nome_element = navegador.find_element(By.ID, 'observacoes_justificativa')
        nome_element.send_keys("Devolução automatizada")
        print("Finalizando devolução")
        navegador.find_element(By.ID, 'botao_devolve').click()
        sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
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
            navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")
    finally:
        print("Encerrando função devolucao_venda")


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

devolucao_venda()

#navegador.quit()
