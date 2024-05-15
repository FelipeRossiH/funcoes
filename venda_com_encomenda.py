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
import datetime

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0

# def venda_com_encomenda(numero_cliente, numero_produto):

#     try:
#         global nr_lcto
#         print('########## TELA PEDIDO DE VENDA ##########')
#         navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")


#         # Preencher o campo "Cliente"
#         nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
#         nome_element.send_keys(numero_cliente)
#         print('### Passei Cliente', numero_cliente)
#         sleep(5)
#         pyautogui.hotkey('down')
#         pyautogui.hotkey('tab')

#         # Preencher o campo "Produto"
#         nome_element = navegador.find_element(By.ID, 'coluna_descricao_produto')
#         sleep(2)
#         nome_element.send_keys(numero_produto)
#         print('### Passei produto.')
#         sleep(2)
#         pyautogui.hotkey('down')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('ENTER')

#         # Preencher o campo "Quantidade"
#         sleep(3)
#         nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
#         sleep(2)
#         nome_element.send_keys('1')
#         print('### Passei quantidade.')
#         pyautogui.hotkey('ENTER')
        
#         # Marcar encomenda
#         sleep(3)
#         nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[16]/div/div[2]/div/div/div[1]/div[1]/table/tbody/tr/td[13]/label')
#         sleep(1)
#         nome_element.click()
#         print("Marquei a encomenda do produto.")



#         # Preencher o campo "Forma de Pagamento"
#         nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
#         nome_element.send_keys('Dinheiro')
#         sleep(3)
#         pyautogui.hotkey('ENTER')
#         print('### Passei forma de pagamento Dinheiro')

    
#         # Clicar no botão "Salvar"
#         navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
#         #sleep(10)
#         print("Aguarda 10 segundos para liberação")
#         for segundo_atual in range(10, 0, -1):
#             print(f"Tempo restante: {segundo_atual} segundos")
#             sleep(1)


#         # Obter número do lançamento
#         b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
#         b_text = b_element.text
#         nr_lcto = b_text[14:19]
#         print('#### Número do lançamento: ', nr_lcto)
#         sleep(12)



               
#     except Exception as e:
#         print(f"Ocorreu um erro: {str(e)}")

#     finally:
#         print("Encerrado função funcao_cadastrar_venda")
#         #navegador.quit()

# from selenium.common.exceptions import NoSuchElementException
# def venda_com_encomenda(numero_cliente, numero_produto):

#     try:
#         global nr_lcto
#         hora_inicio = datetime.datetime.now()
#         print("Tempo iniciado")
#         print('########## TELA PEDIDO DE VENDA (Venda Com Encomenda) ##########')
#         navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")


#         # Preencher o campo "Cliente"
#         nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
#         nome_element.send_keys(numero_cliente)
#         print('### Passei Cliente', numero_cliente)
#         sleep(3)
#         pyautogui.hotkey('down')
#         pyautogui.hotkey('tab')

#         # Preencher o campo "Produto"
#         nome_element = navegador.find_element(By.ID, 'coluna_descricao_produto')
#         sleep(2)
#         nome_element.send_keys(numero_produto)
#         print('### Passei produto.')
#         sleep(2)
#         pyautogui.hotkey('down')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('ENTER')

#         # Preencher o campo "Quantidade"
#         sleep(1)
#         nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
#         sleep(1)
#         nome_element.send_keys('1')
#         print('### Passei quantidade.')
#         pyautogui.hotkey('ENTER')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('tab')
        
#         # Marcar encomenda
#         print("Buscar flag entrega")
#         sleep(1)
#         nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[16]/div/div[2]/div/div/div[1]/div[1]/table/tbody/tr/td[13]/label')
#         sleep(1)
#         print("Encontrado campo marcação de entrega")
#         nome_element.click()
#         print("Marquei a encomenda do produto.")



#         # Preencher o campo "Forma de Pagamento"
#         nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
#         nome_element.send_keys('Dinheiro')
#         sleep(1)
#         pyautogui.hotkey('ENTER')
#         print('### Passei forma de pagamento Dinheiro')

    
#         # Clicar no botão "Salvar"
#         navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
#         #sleep(10)
#         #print("Aguarda 7 segundos para liberação")
#         for segundo_atual in range(1, 0, -1):
#            # print(f"Tempo restante: {segundo_atual} segundos")
#             sleep(1)

#         #sleep(20)
#         # Obter número do lançamento
#         while True:
#             try:
#                 b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
#                 b_text = b_element.text
#                 nr_lcto = b_text[14:19]
#                 print('#### Número do lançamento: ', nr_lcto)
#                 break
#             except NoSuchElementException:
#                 #print("Aguardando elemento...")
#                 sleep(1)
#         hora_fim = datetime.datetime.now()
#         print("Tempo Finalizado")



               
#     except Exception as e:
#         print(f"Ocorreu um erro: {str(e)}")

#     finally:
        
#         tempo_total = (hora_fim - hora_inicio)
#         print("Tempo de execução", tempo_total)  
#         print("Encerrado função funcao_cadastrar_venda")
#         #navegador.quit()


from selenium.common.exceptions import NoSuchElementException
def venda_com_encomenda(numero_cliente, numero_produto):

    try:
        global nr_lcto
        print('########## TELA PEDIDO DE VENDA (Venda Com Encomenda) ##########')
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")


        # Preencher o campo "Cliente"
        nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
        nome_element.send_keys(numero_cliente)
        print('### Passei Cliente', numero_cliente)
        sleep(5)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Preencher o campo "Produto"
        nome_element = navegador.find_element(By.ID, 'coluna_descricao_produto')
        sleep(2)
        nome_element.send_keys(numero_produto)
        print('### Passei produto.')
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('ENTER')

        # Preencher o campo "Quantidade"
        sleep(5)
        nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
        sleep(5)
        nome_element.send_keys('1')
        print('### Passei quantidade.')
        pyautogui.hotkey('ENTER')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        
        # Marcar encomenda
        print("Buscar flag entrega")
        sleep(5)
        nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[17]/div/div[2]/div/div/div[1]/div[1]/table/tbody/tr/td[13]/label')
        sleep(5)
        print("Encontrado campo marcação de entrega")
        nome_element.click()
        print("Marquei a encomenda do produto.")



        # Preencher o campo "Forma de Pagamento"
        nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
        nome_element.send_keys('Dinheiro')
        sleep(5)
        pyautogui.hotkey('ENTER')
        print('### Passei forma de pagamento Dinheiro')

    
        # Clicar no botão "Salvar"
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        #sleep(10)
        print("Aguarda 20 segundos para liberação")
        for segundo_atual in range(20, 0, -1):
            print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)

        sleep(20)
        # Obter número do lançamento
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        nr_lcto = b_text[14:19]
        print('#### Número do lançamento: ', nr_lcto)
        sleep(12)



               
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    finally:
        print("Encerrado função funcao_cadastrar_venda")
        #navegador.quit()


def faturamento_de_venda():

  try:
      print("########## TELA RECEBIMENTOS ##########")
      print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)
      navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recebimentos")
      print("Localizar campo Nº Lançamento")
      nome_element = navegador.find_element(By.XPATH,'//*[@id="numeros_lancamentos"]')
      sleep(3)
      nome_element.send_keys(nr_lcto)
      pyautogui.hotkey('tab')
      sleep(3)
      nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/div/div/div[2]/div/div[4]/div/div/table/tbody/tr/td[1]/label').click()
      sleep(3)
      scroll_to_bottom_script = "window.scrollTo(0, document.body.scrollHeight);"
      # Executa o script para rolar a página
      navegador.execute_script(scroll_to_bottom_script)
      sleep(10)
      nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/button').click()
      print('Finalizado Lançamento')
      sleep(20)

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
      print("Encerrado função funcao_fatura_lcto")

def encomenda_de_produto():
    try:
        print("########## TELA ENCOMENDA DE PRODUTOS ##########")
        print("Recebido da função venda com encomenda o lançamento: ", nr_lcto)
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/encomendas_produtos")
        sleep(2)

        nr_lancamento = navegador.find_element(By.XPATH, '//*[@id="documentos.numero_lancamento"]')
        sleep(1)
        nr_lancamento.send_keys(nr_lcto)
        pyautogui.hotkey('Enter')
        sleep(1)
        checkbox = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[3]/div[1]/table/tbody/tr/td[1]/div/label')
        sleep(1)
        checkbox.click()
        sleep(1)

        gerar_pedido_compra = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[4]/button')
        sleep(1)
        gerar_pedido_compra.click()

        sleep(5)

        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        msg_confirmacao = b_text[0:99]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(1)

        if msg_confirmacao == 'Gerado com sucesso!':
            print("### Encomenda gravada com sucesso.")
        else:
            print(">>>>>>>>>>>>>> Erro na tela! Verificar.")
            
    finally:
       print("Encerrado função venda_com_encomenda")
       navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")


navegador = Firefox()
navegador.maximize_window()
navegador.get(smart)
#hora_inicio = datetime.datetime.now()
cont = 0
erro = 0

print('#######################################################################')
print('#                NÃO UTILIZE MOUSE E TECLADO                          #')
print('#######################################################################')
sleep(3)
print('### Navegador aberto.')

usuario_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'usuario')))
usuario_element.send_keys('robo.robo')
print('### Passei usuário.')


senha_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'senha')))
senha_element.send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)


venda_com_encomenda("12546", "7410")
#faturamento_de_venda()
#encomenda_de_produto()

hora_fim = datetime.datetime.now()
#tempo_total = (hora_fim - hora_inicio)

# Configurações do email
email_remetente = 'felipe.rossi@sgisistemas.com.br'
email_destinatarios = ['feliperossihav@icloud.com', 'sgi.felipe@gmail.com', 'gabrielama@unochapeco.edu.br']  # Lista de destinatários
senha_remetente = '3971175Sgi!'  # Senha do remetente

# Construindo o email
msg = MIMEMultipart()
msg['From'] = email_remetente
msg['To'] = ', '.join(email_destinatarios)  # Transforma a lista em uma string separada por vírgulas
msg['Subject'] = 'ENVIO AUTOMÁTICO - Relatório de Execução Automação - Felipe Rossi'

# Corpo do email com as variáveis
corpo_email = f"""\
Robô iniciado em 
Robô finalizado em {hora_fim}
Tempo de execução: 
Quantidade de telas verificadas: {cont}
Telas com erro: {erro}
Funções executadas
cadastrar_venda("12546", "7410")
analise_credito()
faturamento_de_venda()
gestao_entrega()
cadastrar_pessoa()
cadastro_e_alteracao_de_escolaridade()
cadastro_e_alteracao_de_tipo_dependente()
configuracoes_mva_antecipacoes()
configuracao_tipo_servico()
adicionar_especificacao_produto()
configuracoes_tipos_montagens_produtos()
gera_titulo()
funcao_gera_sped_fiscal()
funcao_gera_sped_contribuicao()
funcao_gera_cobranca()
devolucao_venda()
pedido_compra()
lancamento_entrada()
venda_com_encomenda("12546", "7410")
faturamento_de_venda()
encomenda_de_produto()
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