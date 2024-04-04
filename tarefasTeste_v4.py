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

navegador = Firefox()
navegador.maximize_window()
navegador.get(redmine)

print("Informando usuário.")
usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
usuario.send_keys(userRedmine)

print("Informando senha")
senha = navegador.find_element(By.XPATH, '//*[@id="password"]')
senha.send_keys(passwordRedmine)

navegador.find_element(By.XPATH, '//*[@id="login-submit"]').click()
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

for _ in range(34):
    pyautogui.hotkey('down')
pyautogui.hotkey('tab')

filtroData = navegador.find_element(By.XPATH, '//*[@id="operators_start_date"]')
filtroData.click()

for _ in range(3):
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

coluna_tempo_estimado_geral = navegador.find_element(By.XPATH,
                                                      '/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/div/table/tbody/tr[1]/td[2]/span/span[1]/select/option[10]')
action_chains = ActionChains(navegador)
action_chains.double_click(coluna_tempo_estimado_geral).perform()

coluna_tempo_gasto = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/div/table/tbody/tr[1]/td[2]/span/span[1]/select/option[10]')
pyautogui.hotkey('down')
pyautogui.hotkey('down')
coluna_tempo_gasto_geral = navegador.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/div/table/tbody/tr[1]/td[2]/span/span[1]/select/option[11]')
action_chains = ActionChains(navegador)
action_chains.double_click(coluna_tempo_gasto_geral).perform()

inicio_tarefa = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/form[1]/div/div/fieldset[2]/div/table/tbody/tr[1]/td[2]/span/span[1]/select/option[7]')
action_chains = ActionChains(navegador)
action_chains.double_click(inicio_tarefa).perform()

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

soma_tempo_gasto = trf_teste['Tempo gasto geral'].sum()
soma_tempo_estimado = trf_teste['Tempo estimado geral'].sum()
diferenca = soma_tempo_estimado - soma_tempo_gasto
projeto = trf_teste['Projeto'].value_counts().to_string()
tipo = trf_teste['Tipo'].value_counts().to_string()

# Filtrando apenas tarefas de manutenção
manutencao = trf_teste.loc[trf_teste['Tipo'] == 'Manutenção']

# Agrupando por mês e contando a quantidade de tarefas de manutenção
quantidade_por_mes = manutencao.groupby(manutencao['Data de criação'].dt.to_period('M')).size()

print("##############################################################################################")
print(trf_teste.to_string(index=False))
print("##############################################################################################")
print("RELATORIO COM DADOS DE TAREFAS DO PERÍODO DE ", data_Inicial, "ATÉ ", data_Final)
print("Quantidade total de tarefas:", len(trf_teste))
print("Soma das horas estimadas de todas as tarefas:", soma_tempo_estimado)
print("Soma das horas gastas de todas as tarefas:", soma_tempo_gasto)
print("Diferença da quantidade de horas estimadas e quantidade de horas gastas:", diferenca)
print("----------------------------------------------------------------------------------------------")
print("Quantidade de tarefa por projeto:\n", projeto)
print("----------------------------------------------------------------------------------------------")
print("Quantidade de tarefa por tipo:\n", tipo)
print("----------------------------------------------------------------------------------------------")
print("Quantidade de tarefas de manutenção por mês:")
print(quantidade_por_mes)
print(trf_teste)

email_remetente = 'felipe.rossi@sgisistemas.com.br'
email_destinatarios = ['feliperossihav@icloud.com', 'sgi.felipe@gmail.com', 'felipe.rossi@sgisistemas.com.br']
senha_remetente = '3971175Sgi!'

msg = MIMEMultipart()
msg['From'] = email_remetente
msg['To'] = ', '.join(email_destinatarios)
msg['Subject'] = 'ENVIO AUTOMÁTICO - Relatório de tarefas por período informado - Felipe Rossi'

if quantidade_tarefa_teste > 0:
    corpo_email = f"""\
##############################################################################################
RELATORIO COM DADOS DE TAREFAS DO PERÍODO DE {data_Inicial} ATÉ {data_Final}
Quantidade total de tarefas: {len(trf_teste)}
Soma das horas estimadas de todas as tarefas: {soma_tempo_estimado}
Soma das horas gastas de todas as tarefas: {soma_tempo_gasto}
Diferença da quantidade de horas estimadas e quantidade de horas gastas: {diferenca}
----------------------------------------------------------------------------------------------
Quantidade de tarefa por projeto:
{projeto}
----------------------------------------------------------------------------------------------
Quantidade de tarefa por tipo:
{tipo}
----------------------------------------------------------------------------------------------
Quantidade de tarefas do tipo teste: {quantidade_tarefa_teste}
Quantidade de tarefas de teste por usuário:
{tarefas_por_usuario_teste}
----------------------------------------------------------------------------------------------
Quantidade de tarefas do tipo desenvolvimento: {quantidade_tarefa_desenvolvimento}
Quantidade de tarefas de desenvolvimento por usuário:
{tarefas_por_usuario_desenvolvimento}
----------------------------------------------------------------------------------------------
Quantidade de tarefas de 'Correção': {quantidade_tarefa_correcao}
Quantidade de tarefas de correção por usuário:
{tarefas_por_usuario_correcao}
----------------------------------------------------------------------------------------------
{trf_teste}
##############################################################################################
"""
else:
    corpo_email = f"""
Não temos tarefas no período.
"""

msg.attach(MIMEText(corpo_email, 'plain'))

smtp_server = 'smtp.sgisistemas.com.br'
smtp_port = 587

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

server.login(email_remetente, senha_remetente)

server.sendmail(email_remetente, email_destinatarios, msg.as_string())

server.quit()

print("Email enviado com sucesso!")
