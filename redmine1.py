import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from datetime import datetime
import pandas as pd
import getpass

redmine = 'https://redmine.sgisistemas.com.br/login'


#userRedmine = input("Informe seu usuário: ")
#passwordRedmine = getpass.getpass("Informe sua senha: ")
#data_Inicial = input("Por favor, insira a data inicial do período de atualização no formato 'DD/MM/AAAA': ")
#dtIni = datetime.strptime(data_Inicial, '%d/%m/%Y')
#data_Final = input("Por favor, insira a data final do pe´riodo de atualização no formato 'DD/MM/AAAA': ")
#dtFim = datetime.strptime(data_Final, '%d/%m/%Y')
metaPeriodo = float(input("Informe a meta de horas para o período informado: "))

navegador = Firefox()
navegador.maximize_window()
navegador.get(redmine)

usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
#usuario.send_keys(userRedmine)
usuario.send_keys('felipe.rossi')

senha = navegador.find_element(By.XPATH, '//*[@id="password"]')
#senha.send_keys(passwordRedmine)
senha.send_keys('3971175Sgi')

navegador.find_element(By.XPATH, '//*[@id="login-submit"]').click()

sleep(2)

navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/a').click()

navegador.find_element(By.XPATH, '//*[@id="cb_status_id"]').click()

# navegador.find_element(By.XPATH, '//*[@id="add_filter_select"]').click()
# for i in range(38):
#     pyautogui.press('down')
# pyautogui.press('tab')

# navegador.find_element(By.XPATH, '//*[@id="operators_cf_27"]').click()
# for i in range(3):
#     pyautogui.press('down')
# pyautogui.press('tab')

# sleep(1)
# dataIni = navegador.find_element(By.ID, 'values_cf_27_1')
# #dataIni.click()
# #dataIni.send_keys(dataInicial)
# dataIni.send_keys(dtIni.strftime('%Y-%m-%d'))
# sleep(1)
# dataFim = navegador.find_element(By.ID, 'values_cf_27_2')
# #dataFim.click()
# #dataFim.send_keys(dataFinal)
# dataFim.send_keys(dtFim.strftime('%Y-%m-%d'))
# sleep(2)

consulta = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[1]/ul[3]/li[4]/a')
consulta.click()

csv = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/p/span[2]/a')
csv.click()

export = navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/p[4]/input')
export.click()
# print("Aguarda 5 segundos para download")
# for segundo_atual in range(5, 0, -1):
#     print(f"Tempo restante: {segundo_atual} segundos")
#     sleep(1)

print("Encerrando navegador...")
navegador.quit()



tmp_total = pd.read_csv(r'C:\\Users\\felip\\Downloads\\issues.csv', encoding='latin1', delimiter=';')

tmp_total['Tempo gasto geral'] = tmp_total['Tempo gasto geral'].str.replace(',', '.').astype(float)
soma_tempo_gasto = tmp_total['Tempo gasto geral'].sum()
quantidade_tipo = tmp_total['Tipo'].value_counts().to_string()
quantidade_situacao = tmp_total['Situação'].value_counts().to_string()

print(tmp_total)
diferenca = soma_tempo_gasto - metaPeriodo
print("A soma das horas da coluna 'Tempo gasto geral' é:", soma_tempo_gasto)
print("Diferença da meta para o realizado é: ", diferenca)
print("\nQuantidade de tarefas por 'Tipo':")
print(quantidade_tipo)
print("\nQuantidade tarefas por 'Situação':")
print(quantidade_situacao)


