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

redmine = 'https://redmine.sgisistemas.com.br/login'


#userRedmine = input("Informe seu usuário: ")
#passwordRedmine = getpass.getpass("Informe sua senha: ")

navegador = Firefox()
navegador.maximize_window()
navegador.get(redmine)

usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
usuario.send_keys('felipe.rossi')

senha = navegador.find_element(By.XPATH, '//*[@id="password"]')
senha.send_keys('3971175Sgi')

navegador.find_element(By.XPATH, '//*[@id="login-submit"]').click()

sleep(2)

navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/a').click()

sleep(1)

filtro = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[1]/ul[3]/li[1]/a')
filtro.click()
sleep(1)

csv = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/p/span[2]/a')
csv.click()

export = navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/p[4]/input')
export.click()
sleep(2)
segundo_filtro = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[1]/ul[3]/li[6]/a')
segundo_filtro.click()
sleep(1)

csv = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div[2]/p/span[2]/a')
csv.click()

export = navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/p[4]/input')
export.click()



print("Encerrando navegador...")
navegador.quit()


correcoes = pd.read_csv(r'C:\\Users\\felip\\Downloads\\issues.csv', encoding='latin1', delimiter=';')
correcoes = correcoes.filter(['#', 'Atribuído para', 'Tempo gasto geral', 'Versão' ])

sprints = pd.read_csv(r'C:\\Users\\felip\\Downloads\\issues(1).csv', encoding='latin1', delimiter=';')
sprints = sprints.filter(['#', 'Atribuído para', 'Tempo gasto geral', 'Versão'])
contagem_por_versao = sprints.groupby('Versão')['#'].count()

sprints['Tempo gasto geral'] = sprints['Tempo gasto geral'].str.replace(',', '.').astype(float)
tempo_gasto_sprint = sprints['Tempo gasto geral'].sum()
quantidade_correcao_por_sprint = correcoes.groupby('Versão')['#'].count()

correcoes['Tempo gasto geral'] = correcoes['Tempo gasto geral'].str.replace(',', '.').astype(float)
soma_tempo_gasto = correcoes['Tempo gasto geral'].sum()
quantidade_correcoes = correcoes['#'].value_counts().sum()

quantidade_total_sprints = sprints['#'].value_counts().sum()

correcoes_por_versao = correcoes.groupby('Versão')['#'].count()
total_tarefas_correcao = correcoes['#'].count()

percent = (correcoes_por_versao / contagem_por_versao)*100


# for versao, quantidade in correcoes_por_versao.items():
#     percentual = (quantidade / total_tarefas_correcao) * 100
#     print(f"Versão {versao}: {percentual:.2f}%")

#tempo_gasto_sprint = float(tempo_gasto_sprint)
if tempo_gasto_sprint !=0: 
    print(correcoes)
    print("*********************************************************")
    print("Tempo gasto geral em sprint é: ", tempo_gasto_sprint)
    print("Tempo gasto geral em tarefas de correção é:", soma_tempo_gasto)
    print("\nQuantidade de tarefas de sprint:", quantidade_total_sprints)
    print("Quantidade de tarefas correção:", quantidade_correcoes)
    print("\nQuantidade de tarefas por sprint:", contagem_por_versao)
    print("Quantidade de tarefas de correcao por sprint:", correcoes_por_versao)
    print("\nQuantidade de tarefas de correção por Dev em cada sprint:")
    print(correcoes.groupby(['Atribuído para', 'Versão'])['#'].count())
    print("*********************************************************")
    print("Percentual de correção por sprint")
    print(percent)
    # print("Percentual de tarefas de correção por sprint")
    # for versao, quantidade in correcoes_por_versao.items():
    #     percentual = (quantidade / total_tarefas_correcao) * 100
    #     print(f"Versão {versao}: {percentual:.2f}%")
   # print("\nQuantidade de tarefas de correção por Dev em cada sprint:")
   # correcoes_grouped = correcoes.groupby(['Atribuído para', 'Versão'])['#'].count()
   # for index, value in correcoes_grouped.items():
   #     print(f"{index}: {value} ({(value/quantidade_correcoes)*100:.2f}%)")
else:
    print("Não temos tarefas de correção.")


# Configurações do email
email_remetente = 'felipe.rossi@sgisistemas.com.br'
email_destinatarios = ['feliperossihav@icloud.com', 'sgi.felipe@gmail.com', 'maykel@sgisistemas.com.br'] 
senha_remetente = '3971175Sgi!'  # Senha do remetente

# Construindo o email
msg = MIMEMultipart()
msg['From'] = email_remetente
msg['To'] = ', '.join(email_destinatarios)  # Transforma a lista em uma string separada por vírgulas
msg['Subject'] = 'ENVIO AUTOMÁTICO - Relatório de tarefas por sprint 2024 - Felipe Rossi'

if tempo_gasto_sprint != 0: 
    corpo_email = f"""\
    # RELATÓRIO DE TAREFAS POR SPRINT 2024
    ********************************************************************************************
    ## Quantidade total de tarefas de sprint: {quantidade_total_sprints}
    Tempo gasto geral em sprint é: {tempo_gasto_sprint}
    
    ## Quantidade de tarefas de correção: {quantidade_correcoes}
    Tempo gasto geral em tarefas de correção é: {soma_tempo_gasto}
    ********************************************************************************************
    ## Quantidade de tarefas por sprint: {contagem_por_versao}
    Quantidade de tarefas de correcao por sprint: {correcoes_por_versao}
    ********************************************************************************************
    ## Quantidade de tarefas de correção por Dev em cada sprint:
    {correcoes.groupby(['Atribuído para', 'Versão'])['#'].count()}
    ********************************************************************************************
    ## Percentual de tarefas de correção por sprint:
    {percent}
    """
    # Calcular o percentual de tarefas de correção para cada versão
    # for versao, quantidade in correcoes_por_versao.items():
    #     percentual = (quantidade / total_tarefas_correcao) * 100
    #     corpo_email += f"Versão {versao}: {percentual:.2f}%\n"
    
        
else:
    corpo_email = f"""
    Não temos tarefas para exibição.
    """

msg.attach(MIMEText(corpo_email, 'plain'))

# Configurações do servidor SMTP
smtp_server = 'smtp.sgisistemas.com.br'
smtp_port = 587  # Porta para TLS

# Iniciando conexão com o servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Inicia conexão TLS (Transport Layer Security) para criptografar a comunicação


# Fazendo login no servidor SMTP
server.login(email_remetente, senha_remetente)

# Enviando email
server.sendmail(email_remetente, email_destinatarios, msg.as_string())

# Finalizando conexão com o servidor SMTP
server.quit()

print("Email enviado com sucesso!")