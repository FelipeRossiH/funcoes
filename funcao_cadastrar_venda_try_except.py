import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from time import sleep
import datetime

nr_lcto = 0

def cadastrar_venda(numero_cliente, numero_produto):
    try:
        global nr_lcto
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")
        print('### Acessei Tela de Vendas')

        # Restante do código da função

    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro de venda: {str(e)}")

    finally:
        print("Encerrado função funcao_cadastrar_venda")
        # Não é necessário chamar navegador.quit() aqui, pois você já está fazendo isso no bloco `finally` no final do seu script.

def faturamento_de_venda():
    print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)
    # Restante do código da função

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

try:
    cadastrar_venda("12546", "7410")
    faturamento_de_venda()
except Exception as main_error:
    print(f"Ocorreu um erro durante a execução principal: {str(main_error)}")
finally:
    navegador.quit()