import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def open_url(driver, url):
    driver.get(url)
    sleep(2)

def login(driver):
    usuario_element = driver.find_element(By.NAME, 'usuario')
    usuario_element.send_keys('robo.casa')

    senha_element = driver.find_element(By.NAME, 'senha')
    senha_element.send_keys("Robo123" + Keys.ENTER)

    sleep(2)

def check_page(driver, url):
    open_url(driver, url)
    error_message = driver.find_elements(By.NAME, "filtros[nome]")
    if error_message:
        print(f"A página {url} foi aberta")
    else:
        global erro
        erro += 1
        print(f">>>>>>>>>>>>>>>>>>>>>>>>> A PÁGINA {url} CONTÉM ERRO")

cont = 0
erro = 0

smart_url = 'https://felipe.testes.smart.sgisistemas.com.br/'

navegador = webdriver.Firefox()
navegador.maximize_window()

try:
    open_url(navegador, smart_url)
    print('#######################################################################')
    print('#                NÃO UTILIZE MOUSE E TECLADO                          #')
    print('#######################################################################')
    print('### Navegador aberto.')

    login(navegador)

    urls_to_check = [
        "https://felipe.testes.smart.sgisistemas.com.br/pessoas",
        "https://felipe.testes.smart.sgisistemas.com.br/produtos",
        "https://felipe.testes.smart.sgisistemas.com.br/empresas/1/edit",
        "https://felipe.testes.smart.sgisistemas.com.br/relatorio_inventarios",
        "https://felipe.testes.smart.sgisistemas.com.br/relatorio_precos_produtos"
    ]

    for url in urls_to_check:
        check_page(navegador, url)
        cont += 1

finally:
    navegador.quit()
