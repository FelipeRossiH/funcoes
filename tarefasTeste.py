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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


redmine = 'https://redmine.sgisistemas.com.br/login'

print("ACESSANDO REDMINE SGI SISTEMAS")
print("UTILIZE MOUSE E TECLADO SOMENTE QUANDO SOLICITADO.")
userRedmine = input("Informe seu usuário: ")
passwordRedmine = getpass.getpass("Informe sua senha: ")
data_Inicial = input("Por favor, insira a data inicial das tarefas no formato 'DD/MM/AAAA': ")
dtIni = datetime.strptime(data_Inicial, '%d/%m/%Y')
data_Final = input("Por favor, insira a data final das tarefas no formato 'DD/MM/AAAA': ")
dtFim = datetime.strptime(data_Final, '%d/%m/%Y')
print("SERÃO FILTRADAS TAREFAS DO PERÍODO DE: ", data_Inicial, "ATÉ", data_Final)
#metaPeriodo = float(input("Informe a meta de horas para o período informado: "))
#metaPeriodo = 1117
navegador = Firefox()
navegador.maximize_window()
navegador.get(redmine)

print("Informando usuário.")
usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
usuario.send_keys(userRedmine)
#usuario.send_keys('felipe.rossi')
print("Informando senha")
senha = navegador.find_element(By.XPATH, '//*[@id="password"]')
senha.send_keys(passwordRedmine)
#senha.send_keys('3971175Sgi')

navegador.find_element(By.XPATH, '//*[@id="login-submit"]').click()
print("Acessando")
sleep(2)
print("Abrindo página inicial para o usuario: ", userRedmine)
pagina_inicial = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/a')
pagina_inicial.click()

print("Desmarco situação das tarefas")
situacao_tarefa = navegador.find_element(By.XPATH, '//*[@id="cb_status_id"]')
situacao_tarefa.click()

print("Adicionando filtro de data")
adiciona_filtro = navegador.find_element(By.XPATH, '//*[@id="add_filter_select"]')
adiciona_filtro.click()

opcao_filtro = 0
for opcao_filtro in range(34):
    pyautogui.hotkey('down')
pyautogui.hotkey('tab')

filtroData = navegador.find_element(By.XPATH, '//*[@id="operators_start_date"]')
filtroData.click()

for opcao_filtro_data in range(3):
    pyautogui.hotkey('down')
pyautogui.hotkey('tab')

print("Informando data inicial: ", data_Inicial)
filtro_data_inicial = navegador.find_element(By.XPATH, '//*[@id="values_start_date_1"]')
filtro_data_inicial.click()
filtro_data_inicial.send_keys(dtIni.strftime('%Y-%m-%d'))

print("Informando data final: ", data_Final)
filtro_data_final = navegador.find_element(By.XPATH, '//*[@id="values_start_date_2"]')
filtro_data_final.click()
filtro_data_final.send_keys(dtFim.strftime('%Y-%m-%d'))

print("Aplicando filtros")
btnAplicar = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/form[1]/div/p/a[1]')
btnAplicar.click()

print("Adicionando colunas")
opcoes_colunas = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/legend')
opcoes_colunas.click()

coluna_tempo_estimado_geral = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/div/table/tbody/tr[1]/td[2]/span/span[1]/select/option[10]')
action_chains = ActionChains(navegador)
action_chains.double_click(coluna_tempo_estimado_geral).perform()

coluna_tempo_gasto = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/div/table/tbody/tr[1]/td[2]/span/span[1]/select/option[10]')
#coluna_tempo_gasto.click()
pyautogui.hotkey('down')
pyautogui.hotkey('down')
coluna_tempo_gasto_geral = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/div/table/tbody/tr[1]/td[2]/span/span[1]/select/option[11]')
action_chains = ActionChains(navegador)
action_chains.double_click(coluna_tempo_gasto_geral).perform()

print("Aplicando busca")
btnAplicar = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/form[1]/div/p/a[1]')
btnAplicar.click()

print("Gerando CSV")
gera_csv = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/p/span[2]/a')
gera_csv.click()

exportar = navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/p[4]/input')
exportar.click()

print("Encerrando navegador...")
navegador.quit()

print("Lendo arquivo")
trf_teste = pd.read_csv(r'C:\\Users\\felip\\Downloads\\issues.csv', encoding='latin1', delimiter=';')
trf_teste = trf_teste.filter(['#', 'Projeto', 'Tipo', 'Título', 'Situação', 'Atribuído para', 'Tempo estimado geral', 'Tempo gasto geral'])

trf_teste['Tempo estimado geral'].fillna(0, inplace=True)
trf_teste['Tempo estimado geral'] = pd.to_numeric(trf_teste['Tempo estimado geral'], errors='coerce')

trf_teste['Tempo gasto geral'].fillna(0, inplace=True)
trf_teste['Tempo gasto geral'] = pd.to_numeric(trf_teste['Tempo gasto geral'], errors='coerce')

tmp_estimado = trf_teste['Tempo estimado geral']
tmp_gasto = trf_teste['Tempo gasto geral']

soma_tempo_gasto = tmp_gasto.sum()
soma_tempo_estimado = tmp_estimado.sum()
diferenca = soma_tempo_estimado - soma_tempo_gasto
projeto = trf_teste['Projeto'].value_counts().to_string()
tipo = trf_teste['Tipo'].value_counts().to_string()

qa = ''
dev = ''


so_tarefa_teste = trf_teste.loc[trf_teste['Tipo'] == 'Teste']
usuarios_teste = so_tarefa_teste['Atribuído para'].unique()
quantidade_tarefa_teste = len(so_tarefa_teste)
tarefas_por_usuario = so_tarefa_teste['Atribuído para'].value_counts()

print("RELATORIO COM DADOS DE TAREFAS DO PERÍODO DE ", data_Inicial, "ATÉ ", data_Final)
#print(trf_teste)
print("Soma de tempos estimados para as tarefas: \n", tmp_estimado)
print("Soma de tempos gastos nas tarefas: \n", tmp_gasto)
print("Diferença Estimado/Gasto: ", diferenca)
print("Quantidade de tarefas por Projeto: \n", projeto)
print("Quantidade de tarefas por Tipo: \n", tipo)
#print("Quantidade de tarefas por QA: ", qa)
#print("Quantidade de tarefa de correção por desenvolvedor: ", dev)
print("só tarefa de teste: ", quantidade_tarefa_teste)
print("Usuários aos quais as tarefas de teste estão atribuídas:")
# for usuario in usuarios_teste:
#     print(usuario)
print("Quantidade de tarefas de teste atribuídas a cada usuário:")
print(tarefas_por_usuario)