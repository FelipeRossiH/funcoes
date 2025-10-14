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
from selenium.common.exceptions import TimeoutException




navegador = Firefox()
smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0
nr_lcto = 0
tela = 0



def cadastro_e_alteracao_de_escolaridade():


    try:
        print("Cadastro e alteração de escolaridade")
        sleep(3) 

        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escolaridades")
        print('### Abrindo cadastro de escolaridade')

        
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

        
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Escolaridade Automática')
        print('### Preenchido campo "descricao" com "Escolaridade Automática"')

        
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
        sleep(3)

        
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Escolaridade Automática Alterada')
        print('### Preenchido campo "descricao" com "Escolaridade Automática Alterada')
        sleep(3)

        
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[1]').click()
        sleep(3)

        
        codigo_escolaridade = navegador.find_element(By.CLASS_NAME, "campo_id")
        print('### Código da escolaridade:', codigo_escolaridade.text)

        descricao_escolaridade = navegador.find_element(By.XPATH, '//*[@id="escolaridades.descricao_ilike"]')
        descricao_escolaridade.send_keys("Escolaridade AutomáticaEscolaridade Automática Alterada")
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]').click()
        sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
        sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[2]').click()
        sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
        sleep(5)
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
        b_text = b_element.text
        msg_confirmacao = b_text[0:25]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'Excluído com Sucesso!':
          print("### Tela cadastro de escolaridade ok.")
        else:
          print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

    finally:
        print('>> Encerrando função cadastro_e_alteracao_de_escolaridade.')
    

def cadastro_e_alteracao_de_tipo_dependente():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_dependentes")
        print('### Abrindo cadastro de tipo de dependente')

        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

        # Preenche o campo "descricao" com o valor "Tipo dependente automático"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Tipo dependente automático')
        print('### Preenchido campo "descricao" com "Tipo dependente automático"')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[2]').click()
        sleep(3)

        # Preenche o campo "descricao" com o valor "Tipo dependente alterada"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Tipo dependente alterada')
        print('### Preenchido campo "descricao" com "Tipo dependente alterada"')
        sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
        sleep(5)
        descricao = navegador.find_element(By.XPATH, '//*[@id="tipos_dependentes.descricao_ilike"]')
        sleep(0.5)
        descricao.click()
        descricao.send_keys('Tipo dependente automáticoTipo dependente alterada')
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]').click()
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/a[2]').click()
        sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
        sleep(5)

        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
        b_text = b_element.text
        msg_confirmacao = b_text[0:25]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'Excluído com Sucesso!':
          print("### Tela cadastro de escolaridade ok.")
        else:
          print(">>>>>>>>>>>>>> Erro na tela! Verificar.")
          erro = erro+1

    finally:
        print('>> Encerrando função cadastro_e_alteracao_de_tipo_dependente.')


def configuracoes_mva_antecipacoes():
    try:
        print('########## Configuração MVA Antecipação (%) ##########')
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_mva_antecipacoes")


        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

        # Clique no botão para abrir a lista de produtos
        produtos_button = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/button')
        produtos_button.click()

        # Espera até que a lista de produtos seja clicável
        produtos_list = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/ul'))
        )

        # Clique nas opções desejadas na lista de produtos
        for i in range(3, 6):
            option_xpath = f'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/ul/li[{i}]/a/label/input'
            navegador.find_element(By.XPATH, option_xpath).click()

        # Clique novamente no botão para fechar a lista de produtos
        produtos_button.click()

        # Encontre o campo "autocompletar_produtos" e preencha-o
        nome_element = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produtos"]')
        nome_element.send_keys('7410')
        sleep(2)
        print('### Passei produto.')

        # Use pyautogui para pressionar teclas
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')

        # Encontre o campo "percentual_mva_antecipacao" e preencha-o
        nome_element = navegador.find_element(By.XPATH, '//*[@id="percentual_mva_antecipacao"]')
        nome_element.send_keys('100')
        print('### Passei % de MVA Antecipação.')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/input[2]').click()

        # Encontre o campo "percentual_mva_antecipacao" novamente e preencha-o com outro valor
        nome_element = navegador.find_element(By.XPATH, '//*[@id="percentual_mva_antecipacao"]')
        nome_element.send_keys('0')
        print('### Passei % de MVA Antecipação alterado.')
        sleep(5)
        # Clique no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/input[1]').click()
        sleep(5)
        # Clique no link para excluir o cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
        sleep(5)
        # Clique no botão "Excluir"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/a[2]').click()

        # Confirme a exclusão
        sleep(2)
        navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
        print('### Excluído cadastro')

    finally:
        # Feche o navegador
        #navegador.quit()
        print('>> Encerrando funcao_configuracoes_mva_antecipacoes.')


def configuracao_tipo_servico():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_servicos")
        print('### Abrindo Configuração por Tipo de Serviço')

        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()
        print('### Selecionando Tipo de Serviço')

        # Espera até que o campo de seleção de tipo de serviço esteja clicável
        tipo_servico_element = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo_servico"]'))
        )
        tipo_servico_element.click()

        # Use o pyautogui para pressionar as teclas de seta para baixo várias vezes
        for _ in range(5):
            pyautogui.hotkey('down')

        # Use o pyautogui para pressionar a tecla "tab" duas vezes
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')

        print('#### Selecionado Garantia Estendida - Zurich')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[2]').click()
        print('### Salvo cadastro')

        # Espera até que o botão "Excluir" esteja visível
        excluir_button = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/a[2]'))
        )
        excluir_button.click()

        # Espera até que o botão de confirmação esteja clicável
        confirm_button = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]'))
        )
        confirm_button.click()
        print('### Excluído cadastro')

    finally:
        # Feche o navegador
        print('>> Encerrando função configuracoes_tipos_servicos.')


def adicionar_especificacao_produto():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/especificacoes_produtos")
        print('### Abrindo especificação do produto')
        print('### Adicionar')

        # Clique no botão para abrir o formulário de cadastro
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        ).click()

        # Preencha a descrição da especificação
        descricao_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        descricao_element.send_keys('Especificação Automática')
        print('### Passei descrição especificação.')

        print('Texto Curto (até 255 caracteres)')
        # Selecione o tipo "Texto Curto"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        print('Texto Longo (sem limite de caracteres)')
        # Selecione o tipo "Texto Longo"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        print('Número inteiro')
        # Selecione o tipo "Número inteiro"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Defina o número de casas decimais (para o tipo "Número decimal")
        if "Número decimal" in navegador.page_source:
            casas_decimais_element = navegador.find_element(By.XPATH, '//*[@id="casas_decimais"]')
            casas_decimais_element.send_keys('2')
            print('### Passei 2 casas decimais')

        # Clique no botão "Salvar"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]'))
        ).click()
        sleep(2)
        print('Lista Pré-definida')
        # Selecione o tipo "Lista Pré-definida"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Preencha as opções da lista
        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
        opcao_element.send_keys('Primeira opção')
        print('### Passei primeira opção')

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/table/tfoot/tr/td/button').click()

        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_1"]')
        opcao_element.send_keys('Segunda opção')
        print('### Passei segunda opção')

        # Clique no botão "Salvar"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]'))
        ).click()

        print('Sim/Não')
        # Selecione o tipo "Sim/Não"
        sleep(2)
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        print('Lista Pré-definida (Multiselect)')
        # Selecione o tipo "Lista Pré-definida (Multiselect)"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tipo"]'))
        ).click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        # Preencha as opções da lista
        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
        opcao_element.send_keys('Primeira opção')
        print('### Passei primeira opção')

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/table/tfoot/tr/td/button').click()

        opcao_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_1"]')
        opcao_element.send_keys('Segunda opção')
        print('### Passei segunda opção')

        
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]'))
        ).click()
        sleep(10)
        
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[2]'))
        ).click()
        sleep(2)

        
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]'))
        ).click()

        print('Realizado exclusão de especificação do produto')

    finally:
        # Feche o navegador
        # navegador.quit()
        print('>> Encerrando função especificacoes_produtos')

def configuracoes_tipos_montagens_produtos():

     try:
         print('########## TELA CONFIGURAÇÃO DE TIPO DE MONTAGEM POR PRODUTO ##########')
         navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_montagens_produtos")


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
         sleep(6)
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
         inf_campo = navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/input[1]')
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
         sleep(2)
         navegador.find_element(By.XPATH,'/html/body/div[8]/div/div/div[2]/button[2]').click()
         print('Realizado exclusão')
         sleep(3)

     finally:
         #navegador.quit()
         print('>> Encerrando função configuracoes_tipos_montagens_produtos')

def cadastrar_pessoa():
    sleep(5)
    print('########## TELA PESSOA ##########')
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pessoas/new")


    print('### Abrindo Gerador de CPF. ')
    url = 'https://www.4devs.com.br/gerador_de_cpf'
    print('#### Aguardando ...')

    navegador.execute_script("window.open('');")  # Abre uma nova janela do navegador
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[1])
    navegador.get(url)

    print('### Novo navegador aberto.\n#### Gerador de CPF\n##### 3 segundos para prosseguir')
    sleep(5)

    navegador.find_element(By.ID, 'bt_gerar_cpf').click()
    sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="cookiescript_accept"]').click()
    sleep(3)
    navegador.find_element(By.ID, 'texto_cpf').click()
    sleep(3)
    navegador.find_element(By.CLASS_NAME, "clipboard-copy").click()
    print('### CPF copiado.')
    CPFcopiado = clipboard.paste()
    sleep(3)
    navegador.close()
    navegador.switch_to.window(janelas[0])
    print('### Gerador de CPF encerrado.')
    sleep(5)
    nome_element = navegador.find_element(By.NAME, 'pessoa[nome]')
    nome_element.send_keys('Nome automatizado')
    print('### Passei nome.')

    nome_element = navegador.find_element(By.NAME, 'pessoa[apelido]')
    nome_element.send_keys('Apelido automatizado')
    print('### Passei apelido.')

    sleep(3)
    navegador.find_element(By.NAME, 'pessoa[cpf_cnpj]').click()
    pyautogui.hotkey('ctrl', 'v')
    sleep(3)
    print('### CPF inserido: ', CPFcopiado)

    nome_element = navegador.find_element(By.NAME, 'pessoa[data_nascimento_fundacao]')
    nome_element.send_keys('19/02/1990')
    print('### Passei data de nascimento.')

    #navegador.find_element(By.NAME, 'pessoa[identidade]')
    #sleep(2)
    #elemento = navegador.find_element(By.XPATH, '//*[@id="identidade"]')
    #sleep(3)
    #elemento.click()
    sleep(4)
    print("Passei aqui")
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[18]/ul/li[2]/a').click()
    sleep(2)    
    navegador.find_element(By.XPATH, '//*[@id="tipo_endereco_id_0"]').click()
    nome_element = navegador.find_element(By.XPATH, '//*[@id="tipo_endereco_id_0"]')
    nome_element.send_keys('R')
    print('#    ## Passei tipo de endereço.')
    nome_element = navegador.find_element(By.ID, 'autocompletar_cep_id_0')
    nome_element.send_keys('89805-545')
    print('### Passei CEP.')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')

    nome_element = navegador.find_element(By.ID, 'numero_0')
    nome_element.send_keys('322')
    print('### Passei número de endereço.')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')

    elemento = navegador.find_element(By.NAME, 'commit')
    sleep(2)
    elemento.click()

    hora_fim = datetime.datetime.now()
    print('Fim de execução: ', hora_fim)
    tempo_total = (hora_fim - hora_inicio)
    sleep(2)

    print('###### Pessoa física cadastrada com sucesso\n##### CPF cadastrado: ', CPFcopiado, 'Tempo de execução: ', tempo_total)
    print('Encerrado função cadastro_pessoa')


# def cadastrar_venda(numero_cliente, numero_produto):
#     try:
#         global nr_lcto
#         print('#######  ### TELA PEDIDO DE VENDA ##########')
#         navegador.get("h    ttps://felipe.testes.smart.sgisistemas.com.br/vendas")
#         10000
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
#         sleep(3)

#         # Preencher o campo "Forma de Pagamento"
#         nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
#         nome_element.send_keys('V')
#         sleep(3)
#         pyautogui.hotkey('ENTER')
#         print('### Passei forma de pagamento carnê')

#         # Preencher o campo "Quantidade de Parcelas"
#         sleep(2)
#         nome_element = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
#         sleep(2)
#         nome_element.send_keys('0')
#         sleep(2)
#         print('### Passei quantidade de parcelas.')

#         # Clicar no botão "Salvar"
#         navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
#         #sleep(10)
#         print("Aguarda 20 segundos para liberação")
#         for segundo_atual in range(20, 0, -1):
#             print(f"Tempo restante: {segundo_atual} segundos")
#             sleep(1)

#         # Preencher campos de liberação
#         sleep(2)
#         navegador.find_element(By.ID, 'login_liberacao_venda').click()
#         sleep(2)
#         nome_element = navegador.find_element(By.ID, 'login_liberacao_venda')
#         sleep(2)
#         nome_element.send_keys('projeto.robo')
#         pyautogui.hotkey('tab')
#         print('### Passei usuário de liberação')

#         navegador.find_element(By.ID, 'senha_liberacao_venda').click()
#         nome_element = navegador.find_element(By.ID, 'senha_liberacao_venda')
#         nome_element.send_keys('@rlequin@2020')
#         pyautogui.hotkey('tab')
#         print('### Passei senha de liberação')
#         pyautogui.hotkey('ENTER')
#         sleep(20)
#         print("Aguardei 20 segundos.")

#         # Clicar no botão "Salvar" novamente
#         navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button').click()
#         sleep(12)
#         navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
#         sleep(12)

#         # Obter número do lançamento
#         while True:
#             try:
#                 b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
#                 b_text = b_element.text
#                 nr_lcto = b_text[14:19]
#                 print('#### Número do lançamento: ', nr_lcto)
#                 break
#             except NoSuchElementException:
#                 print("Aguardando elemento...")
#                 sleep(1)

#         sleep(20)

#     except Exception as e:
#         print(f"Ocorreu um erro: {str(e)}")

#     finally:
#         print("Encerrado função funcao_cadastrar_venda")
# #         # navegador.quit()


def cadastrar_venda(numero_cliente, numero_produto):
    try:
        global nr_lcto
        hora_inicio = datetime.datetime.now()
        print("Tempo iniciado")
        print('########## TELA PEDIDO DE VENDA ##########')
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")

        #Preencher o campo "Cliente"
        nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
        nome_element.send_keys(numero_cliente)
        print('### Passei Cliente', numero_cliente)
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        #Preencher o campo "Produto"
        nome_element = navegador.find_element(By.ID, 'coluna_descricao_produto')
        sleep(5)
        nome_element.send_keys(numero_produto)
        print('### Passei produto.')
        sleep(5)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('ENTER')

        #Preencher o campo "Quantidade"
        sleep(1)
        nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[18]/div/div/div[2]/div[3]/div/table/tbody/tr[4]/td[3]/strong/input')
        sleep(1)
        nome_element.send_keys('1')
        print('### Passei quantidade.')
        pyautogui.hotkey('ENTER')
        sleep(5)

        #Preencher o campo "Forma de Pagamento"
        nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
        nome_element.send_keys('V')
        sleep(1)
        pyautogui.hotkey('ENTER')
        print('### Passei forma de pagamento carnê')

        #Preencher o campo "Quantidade de Parcelas"
        sleep(5)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
        sleep(5)
        nome_element.send_keys('0')
        sleep(5)
        print('### Passei quantidade de parcelas.')
        
        #Clicar no botão "Salvar"
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        print("Aguarda 20 segundos para liberação")
        for segundo_atual in range(20, 0, -1):
            print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)

        #Preencher campos de liberação
        navegador.find_element(By.ID, 'login_liberacao_venda').click()
        sleep(5)
        nome_element = navegador.find_element(By.ID, 'login_liberacao_venda')
        sleep(5)
        nome_element.send_keys('projeto.robo')
        pyautogui.hotkey('tab')
        print('### Passei usuário de liberação')

        navegador.find_element(By.ID, 'senha_liberacao_venda').click()
        nome_element = navegador.find_element(By.ID, 'senha_liberacao_venda')
        nome_element.send_keys('@rlequin@2020')
        pyautogui.hotkey('tab')
        print('### Passei senha de liberação')
        pyautogui.hotkey('ENTER')
        
        print("Aguarda 10 segundos - 2ªvez")
        for segundo_atual in range(10, 0, -1):
            print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)
    
        #Clicar no botão "Salvar" novamente
        print("Localizar botão salvão")
        navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button').click()
        print("Cliquei no salvar")
        print("Aguarda 10 segundos no Salvar")
        for segundo_atual in range(10, 0, -1):
            print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)
        print('Salvar')
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()

        for segundo_atual in range(15, 0, -1):
            print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)

        #Obter número do lançamento
        while True:
            try:
                b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
                b_text = b_element.text
                nr_lcto = b_text[14:19]
                print('#### Número do lançamento: ', nr_lcto)
                break
            except NoSuchElementException:
                print("Aguardando elemento...")
                sleep(1)
        hora_fim = datetime.datetime.now()
        print("Tempo Finalizado")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    finally:
        hora_fim = datetime.datetime.now()
        tempo_total = (hora_fim - hora_inicio)
        print("Tempo de execução", tempo_total)  
        print("Encerrado função funcao_cadastrar_venda")
        #navegador.quit()




def faturamento_de_venda():
  if nr_lcto == 0:
        print("Sem número de lançamento. Encerrando a função faturamento_de_venda.")
        return  

  try:
      print("########## TELA RECEBIMENTOS ##########")
      print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)
      navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recebimentos")
      print("Localizar campo Nº Lançamento")
      nome_element = navegador.find_element(By.XPATH,'//*[@id="numeros_lancamentos"]')
      sleep(3)
      nome_element.send_keys(nr_lcto)
      pyautogui.hotkey('tab')
      sleep(10)
      nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[4]/div/div/div[2]/div/div[4]/div/div/table/tbody/tr/td[1]/label').click()
      sleep(10)
      scroll_to_bottom_script = "window.scrollTo(0, document.body.scrollHeight);"
      # Executa o script para rolar a página
      navegador.execute_script(scroll_to_bottom_script)
      sleep(10)
      nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/button').click()
      print('Finalizado Lançamento')
      sleep(30)

      abas = navegador.window_handles

      for indice, aba in enumerate(abas):
            navegador.switch_to.window(aba)
            print(f"Índice da janela: {indice}")
            if indice > 0:
                navegador.close()
      sleep(20)
      abas = navegador.window_handles
      if len(abas) > 0:
          navegador.switch_to.window(abas[0])
          navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")

  finally:
      print("Encerrado função funcao_fatura_lcto")

def gestao_entrega():
  if nr_lcto == 0:
        print("Sem número de lançamento. Encerrando a função gestao_entrega.")
        return
  print('Recebido da função cadastrar_venda o lançamento: ', nr_lcto)
  try:
    sleep(5)
    abas = navegador.window_handles
    for aba in abas:
      navegador.switch_to.window(aba)
      if "pdf" in navegador.current_url.lower():
          navegador.close()
    print("########## TELA GESTÃO DE ENTREGA ##########")
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/reservas_produtos")
    print('Abrir + Filtros.')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/form/div/div[2]/div[2]/div/div[17]/a').click()
    print('Localiza campo Nº Lançamento. ')
    nome_element = navegador.find_element(By.XPATH, '//*[@id="numero_lancamento"]')
    nome_element.send_keys(nr_lcto)
    print('Passei número do lançamento: ', nr_lcto)
    print('Filtrar...')
    navegador.find_element(By.XPATH, '//*[@id="pesquisar-reservas"]').click()
    sleep(8)
    print('Marcar lançamento...')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div[4]/table/tbody/tr/td[1]/label').click()
    sleep(2)
    print('Gerar romaneio...')
    navegador.find_element(By.XPATH, '//*[@id="btn_gerar_romaneio"]').click()
    sleep(10)
    print('Confirmando geração... ')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/button[2]').click()
    sleep(30)
    print('Alterar situação...')
    sleep(30)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[2]/div[1]/button').click()
    sleep(2)
    print('Finalizar... ')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[2]/div[1]/ul/li[1]/a').click()
    sleep(2)
    print('Clicaer no salvar...')
    navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
    print('cliquei')
    sleep(10)
    campo_nr_romaneio = navegador.find_element(By.XPATH, '//*[@id="id"]')
    nro_romaneio = campo_nr_romaneio.get_attribute("value")
    sleep(2)
    print("Nº Romaneio: ", nro_romaneio)

  finally:
    print('Encerrando função gestao_entrega')


def gera_titulo():

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/titulos")
    print("########## TELA TÍTULO ##########")

    print("Adicionar novo título à receber")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

    print("Buscar tipos de título")

    sleep(2)

    tp_titulo = navegador.find_element(By.XPATH,'//*[@id="autocompletar_tipo_titulo_id"]')
    sleep(3)
    tp_titulo.send_keys('Receber')
    #pyautogui.hotkey('R','e','c','e','b','e','r')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    print("Selecionar título à receber")
    sleep(2)

    print("Preencher cliente")
    cod_cliente_fornecedor = navegador.find_element(By.XPATH, '//*[@id="autocompletar_pessoa_cliente_fornecedor_id"]')
    cod_cliente_fornecedor.send_keys('12547')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei cliente 12547")

    #gerador aleatorio para numero de titulos
    global numero_titulo_gerado
    numero_titulo_gerado = random.randint(1,5000000)
    sleep(2)

    numero_titulo = navegador.find_element(By.XPATH, '//*[@id="numero_titulo"]')
    sleep(2)
    numero_titulo.send_keys(str(numero_titulo_gerado))
    print("Numero do título: ", numero_titulo_gerado)

    print("Informar título Realizado")
    navegador.find_element(By.XPATH, '//*[@id="previsto_realizado"]').click()
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')

    print("Informar forma de pagamento")
    frm_pgto = navegador.find_element(By.XPATH, '//*[@id="autocompletar_forma_pagamento_id"]')
    frm_pgto.send_keys('Vazio - Carnê Loja TIR')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei forma de pagamento Vazio - Carnê Loja TIR")
    sleep(2)

    print("Informar Portador")
    portador = navegador.find_element(By.XPATH, '//*[@id="autocompletar_portador_titulo_id"]')
    portador.send_keys('Carteira')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei portardor Carteira")
    sleep(2)

    print("Informar Histórico de Receita e Despesa")
    historico_rec_desp = navegador.find_element(By.XPATH, '//*[@id="autocompletar_historico_receita_despesa_id"]')
    historico_rec_desp.send_keys('Venda Financiada')
    sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei Histório de Receita/Despesa Venda Financiada")
    sleep(2)

    print("Informar valor de parcelas")
    vlr_parcela = navegador.find_element(By.XPATH, '//*[@id="valor_cada_titulo"]')
    vlr_parcela.send_keys('10000')
    pyautogui.hotkey('tab')
    dt_primeiro_vcto = navegador.find_element(By.XPATH, '//*[@id="primeira_data_vencimento"]')
    dt_primeiro_vcto.send_keys('01092022')

    print("Informar quantidade de parcelas")
    qtd_parcelas = navegador.find_element(By.XPATH, '//*[@id="quantidade_parcelas"]')
    qtd_parcelas.clear()
    qtd_parcelas.send_keys('0')
    pyautogui.hotkey('tab')
    print("Passei 10 parcelas")

    print("Infomar observação do título")
    obs_titulo = navegador.find_element(By.XPATH, '//*[@id="observacao_geral"]')
    obs_titulo.send_keys('Inserção automática do título: ', numero_titulo_gerado)
    print("Inserido observação")


    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[1]').click()
    print("Salvo título ", numero_titulo_gerado)
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")

  finally:
    print("Encerrando função gera_titulo.")

def funcao_gera_sped_fiscal():

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped")
    tme = 30
    print("########## SPED FISCAL ##########")
    #elemento = WebDriverWait(navegador, tme).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="data_inicial"]')))
    nome_element = navegador.find_element(By.ID, 'data_inicial')
    nome_element.clear()
    nome_element.send_keys('01012024')
    print("Passei data inicial")
    sleep(2)
    nome_element = navegador.find_element(By.ID, 'data_final')
    nome_element.clear()
    nome_element.send_keys('31012024')
    print("Passei data final")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div/div[5]/span/div/div[1]/table/tbody/tr[1]/td[2]')
    actions = ActionChains(navegador)
    actions.double_click(nome_element).perform()
    print("Passei filial 1")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '//*[@id="btn-gerar-sped"]').click()
  finally:
    sleep(10)
    print("Encerrando funcao_gera_sped_fiscal")

def funcao_gera_sped_contribuicao():

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped_contribuicoes")
    tme = 30
    print("########## SPED CONTRIBUIÇÃO ##########")

    nome_element = navegador.find_element(By.ID, 'data_inicial')
    nome_element.clear()
    nome_element.send_keys('01012024')
    print("Passei data inicial")
    sleep(2)
    nome_element = navegador.find_element(By.ID, 'data_final')
    nome_element.clear()
    nome_element.send_keys('31012024')
    print("Passei data final")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
    actions = ActionChains(navegador)
    actions.double_click(nome_element).perform()
    print("Passei filial 1")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
  finally:
    sleep(10)
    print("Encerrando funcao_gera_sped_contribuicao")


def funcao_gera_cobranca():
    print("########## CONTROLE DE COBRANÇAS #########")
    print("Recebido da funcao_gera_titulo: ", numero_titulo_gerado)
    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cobrancas")
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a[1]').click()
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="data_vencimento_inicial"]')
        nome_element.clear()
        nome_element.send_keys('01092022')
        print("Passei data inicial")
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="data_vencimento_final"]')
        nome_element.clear()
        nome_element.send_keys('31122500')
        print("Passei data final")
        sleep(2)
        print("Pesquisar titulos")
        nome_element = navegador.find_element(By.XPATH, '//*[@id="numero_titulo"]')
        nome_element.send_keys(numero_titulo_gerado)
        navegador.find_element(By.XPATH, '//*[@id="pesquisa_titulos_cobrancas"]').click()
        sleep(3)
        print("Marcando títulos para cobrança")
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div[4]/div[2]/div[2]/table/thead/tr/th[1]/label').click()
        sleep(2)
        print("Gerar cobrança")
        navegador.find_element(By.XPATH, '//*[@id="gerar_cobrancas"]').click()
        sleep(3)
        print("Confirmando modal responsáveis cobrança")
        navegador.find_element(By.XPATH, '//*[@id="botao_gerar_modal"]').click()
        sleep(2)

    finally:
      print("Encerrando funcao_gera_cobranca")


def analise_credito():
  if nr_lcto == 0:
        print("Sem número de lançamento. Encerrando a função analise_credito.")
        return
  #nr_lcto = 93986
  print("Recebido da função cadastrar_venda o lançamento: ", nr_lcto)

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/analises_creditos")
    print("########## ANÁLISE DE CRÉDITO ##########")
    print("Localizar campo Nº Lançamento")
    nome_element = navegador.find_element(By.XPATH, '//*[@id="documentos.numero_lancamento"]')
    nome_element.send_keys(nr_lcto)
    print("Pesquisar lançamento para análise")
    sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[18]/div/button[1]').click()
    sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
    sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="btn_analise_credito"]').click()
    sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button[2]').click()
    sleep(5)
    print("Aba Financeiro")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[2]/a/strong').click()
    sleep(3)
    print("Aba Vendas")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[3]/a/strong').click()
    sleep(3)
    print("Aba Solicitações")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[4]/a/strong').click()
    sleep(3)
    print("Aba Observações")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[5]/a/strong').click()
    sleep(3)
    print("Histórico de observações")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div[5]/div[1]/div/div/div[1]/h4/a/strong').click()
    sleep(3)
    print("Aba Comprometimento Futuro")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[6]/a/strong').click()
    sleep(2)
    print("Aba Cobranças")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[7]/a/strong').click()
    sleep(2)
    print("Aba Histórico SPC")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[8]/a/strong').click()
    sleep(2)
    print("Aba Avalista")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[9]/a/strong').click()
    sleep(2)
    print("Aba Devoluções")
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[10]/a/strong').click()
    print("Finalizando Análise de Credito Autorizada")
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="btn_analise_credito"]').click()
    sleep(2)
    navegador.find_element(By.ID, 'btn_finalizar_analise').click()
  finally:
    print("Encerrando função analise_credito")



def devolucao_venda():
    if nr_lcto == 0:
        print("Sem número de lançamento. Encerrando a função devolucao_venda.")
        return

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



def lancamento_entrada():
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entrada")
    print("######### LANÇAMENTO DE ENTRADA ##########")
    print("Acessei tela Entrada")

    global numero_lancamento_entrada
    numero_lancamento_entrada = random.randint(1,5000000)
    sleep(2)

    numero_lancamento = navegador.find_element(By.XPATH, '//*[@id="numero_documento"]')
    sleep(2)
    numero_lancamento.send_keys(str(numero_lancamento_entrada))
    print("Numero do Documento: ", numero_lancamento_entrada)

    serie = navegador.find_element(By.XPATH, '//*[@id="serie_documento"]')
    serie.send_keys('1')
    print("Serie 1")

    fornecedor = navegador.find_element(By.XPATH, '//*[@id="autocompletar_pessoa_cliente_fornecedor_id"]')
    fornecedor.send_keys('FORNECEDOR DE TESTE')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    sleep(3)
    print("Informei Fornecedor de Teste(12551)")
    sleep(2)

    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[1]/h4').click
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[1]/h4').click
    #print("Abri/Fecha")

    nome_element = navegador.find_element(By.XPATH, '//*[@id="coluna_descricao_produto"]')
    nome_element.click()
    #print("fiz o click")
    nome_element = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produto_id_0"]')
    sleep(2)    
    nome_element.send_keys('7410')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    sleep(3)
    print("Passei Produto de Teste(7410)")
    
    qtde_nota = navegador.find_element(By.XPATH, '//*[@id="coluna_quantidade_nota"]')
    qtde_nota.send_keys('10')
    print("Informei 10 unidades do item.")
    sleep(2)
    pyautogui.hotkey('tab')
    sleep(2)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    
    sleep(2)
    pyautogui.write('10')
    pyautogui.hotkey('tab')
    print("Informei 10 unidades de lançamento.")
    sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="concluir_quantidade_por_local"]').click()
    sleep(3)
    cst_icms = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[2]/div/div[2]/table/tbody/tr/td[12]')
    sleep(2)
    cst_icms.click()
    sleep(2)
    inf_cst = navegador.find_element(By.XPATH, '//*[@id="autocompletar_cst_icms_id_0"]')
    sleep(5)
    inf_cst.send_keys('41')
    print("Cliquei na coluna CST ICMS")
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    print("Informei CST 41.")

    sleep(1)

    vlr_unit = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[18]/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div[1]')
    sleep(5)
    vlr_unit.click()
    sleep(5)
    pyautogui.hotkey('backspace')
    print("Apaguei valor unitário.")
    sleep(5)
    pyautogui.write('15000000')
    #vlr_unit.send_keys('15000000')
    sleep(5)
    pyautogui.hotkey('tab')
    sleep(5)
    print("Informei novo valor unitário.")
    sleep(5)

    forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[22]/div/div[2]/div/div[1]/div/div[1]/div/div/div/button/span[1]')
    forma_pgto.click()
    sleep(5)
    busca_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[22]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/input')
    sleep(5)
    busca_forma_pgto.send_keys('BOLETO')
    sleep(5)
    pyautogui.hotkey('Enter')
    sleep(5)
    print("Informei forma de pagamento BOLETO")

    qtde_parcelas = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
    sleep(5)
    qtde_parcelas.click()
    sleep(5)
    pyautogui.hotkey('backspace')
    sleep(5)
    qtde_parcelas.send_keys('3')
    print("Informei 3 parcelas")
    sleep(5)

    navegador.find_element(By.XPATH, '//*[@id="emitir_documento"]').click()
    sleep(10)
    navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button[2]').click()
    print("Finalizado lançamento.")
    sleep(20)

    abas = navegador.window_handles

    for indice, aba in enumerate(abas):
        navegador.switch_to.window(aba)
        print(f"Índice da janela: {indice}")
        if indice > 0:
            navegador.close()
    sleep(15)
    abas = navegador.window_handles
    if len(abas) > 0:
        navegador.switch_to.window(abas[0])
    #    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")

    sleep(15)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/form/div/div[2]/div[2]/table/tbody/tr/td[1]/label').click()
    sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="tipo_custo"]').click()
    sleep(1)
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('tab')
    sleep(1)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/form/div/div[3]/button').click()
    sleep(3)
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")

def pedido_compra():
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_compras")
    print('########## TELA PEDIDO DE COMPRA ##########')
    print('Tela: ', tela)
    sleep(2)
    print("Acessei tela de Pedido de Compra")

    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()
    sleep(5)
    print("Cliquei adicionar.")

    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div[4]/div/div/select').click()
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Informei Tipo de Pedido de Compra.")

    fornecedor = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div[5]/div/div/div/div/span[1]/input[2]')
    fornecedor.send_keys('FORNECEDOR DE TESTE')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Informei Fornecedor de Teste(12551).")
    sleep(2)

    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/button').click()
    sleep(2)

    produto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/span[1]/input[2]')
    produto.send_keys('7410')
    sleep(3)
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    sleep(5)
    print("Informei Produto de Teste(7410).")
    qtde_produto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div[2]/div/div[3]/div/div/input')
    sleep(5)
    qtde_produto.send_keys('100')
    sleep(3)
    pyautogui.hotkey('tab')
    print("Informei a quantidade de 100 itens.")
    pyautogui.write('10000')
    print("Informei valor unitário.")
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div/div[3]/div/button[1]/span[2]').click()
    sleep(2)

    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/div[2]/div[1]/div/div[1]/div/div/select').click()
    cont = 0
    for i in range (1,22):
        pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    print("Passei forma de pagamento BOLETO.")
    forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[8]/div/div[2]/div[1]/div/div[3]/div[1]/div/div/input')
    forma_pgto.click()
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('3')
    pyautogui.hotkey('tab')
    print("Informa a quantidade de parcelas(3).")

    observacao_pedido = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[9]/div/div[2]/div[3]/div/div/textarea')
    observacao_pedido.send_keys("Observação com automação")
    print("Informei observação de teste.")
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
    sleep(15)


    b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
    b_text = b_element.text
    msg_confirmacao = b_text[0:99]
    print('#### Mensagem confirmação: ', msg_confirmacao)
    sleep(8)

    if msg_confirmacao == 'Adicionado com Sucesso!':
        print("### Pedido gravado com sucesso.")
    else:
        print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


# from selenium.common.exceptions import NoSuchElementException
# def venda_com_encomenda(numero_cliente, numero_produto):

#     try:
#         global nr_lcto
#         nr_lcto = 0
#         print('########## TELA PEDIDO DE VENDA (Venda Com Encomenda) ##########')
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
#         sleep(5)
#         nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
#         sleep(5)
#         nome_element.send_keys('1')
#         print('### Passei quantidade.')
#         pyautogui.hotkey('ENTER')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('tab')
        
#         # Marcar encomenda
#         print("Buscar flag entrega")
#         sleep(5)
#         nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[16]/div/div[2]/div/div/div[1]/div[1]/table/tbody/tr/td[13]/label')
#         sleep(5)
#         print("Encontrado campo marcação de entrega")
#         nome_element.click()
#         print("Marquei a encomenda do produto.")



#         # Preencher o campo "Forma de Pagamento"
#         nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
#         nome_element.send_keys('Dinheiro')
#         sleep(5)
#         pyautogui.hotkey('ENTER')
#         print('### Passei forma de pagamento Dinheiro')

    
#         # Clicar no botão "Salvar"
#         navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
#         #sleep(10)
#         print("Aguarda 20 segundos para liberação")
#         for segundo_atual in range(20, 0, -1):
#             print(f"Tempo restante: {segundo_atual} segundos")
#             sleep(1)

#         sleep(20)
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
        nome_element = navegador.find_element(By.ID, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[18]/div/div/div[2]/div[3]/div/table/tbody/tr[4]/td[3]/strong/input')
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
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
        b_text = b_element.text
        nr_lcto = b_text[14:19]
        print('#### Número do lançamento: ', nr_lcto)
        sleep(12)



               
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    finally:
        print("Encerrado função funcao_cadastrar_venda")
        #navegador.quit()


def encomenda_de_produto():
    if nr_lcto == 0:
        print("Sem número de lançamento. Encerrando a função encomenda_de_produtos.")
        return 
    
    try:
        print("########## TELA ENCOMENDA DE PRODUTOS ##########")
        print("Recebido da função venda com encomenda o lançamento: ", nr_lcto)
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/encomendas_produtos")
        sleep(2)

        nr_lancamento = navegador.find_element(By.XPATH, '//*[@id="documentos.numero_lancamento"]')
        sleep(5)
        nr_lancamento.send_keys(nr_lcto)
        sleep(5)
        pyautogui.hotkey('Enter')
        sleep(5)
        checkbox = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[3]/div[1]/table/tbody/tr/td[1]/div/label')
        sleep(5)
        checkbox.click()
        sleep(5)

        gerar_pedido_compra = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[4]/button')
        sleep(5)
        gerar_pedido_compra.click()

        sleep(20)

        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
        b_text = b_element.text
        msg_confirmacao = b_text[0:99]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(3)

        if msg_confirmacao == 'Gerado com sucesso!':
            print("### Encomenda gravada com sucesso.")
        else:
            print(">>>>>>>>>>>>>> Erro na tela! Verificar.")
            
    finally:
       print("Encerrado função venda_com_encomenda")
       navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")

def pdv_oline():

    try:
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pdv_online")
        print('### Acesso PDV Online')

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button/span[3]').click()
        sleep(0.5)
        for i in range(10):
            sleep(0.5)
            pyautogui.write('7410')
            pyautogui.hotkey('Enter')
            print("Incluso ", i, "vezes.")
        sleep(0.5)
        
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div[1]/div[1]/div[1]/div[4]/button').click()
        sleep(1)
        
        navegador.find_element(By.XPATH, '//*[@id="vendedor_id"]').click()

        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('space')
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(2)
        finalizar = navegador.find_element(By.XPATH, '//*[@id="btn_finaliza"]')
        sleep(2)
        finalizar.click()
        sleep(20)


        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div')
        b_text = b_element.text
        nr_lcto = b_text[0:99]
        print('#### Número do lançamento: ', nr_lcto)

    finally:
        print('>> Encerrando função PDV Online.')
        # Feche o navegador
        #navegador.quit()

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
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
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
        sleep(5)
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
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
       sleep(5)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
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
       sleep(5)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
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

def cadastro_de_produto():
    try:
        data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
        descricao = 'Cadastro automático de produto.'
        descProduto = f"{descricao} - {data_atual}"

        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos")

        btnAdicionar = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
        btnAdicionar.click()

        descricaoProduto = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        descricaoProduto.send_keys(descProduto)

        subgrupo = navegador.find_element(By.XPATH, '//*[@id="autocompletar_subgrupo_produto_id"]')
        subgrupo.send_keys(data_atual)
        sleep(2)

        pyautogui.press('down')
        pyautogui.press('tab')

        marca = navegador.find_element(By.XPATH, '//*[@id="autocompletar_marca_produto_id"]')
        marca.send_keys(data_atual)
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        undMedida = navegador.find_element(By.XPATH, '//*[@id="autocompletar_unidade_medida_id"]')
        undMedida.send_keys('UN')
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        tributacao = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/ul/li[3]/a')
        tributacao.click()
        sleep(2)

        origem = navegador.find_element(By.XPATH, '//*[@id="autocompletar_origem_produto_id"]')
        origem.send_keys('Nacional, exceto as indicadas nos códigos 3 a 5.')
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        ncm = navegador.find_element(By.XPATH, '//*[@id="autocompletar_ncm_id"]')
        ncm.send_keys('9403.91.00')
        sleep(2)
        pyautogui.press('down')
        pyautogui.press('tab')

        sleep(2)

        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/input[1]').click()

        sleep(5)
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
        b_text = b_element.text
        msg_confirmacao = b_text[0:25]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'Adicionado com Sucesso!':
          print("### Cadastrado Produto com sucesso: ")
        else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")    

    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro do produto: {str(e)}")

    finally:
         print("Encerrado função cadastro de produto")

def conta_caixa_por_usuario():
    try:
        navegador.get('https://felipe.testes.smart.sgisistemas.com.br/contas_caixas_usuarios')
        print("######### CONTA CAIXA POR USUÁRIO ##########")
        sleep(2)
        usuario = navegador.find_element(By.XPATH, '//*[@id="autocompletar_usuario_id"]')
        usuario.send_keys('robo.robo')
        print("Selecionei usuário")
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        print("Confirmei usuário")
        sleep(3)
        contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        contas_caixas.click()
        print("Abri multiselect de Contas Caixa")
        selecao_todos = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/ul/li[2]/a/label/input')
        selecao_todos.click()
        print("Marquei todas")
        contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        contas_caixas.click()
        print("Fechei multiselect")

        contas_caixas_permitidas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/button/span')
        contas_caixas_permitidas.click()
        print("Abri multiselct de Contas Caixa permitidas")
        selecao_todos_permitidos = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/ul/li[2]/a/label/input')
        selecao_todos_permitidos.click()
        print("Marquei todas das permitidas")

        contas_caixas_permitidas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/button/span')
        contas_caixas_permitidas.click()
        print("Fechei multiselect")

        btn_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/input')
        btn_salvar.click()
        print("Salvar")

        WebDriverWait(navegador, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')))
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')   
        b_text = b_element.text
        msg_confirmacao = b_text[0:30]
        print('#### Mensagem confirmação: ', msg_confirmacao)

        if msg_confirmacao == 'Salvo com sucesso.':
            print("### Conta caixa liberada com sucesso")
        else:
            print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


        # print("######### SEGUNDA EXECUÇÃO ##########")
        # sleep(2)
        # usuario = navegador.find_element(By.XPATH, '//*[@id="autocompletar_usuario_id"]')
        # usuario.send_keys('robo.robo')
        # print("Selecionei usuário")
        # sleep(5)
        # pyautogui.hotkey('down')
        # pyautogui.hotkey('tab')
        # print("Confirmei usuário")
        # sleep(5)
        # contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        # contas_caixas.click()
        # print("Abri multiselect de Contas Caixa")
        # sleep(8)
        # selecao_unico = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/ul/li[4]/a/label')
        # selecao_unico.click()
        # sleep(2)
        # contas_caixas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/button')
        # contas_caixas.click()
        # sleep(2)

        # contas_caixas_permitidas = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/button/span')
        # contas_caixas_permitidas.click()
        # print("Abri multiselct de Contas Caixa permitidas")

        # selecao_unico_permitido = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[4]/div/div/ul/li[4]/a/label')
        # selecao_unico_permitido.click()

        # btn_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/input')
        # btn_salvar.click()
        # print("Salvar")    

        # WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')))
        # b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')   
        # b_text = b_element.text
        # msg_confirmacao = b_text[0:30]
        # print('#### Mensagem confirmação: ', msg_confirmacao)

        # if msg_confirmacao == 'Salvo com sucesso.':
        #     print("### Conta Caixa liberada com sucesso")
        # else:
        #     print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

        

    finally:
        print("Encerrando função liberação Conta Caixa por Usuário")




def conta_corrente():

    try:
        navegador.get('https://felipe.testes.smart.sgisistemas.com.br/contas_correntes')
        print("######### CADASTRO DE CONTA CORRENTE ##########")
        

        btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
        btn_adicionar.click()

        banco = WebDriverWait(navegador,10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="autocompletar_banco"]'))
        )
        banco.send_keys('Banco do Brasil S/A')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        agencia = navegador.find_element(By.XPATH, '//*[@id="autocompletar_agencia_id"]')
        agencia.send_keys('3004')
        sleep(3)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')

        global numero_conta_cadastro
        numero_conta_cadastro = random.randint(1,5000000)
        sleep(2)
        numero_conta = navegador.find_element(By.XPATH, '//*[@id="numero_conta"]')
        numero_conta.send_keys(numero_conta_cadastro)

        digito_conta = navegador.find_element(By.XPATH, '//*[@id="digito_conta"]')
        digito_conta.send_keys('0')

        compe = navegador.find_element(By.XPATH, '//*[@id="compe"]')
        compe.send_keys('001')

        btn_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]')
        btn_salvar.click()

    finally:
        print("Encerrando cadastro de conta corrente")

def simulacao_venda():
    try:
        print("######### TELA SIMULAÇÃO DE VENDAS #########")
        navegador.get('https://felipe.testes.smart.sgisistemas.com.br/simulacoes_vendas')
        produto = navegador.find_element(By.XPATH, '//*[@id="coluna_descricao_produto"]')
        produto.click()

        # Procurar pelo elemento de auto completar produto
        from selenium.common.exceptions import NoSuchElementException
        try:
            auto_completar_produto = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produto_id_0"]')
        except NoSuchElementException:
            print("O elemento não foi encontrado.")
        
        # Enviar chaves para o campo de auto completar produto
        auto_completar_produto.send_keys('7410')
        sleep(2)
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(2)

        # Clicar no botão de forma de pagamento
        forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[7]/div/div[2]/div/div[1]/div/div[1]/div/div/div/button/span[1]')
        forma_pgto.click()
        
        # Enviar chaves para o campo de opção de forma de pagamento
        opcao_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/input')
        opcao_forma_pgto.send_keys('Vazio - Carnê Loja TIR')
        
        # Clicar na opção de forma de pagamento
        opcao_forma_pgto = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[6]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/ul/li[30]/a/span[1]')
        opcao_forma_pgto.click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('tab')
        sleep(6)

        parcelas = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
        parcelas.send_keys('0')
        pyautogui.hotkey('tab')
        sleep(6)

        btn_gerar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[10]/input')
        btn_gerar.click()
        sleep(25)
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
        b_text = b_element.text
        msg_confirmacao = b_text[41:48]
        print('#### Mensagem confirmação: ', msg_confirmacao)
        sleep(8)

        if msg_confirmacao == 'sucesso':
            print("### Pedido gravado com sucesso.")
        else:
            print(">>>>>>>>>>>>>> Erro na tela! Verificar.")



    finally:
        print("Encerrando tela simulação de venda.")

def cadastro_grupo_receita_despesa():
   
    try:
       data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
       desc_grupo_hist_rec_desp = 'Grupo Historico Receita/Despesa Automatizado'
       desc_grupo_hist_rec_desp_data = f"{desc_grupo_hist_rec_desp} - {data_atual}"
       
       navegador.get('https://felipe.testes.smart.sgisistemas.com.br/grupos_historicos_rd')
       print("######### TELA GRUPOS DE HISTÓRICOS DE RECEITAS E DESPESAS #########")

       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)
       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_grupo_hist_rec_desp_data)
       sleep(0.5)
       navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
       sleep(3)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Grupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

       print('### INICIANDO EXCLUSÃO ###')

       filtro = navegador.find_element(By.XPATH, '//*[@id="descricao_ilike"]')
       filtro.send_keys(desc_grupo_hist_rec_desp_data)

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]/span').click()
       sleep(2)
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr/td/a').click()
       sleep(2)
       btn_exclusao = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/a[2]')
       btn_exclusao.click()
       sleep(2)
       btn_confirma = navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]')
       btn_confirma.click()

       sleep(3)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:25]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Excluído com Sucesso!':
         print("### Tela cadastro Grupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


       print('### INICIANDO SEGUNDA INCLUSÃO ###')


       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)
       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_grupo_hist_rec_desp_data)
       sleep(0.5)
       navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
       sleep(3)
       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Grupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")




    finally:
       print("Encerrado função cadastro_grupo_receita_despesa.")

def cadastro_subgrupo_historico_receita_despesa():
    try:
       data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
       desc_subgrupo_hist_rec_desp = 'SUBGrupo Historico Receita/Despesa Automatizado'
       desc_subgrupo_hist_rec_desp_data = f"{desc_subgrupo_hist_rec_desp} - {data_atual}"
       
       navegador.get('https://felipe.testes.smart.sgisistemas.com.br/subgrupos_historicos_rd')
       print("######### TELA SUBGRUPOS DE HISTÓRICOS DE RECEITAS E DESPESAS #########")

       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)

       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_subgrupo_hist_rec_desp_data)
       sleep(2)
       
       grupo_hist_rec_desp = navegador.find_element(By.XPATH, '//*[@id="autocompletar_grupo_historico_rd_id"]')
       grupo_hist_rec_desp.click()
       sleep(2)
       grupo_hist_rec_desp.send_keys(data_atual)
       sleep(2)
       pyautogui.hotkey('down')
       pyautogui.hotkey('tab')
       sleep(0.5)

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[1]').click()

       sleep(3)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(3)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro SUBGrupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

       
       print("### INICIANDO EXCLUSÃO ###")

       filtro = navegador.find_element(By.XPATH, '//*[@id="descricao_ilike"]')
       filtro.send_keys(desc_subgrupo_hist_rec_desp_data)

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]').click()

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
       sleep(2)
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[2]').click()
       sleep(2)
       navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
       sleep(2)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:25]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Excluído com Sucesso!':
         print("### Tela cadastro Grupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


       print("### INICIANDO SEGUNDA INCLUSÃO ###")
       
       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)

       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_subgrupo_hist_rec_desp_data)
       sleep(2)
       
       grupo_hist_rec_desp = navegador.find_element(By.XPATH, '//*[@id="autocompletar_grupo_historico_rd_id"]')
       grupo_hist_rec_desp.click()
       sleep(2)
       grupo_hist_rec_desp.send_keys(data_atual)
       sleep(2)
       pyautogui.hotkey('down')
       pyautogui.hotkey('tab')
       sleep(0.5)

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[1]').click()

       sleep(3)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(3)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro SUBGrupos de Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

    finally:
        print("Encerrando execução função cadastro_subgrupo_historico_receita_despesa ")


def cadastro_historico_receita_despesa():
    try:
       data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
       desc_hist_rec_desp = 'Historico Receita/Despesa Automatizado'
       desc_hist_rec_desp_data = f"{desc_hist_rec_desp} - {data_atual}"

       navegador.get('https://felipe.testes.smart.sgisistemas.com.br/historicos_receitas_despesas')
       print("######### TELA  HISTÓRICOS DE RECEITAS E DESPESAS #########")

       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)

       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_hist_rec_desp_data)
       sleep(2)

       subgrupo = navegador.find_element(By.XPATH, '//*[@id="autocompletar_subgrupo_historico_rd_id"]')
       subgrupo.send_keys(data_atual)
       sleep(2)
       pyautogui.hotkey('down')
       pyautogui.hotkey('tab')
       sleep(5)
       bt_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[15]/div/input[1]')
       sleep(2)
       bt_salvar.click()
       sleep(10)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(3)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")


       print("### INICIANDO EXCLUSÃO ###")
       
       filtro = navegador.find_element(By.XPATH, '//*[@id="descricao_ilike"]')
       filtro.send_keys(desc_hist_rec_desp_data)

       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[4]/div/button[1]').click()
       sleep(2)
       #input("Enter")
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
       sleep(2)
       scroll_to_bottom_script = "window.scrollTo(0, document.body.scrollHeight);"
      # Executa o script para rolar a página
       navegador.execute_script(scroll_to_bottom_script)
       # input("Enter")
       navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[15]/div/a[2]').click()
       sleep(2)
       # input("Enter")
       navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
       sleep(2)
       # input("Enter")

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:25]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(8)

       if msg_confirmacao == 'Excluído com Sucesso!':
         print("### Tela Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

       print("### INICIANDO SEGUNDA INCLUSÃO ###")

       btn_adicionar = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a'))
        )
       btn_adicionar.click()
       sleep(5)

       descricao = WebDriverWait(navegador, 10).until(
          EC.visibility_of_element_located((By.XPATH, '//*[@id="descricao"]'))
       )
       descricao.send_keys(desc_hist_rec_desp_data)
       sleep(2)

       subgrupo = navegador.find_element(By.XPATH, '//*[@id="autocompletar_subgrupo_historico_rd_id"]')
       subgrupo.send_keys(data_atual)
       sleep(3)
       pyautogui.hotkey('down')
       pyautogui.hotkey('tab')
       sleep(5)
       scroll_to_bottom_script = "window.scrollTo(0, document.body.scrollHeight);"
      # Executa o script para rolar a página
       navegador.execute_script(scroll_to_bottom_script)
       bt_salvar = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[15]/div/input[1]')
       sleep(2)
       bt_salvar.click()
       sleep(5)

       b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div')
       b_text = b_element.text
       msg_confirmacao = b_text[0:32]
       print('#### Mensagem confirmação: ', msg_confirmacao)
       sleep(3)

       if msg_confirmacao == 'Adicionado com Sucesso!':
         print("### Tela cadastro Históricos de Receita e Despesas Ok.")
       else:
         print(">>>>>>>>>>>>>> Erro na tela! Verificar.")

    finally:
        print("Encerrando execução função cadastro_historico_receita_despesa.")



 



navegador = Firefox()
navegador.maximize_window()
navegador.get(smart)
hora_inicio = datetime.datetime.now()
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

print("Funções que serão executadas na seguinte ordem.")
print("cadastrar_venda") 
print("analise_credito")
print("faturamento_de_venda")
print("gestao_entrega")
print("cadastrar_pessoa")
print("cadastro_e_alteracao_de_escolaridade")
print("cadastro_e_alteracao_de_tipo_dependente")
print("configuracoes_mva_antecipacoes")
print("configuracao_tipo_servico")
print("adicionar_especificacao_produto")
print("configuracoes_tipos_montagens_produtos")
print("gera_titulo")
print("funcao_gera_sped_fiscal")
print("funcao_gera_sped_contribuicao")
print("funcao_gera_cobranca")
print("devolucao_venda")
print("pedido_compra")
print("lancamento_entrada")
print("venda_com_encomenda")
print("faturamento_de_venda")
print("encomenda_de_produto")
print("pdv_oline")
print("cadastro_departamento")
print("cadastro_grupo")
print("cadastro_subgrupo")
print("cadastro_marca")
print("cadastro_de_produto")
print("conta_caixa_por_usuario")
print("cadastro_conta_corrente")
print("simulacao_venda")
print("cadastro_grupo_receita_despesa")
print("cadastro_subgrupo_historico_receita_despesa")
print("cadastro_historico_receita_despesa")



sleep(2)

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/empresas/1/edit")
print('########## TELA CONFIGURAÇÃO DA EMPRESA ##########')
tela = tela + 1
print('Tela: ', tela)
sleep(2)

navegador.find_element(
    By.XPATH,
    '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[1]/input[1]'
).click()

print("Aguarda 10 segundos para validação da mensagem de confirmação")
for segundo_atual in range(30, 0, -1):
    print(f"Tempo restante: {segundo_atual} segundos")
    sleep(1)
print("Fim da espera")

# Espera a mensagem de sucesso aparecer
elemento_msg = WebDriverWait(navegador, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='texto-alerta']"))
) 

msg_confirmacao = elemento_msg.text.strip()
print("Passei e vou ler texto")
print("#### Mensagem confirmação:", msg_confirmacao)

if msg_confirmacao == "Atualizado com Sucesso!":
    print("### Tela configuração de empresa ok.")
else:
    print(">>>>>>>>>>>>>> Erro na tela! Verificar.")
    erro += 1


# # Chamada de funções
# simulacao_venda()
cadastrar_venda("12546", "7410")
analise_credito()
faturamento_de_venda()
gestao_entrega()
cadastro_departamento()
cadastro_grupo()
cadastro_subgrupo()
cadastro_marca()
cadastro_de_produto()
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
# lancamento_entrada()
#pdv_oline()    
conta_caixa_por_usuario()
conta_corrente()
cadastro_grupo_receita_despesa()
cadastro_subgrupo_historico_receita_despesa()
cadastro_historico_receita_despesa()
# venda_com_encomenda("12546", "7410")
# faturamento_de_venda()
# encomenda_de_produto()

print('#######################################################################')
print('#                LIBERADO USO MOUSE E TECLADO                         #')
print('#######################################################################')
sleep(3)


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos")
# print('########## TELA PRODUTOS ##########')
# tela = tela + 1
# error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#     result_teste = ">>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO"
# cont = cont +1


sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_inventarios")
print('### Acessei Relatório de Inventário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ncm]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_precos_produtos")
print('### Acessei Relatório de Preços de Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[status_produto]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_sef")
print('### Acessei SEF II')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"exportacao_sef[data_base]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/demonstracoes")
print('### Acessei Demonstração de Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entradas_manuais")
print('### Acessei Entrada Manual')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_fretes")
print('### Acessei Tabela de Frete')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_orcamentos")
print('### Acessei Relatório de Orçamentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[detalhamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_servicos")
print('### Acessei Log de Integração Serviços')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[lancamento_documento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atualizacoes_codigos_pessoas")
print('### Acessei Atualização de Código de Pessoas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"gerar_codigo_automaticamente")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_servicos")
print('### Acessei Definição de Serviço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"servicos.descricao_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atualizacoes_automaticas_precos")
print('### Acessei Atualizações Automáticas de Tabela de Preço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_variacoes_grades")
print('### Acessei Grupo Variações de Grade')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/variacoes_grades")
print('### Acessei Variações de Grade')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/designers_produtos")
print('### Acessei Designer do Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_encomendas_produtos")
print('### Acessei Configuração de Encomenda de Produtos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/mva")
print('### Acessei MVA')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cores_produtos")
print('### Acessei Cor')
tela = tela + 1
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
print('Tela: ', tela)
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/unidades_medidas")
print('### Acessei Unidade de Medida')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/origens_produtos")
print('### Acessei Origem do Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/marcas_produtos")
print('### Acessei Marca do Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subgrupos_produtos")
# print('### Acessei Subgrupo do Produto')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1

# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_produtos")
# print('### Acessei Grupo do Produto')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1

# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/departamentos_produtos")
# print('### Acessei Departamento do Produto')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/profissoes")
print('### Acessei Profissão')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/meios_contatos")
print('### Acessei Meio de Contato')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_referencias")
print('### Acessei Tipo de Referência')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/servicos")
print('### Acessei Serviço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/kits_produtos")
print('### Acessei Kit de Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/kits_produtos")
print('### Acessei Kit de Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_compras")
print('### Acessei Relatório de Análise de Compras')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/baixar_xmls_mdfe")
print('### Acessei Baixar XML de MDF-e')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_detalhamentos_custos")
print('### Acessei Relatório de Detalhamento de Custo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_liberacoes_pedidos_compras")
print('### Acessei Configuração de Liberação do Pedido de Compra')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"titulo_campo_tipos_pedidos_compras_ids")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_pedidos_compras")
print('### Acessei Relatório de Pedido de Compra')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inclusao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_cooperados")
print('### Acessei Relatório de Cooperado')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_entradas")
print('### Acessei Relatório de Documentos de Entrada')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/encomendas_produtos")
# print('### Acessei Encomenda de Produtos')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[encomendas_produtos.created_at_maior_igual]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controles_impressoes_etiquetas")
print('### Acessei Controle de Impressão de Etiquetas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracao_impressao_etiqueta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/impressoes_etiquetas")
print('### Acessei Impressão de Etiquetas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"impressao_etiqueta[configuracao_impressao_etiqueta_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_xml_nfe")
print('### Acessei Importação do XML da NF-e')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"filtro_nome_fornecedor")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/xml_sefaz")
print('### Acessei Baixar XML de Documentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cancelamento_documentos")
print('### Acessei Cancelamento de Documentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/devolucoes_documentos")
#print('### Acessei Devolução')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.ID,"autocompletar_numero_lancamento")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/documentos")
print('### Acessei Documentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[cliente_fornecedor.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/estoques_minimos_ecommerces")
print('### Acessei Estoque Mínimo do E-commerce')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_ecommerces")
print('### Acessei Log do E-commerce')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestoes_ecommerces")
print('### Acessei Gestão E-commerce')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pedidos_ecommerces.id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos_ecommerces")
print('### Acessei Produto E-commerce')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/distribuicoes_mercadorias")
print('### Acessei Distribuição de Mercadoria')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_filial_entrega_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_enderecamentos_estoques")
print('### Acessei Relatório de Endereçamento de Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[detalhamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_niveis_enderecamentos")
print('### Acessei Produto por Endereçamento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/enderecamentos")
print('### Acessei Níveis de Endereçamento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1




navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_estoques")
print('### Acessei Auditoria de Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_encomendas_produtos")
print('### Acessei Relatório de Encomendas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_encomenda_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestoes_montagens")
print('### Acessei Gestão de Montagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[previsao_montagem_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/romaneios_montagens")
print('### Acessei Romaneio de Montagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_locais_estocagens")
print('### Acessei Relatório Razão de Produto por Local de Estocagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/distribuicoes_estoques")
print('### Acessei Relatório de Distribuição de Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[exibir_estoque_detalhado]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_entregas_transportador")
print('### Acessei Relatório de Entregas por Transportador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_venda_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_ordens_servicos")
print('### Acessei Tipo de Assistência Técnica')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"descricao_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escopos_configuracoes_custos")
print('### Acessei Configurações de Custo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_movimentacoes_codigos_unicos")
print('### Acessei Relatório de Movimentações dos Códigos Únicos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/codigos_unicos")
print('### Acessei Código Único')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_codigos_unicos")
print('### Acessei Configuração de Código Único')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[definicao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_servicos_documentos")
print('### Acessei Assistência Técnica a partir do Documento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_servicos")
print('### Acessei Assistência Técnica')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entregas_montagens")
print('### Acessei Controle de Agendamento de Serviços')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_estoque_minimo_maximo")
print('### Acessei Relatório De Estoque Mínimo/Máximo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[agrupamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_produtos")
print('### Acessei Relatório Razão de Produtos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[ativo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_giros_estoques")
print('### Acessei Relatório de Giro Médio do Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[opcoes]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_posicao_estoque")
print('### Acessei Relatório de Posição do Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo_valor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_auditorias_estoques_produtos")
print('### Acessei Relatório de Auditoria do Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[filial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_transferencias_mercadorias")
print('### Acessei Relatório de Transferência de Mercadoria')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/reservas_produtos")
#print('### Acessei Gestão de Entrega')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.NAME,"filtros[descricao_produto]")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/romaneios_separacoes")
print('### Acessei Romaneio de Separação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_estoques_configuracoes")
print('### Acessei Configuração Auditoria de Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_operacao_documento_entrada_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_entradas_transferencias")
print('### Acessei Conferência de Entrada por Transferência')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filial_destino")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transferencias_mercadorias")
print('### Acessei Transferência de Mercadoria')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[documentos_saidas.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/parametros_transferencias_mercadorias")
print('### Acessei Parâmetro para Transferência de Mercadoria')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[filial_origem.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/requisicoes_mercadorias")
print('### Acessei Requisição de Mercadorias')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_filial_origem_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_locais_estocagens")
print('### Acessei Movimentação Local de Estocagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[locais_estocagens.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/locais_estocagens")
print('### Acessei Local de Estocagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fechamentos_estoques")
print('### Acessei Fechamento de Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[filiais.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/estoques_minimo_maximo")
print('### Acessei Estoque Mínimo/Máximo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_estoques")
print('### Acessei Consulta de Estoque')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simulacoes_guias_icms")
print('### Acessei Simulação de Guias de ICMS e ICMS ST')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"nao_considerar")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_nfe_inutilizadas")
print('### Acessei Relatório de Notas Inutilizadas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inutilizacao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contabilizacao")
print('### Acessei Relatório de Contabilização')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/guias_icms_st")
print('### Acessei Guia de Imposto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/nf_complementar")
print('### Acessei NF-e Complementar')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"nf_complementar[tipo_nfe]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_xml_nfe")
print('### Acessei Exporta XML NF-e e NFC-e')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"exporta_xml_nfe[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sintegra")
print('### Acessei SINTEGRA')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"sintegra[finalidade_arquivo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped")
#print('### Acessei SPED Fiscal')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.NAME,"sped[data_inicial]")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/inutilizacao_nfe")
print('### Acessei Inutilização NF-e')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_nfe_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simples_remessa")
print('### Acessei Simples Remessa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped_contribuicoes")
#print('### Acessei SPED Contribuições')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.NAME,"sped[data_inicial]")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_ecommerces")
print('### Acessei Configuração E-commerce')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracao_ecommerce[tipo_integracao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_ecommerces")
print('### Acessei Log de Integração do E-commerce')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entrada")
# print('### Acessei Entrada')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.ID,"numero_lancamento")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sugestoes_compras")
print('### Acessei  Sugestão de Compra')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo_custo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_compras")
# print('### Acessei Pedido de Compra')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[fornecedores.nome_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cartas_correcoes_documentos")
print('### Acessei Carta de Correção NF')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/juros")
print('### Acessei Juros')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[quantidade_dias_atraso_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_ecommerces")
print('### Acessei Pedidos E-commerce')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/csosn_icms")
print('### Acessei CSOSN ICMS')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/situacoes")
print('### Acessei Situações')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

print('Aguardando cobrancas_clientes')
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cobrancas_clientes")
print('### Acessei Controle de Cobrança por Cliente')

error_message = navegador.find_elements(By.NAME,"filtros[cobranca_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_correntes_colaboradores")
print('### Acessei Conta Corrente do Colaborador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[colaboradores.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_vtex_tracking")
print('### Acessei Configuração VTEX Tracking')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracao_vtex_tracking[usuario]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_integracoes_financeiras")
print('### Acessei Importação Integração Financeira')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[nome_arquivo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_impressoes_etiquetas")
print('### Acessei Configuração de Impressão de Etiquetas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vinculos_contas_ordens")
print('### Acessei Vínculo de Conta e Ordem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/button')
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/xml_cte")
print('### Acessei Importação de XML CT-e')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_losango_r0011_produtos")
print('### Acessei Tabela de Integração Losango R0011')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[codigo_produto]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/odts")
print('### Acessei ODT')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")
#print('### Acessei Pedido de Venda')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.ID,"numero_lancamento")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exposicoes")
print('### Acessei Exposição')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[filial_exposicao.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/orcamento/orcamentos")
print('### Acessei Exposição')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_contato]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recuperacoes_servicos")
print('### Acessei Exposição')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_filtro_documento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_entregas")
print('### Acessei Controle de Ordem de Entrega')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[clientes.codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_locais_estocagens_entregas")
print('### Acessei Configuração de Local de Estocagem para Entrega')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas")
print('### Acessei Relatório de Documentos de Saída')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_por_itens")
print('### Acessei Relatório de Documentos de Saída por Item')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_vendedores")
print('### Acessei Relatório de Documentos de Saída - Vendedor')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_fornecedores")
print('### Acessei Relatório Documentos de Saída - Fornecedor')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_importacoes_bancarias_automaticas")
print('### Acessei Log de importação bancária automática')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_movimentacoes_diversas")
print('### Acessei Conferência de Movimentações Diversas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_recebimentos")
print('### Acessei Relatório de Recebimentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_conciliacoes_bancarias")
print('### Acessei Importação Conciliação Bancária')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[nome_arquivo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/categorias_lancamentos_bancarios")
print('### Acessei Categoria de Lançamento Bancário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_conciliacoes_bancarias")
print('### Acessei Configuração da Conciliação Bancária')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"endereco_webservice")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_contas_correntes_colaboradores")
print('### Acessei Configuração da Conta Corrente do Colaborador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_correntes_colaboradores")
print('### Acessei Relatório de Conta Corrente do Colaborador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[valor_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controle_pdds")
print('### Acessei Controle de PDD')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_historicos_por_centro_custo")
print('### Acessei Relatório de Históricos por Centro de Custo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_fechamentos_caixas")
print('### Acessei Relatório de Fechamento de Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[listar_por]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_lotes_cobrancas")
print('### Acessei Relatório de Cobranças - Lote')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_lotes_cobrancas]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_fechamentos_caixas")
print('### Acessei Conferência de Fechamento de Caixa Cego')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_lotes_cobrancas]")
if error_message:
    print("A página foi aberta")
else:
    #erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  SEM CONFIGURAÇÃO DE CAIXA CEGO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_inadimplencias")
print('### Acessei Relatório de Inadimplência')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_receber_exportacoes")
print('### Acessei Relatório Contas a Receber - Exportação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[periodo_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_exportacoes_contas_receber")
print('### Acessei Configuração Exportação Contas a Receber')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/documentos_integracoes_financeiras")
print('### Acessei Integração Financeira')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_financeiras")
print('### Acessei Conta Financeira')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conciliacoes_cartoes")
print('### Acessei Conciliação de Cartão')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_recebimentos")
print('### Acessei Recebimentos de Caixa Aguardando Integração - DJPDV')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/status_conferencias_itens_cobrancas")
print('### Acessei Status das Conferências dos Lotes de Cobrança')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_juros_previstos_cobrados")
print('### Acessei Relatório de Juros Previstos X Juros Cobrados')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_lancamentos_creditos")
print('### Acessei Relatório Lançamentos de Créditos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[periodo_inclusao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/lotes_cobrancas")
print('### Acessei Lotes de Cobranças')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fechamentos_caixas_analiticos")
print('### Acessei Fechamento de Caixa - Analítico')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_fechamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_extrato_movimentacoes")
print('### Acessei Relatório Extrato de Movimentações')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_caixas")
print('### Acessei Relatório de Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_cheques")
print('### Acessei Relatório de Cheques')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[bom_para_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_transferencias_caixas")
print('### Acessei Conferência de Transferência de Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cheques")
print('### Acessei Controle de Cheques')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[bom_para_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fechamentos_caixas")
print('### Acessei Fechamento de Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_fechamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/lancamentos_creditos")
print('### Acessei Lançamentos de Créditos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_filtro_nome")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_saldos")
print('### Acessei Consulta Saldos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"conta_caixa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_caixas")
print('### Acessei Movimentações de Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[movimentacoes_caixas.id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_diversas")
print('### Acessei Movimentações Diversas')

error_message = navegador.find_elements(By.NAME,"movimentacao_diversa[numero_documento_bancario]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pagamentos_fornecedores")
print('### Acessei Pagamento de Fornecedor')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[titulos.numero_titulo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transferencias")
print('### Acessei Transferências de Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"transferencia[transferencias][0][valor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recebimentos")
#print('### Acessei Recebimentos')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.ID,"autocompletar_cliente_id")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/responsaveis_cobrancas")
print('### Acessei Responsável pela Cobrança')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_integracoes_bancarias")
print('### Acessei Configuração da Integração Bancária')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_banco_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_receitas_despesas")
# print('### Acessei Histórico de Receita e Despesa')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subgrupos_historicos_rd")
# print('### Acessei Subgrupos de Históricos de Receitas e Despesas')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_historicos_rd")
# print('### Acessei Grupos de Históricos de Receitas e Despesas')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1


# navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_caixas_usuarios")
# print('### Acessei Conta Caixa por Usuário')
# tela = tela + 1
# print('Tela: ', tela)
# error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
# if error_message:
#     print("A página foi aberta")
# else:
#     erro = erro+1
#     print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
# cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_por_ncm")
print('### Acessei Relatório de Documentos de Saída por NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_difal")
print('### Acessei Relatório DIFAL')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_entregas_futuras")
print('### Acessei Relatório de Entrega Futura')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_entregas_montagens")
print('### Acessei Relatório de Entrega e Montagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_pessoas.id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_tickets_medios_vendas")
print('### Acessei Relatório Ticket Médio de Vendas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_assistencia_tecnica")
print('### Acessei Relatório de Assistência Técnica')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_abertura_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_movimentacoes_assistencias_tecnicas")
print('### Acessei Tipo de Movimentação da Assistência Técnica')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/formas_pagamentos")
print('### Acessei Forma de Pagamento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_operacoes_documentos")
print('### Acessei Grupo de Operação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/operacoes_documentos")
print('### Acessei Operação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/operacoes_documentos_usuarios")
print('### Acessei Operações do Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendedores")
print('### Acessei Vendedor')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/formas_pagamentos_contas_caixas")
print('### Acessei Formas de Pagamento por Conta Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_forma_pagamento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_caixas")
print('### Acessei Conta Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_caixas")
print('### Acessei Tipo de Conta Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/multas")
print('### Acessei Multa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[quantidade_dias_carencia_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_movimentacoes_titulos")
print('### Acessei Histórico de Movimentação de Título')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/portadores_titulos")
print('### Acessei Portador de Título')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_portadores_titulos")
print('### Acessei Tipo de Portador de Título')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_titulos")
print('### Acessei Tipo de Título')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_correntes")
print('### Acessei Conta Corrente')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[bancos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/agencias")
print('### Acessei Agência')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/bancos")
print('### Acessei Banco')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[codigo_banco_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_evolucoes_inadimplencias")
print('### Acessei Relatório de Evolução da Inadimplência')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_renegociacoes_dividas")
print('### Acessei Relatório de Renegociações de Dívidas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_renegociacao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_cobranca")
print('### Acessei Relatório de Cobranças')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_agendamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_receber_cobrancas")
print('### Acessei Relatório de Contas a Receber - Cobrança')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_clientes")
print('### Acessei Relatório Razão de Clientes')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_receber")
print('### Acessei Relatório Contas a Receber')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_pagar")
print('### Acessei Relatório Contas a Pagar')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_bancarias")
print('### Acessei Integração Bancária')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"conta_caixa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/convenios")
print('### Acessei Convênio Bancário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[bancos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cartas_cobrancas")
print('### Acessei Impressões para Cobrança')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[cliente_cpf]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fluxos_caixas")
print('### Acessei Relatório de Fluxo de Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[exibicao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/limites_creditos")
print('### Acessei Controle de Crédito (Financeiro)')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/renegociacoes_dividas")
print('### Acessei Renegociação de Dívida')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cobrancas")
#print('### Acessei Controle de Cobrança')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.NAME,"filtros[cobrancas.id]")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_financeira")
print('### Acessei Consulta Financeira')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_cliente_fornecedor_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_titulos")
print('### Acessei Movimentação de Título')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/titulos")
#print('### Acessei Título')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.NAME,"filtros[numero_titulo]")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ncms_consultas_apis")
print('### Acessei Consultar NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[codigo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_moradias")
print('### Acessei Tipo de Moradia')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_integracoes_financeiras")
print('### Acessei Tabela de Integração Financeira')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_forma_pagamento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_fcp")
print('### Acessei Definição para FCP')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[ufs.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/intermediadores")
print('### Acessei Intermediador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/intermediadores")
print('### Acessei Intermediador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_pagamentos_filiais")
print('### Acessei Configuração de Pagamentos por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracao[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/colaboradores")
print('### Acessei Colaborador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/colaboradores")
print('### Acessei Colaborador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_creditos_aproveitamentos_icms")
print('### Acessei Definição de Créditos de ICMS')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_financeiras")
print('### Acessei Log de Integração Financeira')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_sistemas")
print('### Acessei Auditoria')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[mensagem]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/equipes_montagens")
print('### Acessei Equipe de Montagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_cst_icms_efetivos")
print('### Acessei Definição de CST Efetivo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[cst_icms.numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/motoristas")
print('### Acessei Motorista')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[cpf]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/codigos_beneficios_fiscais")
print('### Acessei Definição de Código de Benefício Fiscal')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[codigo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/composicoes_valores")
print('### Acessei Composição de Valores')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_transferencias_financeiras_clientes")
print('### Acessei Log de Transferências Financeiras de Clientes')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[nome_pessoa_origem_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_cobrancas_usuarios_perfis")
print('### Acessei Configuração de Cobrança por Usuário/Perfil')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atributos_formas_pagamentos")
print('### Acessei Configuração de Formas Pagamentos - Atributos da Pessoa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ncm_codigos_especificadores_st")
print('### Acessei Configuração de CEST com NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[codigos_especificadores_st.numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_economicos")
print('### Acessei Grupo Econômico')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/veiculos")
print('### Acessei Veículo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[motoristas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_recebimentos_filiais")
print('### Acessei Configuração de Recebimento por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracao[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_notificacoes")
print('### Acessei Controle de Notificação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[perfil_descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_horarios")
print('### Acessei Definição de Horário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/centros_custos")
print('### Acessei Centro de Custo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_vendas")
print('### Acessei Configuração de Liberação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_reducoes")
print('### Acessei Configurações de Reduções')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_fornecedor_id_0")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_ibpt")
print('### Acessei Consulta IBPT')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transferencias_financeiras_clientes")
print('### Acessei Transferências Financeiras de Clientes')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_origem_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_situacoes")
print('### Acessei Históricos de Alterações de Situações')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[historicos_situacoes.created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fluxos_situacoes")
print('### Acessei Fluxos das Situações')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/categorias_historicos_contatos_crm")
print('### Acessei Categorias de Históricos de Contatos (CRM)')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_documentos")
print('### Acessei Importação de Documentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"nome_do_arquivo_arquivo")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_documentos")
print('### Acessei Exportação de Documentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/representantes")
print('### Acessei Representante')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[representantes.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/compradores")
print('### Acessei Comprador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[compradores.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_despesas_variaveis")
print('### Acessei Despesas Variáveis')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_despesas_variaveis")
print('### Acessei Tipos de Despesas Variáveis')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cte")
print('### Acessei CT-e')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transportadores")
print('### Acessei Transportador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/montadores")
print('### Acessei Montadores')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_dre")
print('### Acessei Configurações de DRE')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/dias_uteis")
print('### Acessei Definição de Dias Úteis')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conversoes")
print('### Acessei Tabela de Conversões para Importação de XML')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_entrada_id_cfop_cfop_0")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contadores")
print('### Acessei Contador')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[contadores.crc_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_nf")
print('### Acessei Configuração NF')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[filiais.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/modelos_nf_filiais")
print('### Acessei Modelo de NF por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"modelo_nf_filial[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/modelos_nf")
print('### Acessei Modelo de NF')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/programas_usuarios")
print('### Acessei Programas do Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_usuario")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/perfis_usuarios")
print('### Acessei Perfil do Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/usuarios")
print('### Acessei Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"pessoas.nome_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/filiais")
print('### Acessei Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.cpf_cnpj_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/codigos_especificadores_st")
print('### Acessei CEST')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cfop")
print('### Acessei CFOP')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_ipi")
print('### Acessei Código de Situação Tributária do IPI')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_cofins")
print('### Acessei Código de Situação Tributária do COFINS')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_pis")
print('### Acessei Código de Situação Tributária do PIS')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_icms_produtos_ncm")
print('### Acessei Código de Situação Tributária do ICMS por Produto/NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[ufs_origem.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_icms_ufs")
print('### Acessei Código de Situação Tributária do ICMS por UF')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[cst_icms.numero]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_especificas")
print('### Acessei Definição de CST Específico')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[operacoes_documentos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_icms")
print('### Acessei Código de Situação Tributária do ICMS')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ncm")
print('### Acessei NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/itens_ncm")
print('### Acessei Item de NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subposicoes_dois_ncm")
print('### Acessei Subposições II de NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subposicoes_um_ncm")
print('### Acessei Subposições I de NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/posicoes_ncm")
print('### Acessei Posição de NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/capitulos_ncm")
print('### Acessei Capítulo de NCM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_enderecos")
print('### Acessei Tipo de Endereço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ceps")
print('### Acessei CEP')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[cep_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/bairros")
print('### Acessei Bairro')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[bairros.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cidades")
print('### Acessei Cidade')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[cidades.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ufs")
print('### Acessei UF')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/paises")
print('### Acessei País')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_romaneios_filiais")
print('### Acessei Visibilidade de Romaneio de Separação por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_aprovacoes_classificacoes_riscos")
print('### Acessei Configuração para Aprovação de Análise de crédito - Risco')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracoes_aprovacoes_classificacoes_riscos[0][classificacao_risco]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_romaneios_montagens_filiais")
print('### Acessei Visibilidade de Romaneio de Montagem por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_analises_creditos")
print('### Acessei Integração Análise de Crédito')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/classificacoes_riscos")
print('### Acessei Classificação de Risco - Análise de Crédito')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[risco]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_integracoes_analises_creditos")
print('### Acessei Configuração de Integração para Análise de Crédito')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo_integracao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consultas_precos")
print('### Acessei Consulta de Preços')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_produto_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/competencias_documentos")
print('### Acessei Competências - Documentos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_aprovacoes_analises_creditos")
print('### Acessei Configuração para Aprovação de Análise de créditos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracoes_aprovacoes_analises_creditos[0][configuracoes_aprovacoes_analises_creditos_papeis_aprovacoes_attributes[0][papel_aprovacao_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_produtos")
print('### Acessei Visibilidade de Produtos por Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_atingimentos_metas_recebimentos")
print('### Acessei Relatório de Comissão por Atingimento de Meta - Recebimento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_vendedores_descontos")
print('### Acessei Relatório de Comissão dos Vendedores - Desconto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_descontos")
print('### Acessei Controle de Comissão - Desconto Venda')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"definicao_comissao_desconto[itens_definicoes_comissoes_descontos_attributes][0][escopo][escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_creditos")
print('### Acessei Relatório de Análise de Crédito')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[analises_creditos.created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_titulos")
print('### Acessei Visibilidade de Títulos por Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_renegociacoes_pendentes")
print('### Acessei Configuração de Liberação de Renegociações Pendentes')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_analises_creditos_usuarios")
print('### Acessei Visibilidade de Análise de Crédito por Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas_canais_vendas")
print('### Acessei Relatório de Análise de Vendas - Canal de Venda')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_emissoes_documentos_saidas")
print('### Acessei Configuração Emissão Documento de Saída no Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sequencias_tipos_custos")
print('### Acessei Sequência do Tipo de Custo')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_descontos_recebimentos")
print('### Acessei Desconto - Recebimento Por Nível de Aprovação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_crm")
print('### Acessei Relatório CRM')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_operacoes_filiais")
print('### Acessei Visibilidade de Operação Por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_ordens_servicos")
print('### Acessei Visibilidade de Assistência Técnica')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_clientes_inadimplentes")
print('### Acessei Configuração de Liberação de Clientes Inadimplentes')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_tempos_medios_atendimentos")
print('### Acessei Definição Tempo Médio Atendimento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_registros_spc")
print('### Acessei Relatório de Registros do SPC')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/registros_positivacoes_spc")
print('### Acessei Registro de Positivação do SPC')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_contrato]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/registros_negativacoes_spc")
print('### Acessei Registro de Negativação do SPC')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_contrato]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_registros_spc")
print('### Acessei Históricos de Registros do SPC')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simulacoes_precos")
print('### Acessei Simulação de Preço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_produto_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_consultas_spc")
print('### Acessei Históricos de Consulta SPC')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_consultas_spc")
print('### Acessei Históricos de Consulta SPC')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_papeis_usuarios")
print('### Acessei Configuração de Papel de Aprovação por Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[validade_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_niveis_tipos_liberacoes")
print('### Acessei Configuração de Nível por Tipo de Liberação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/niveis_aprovacoes")
print('### Acessei Nível de Aprovação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/papeis_aprovacoes")
print('### Acessei Papel de Aprovação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/desvinculos_documentos_devolucoes")
print('### Acessei Desvínculo de Documentos de Devolução')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas_tabelas_precos")
print('### Acessei Relatório de Análise de Vendas Entre Tabelas de Preços')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_percentuais_atingimentos_tabelas_precos")
print('### Acessei Definição de Percentual de Atingimento por Tabela de Preço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controles_comissoes_formas_pagamentos")
print('### Acessei Controle de Comissão por Forma de Pagamento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_forma_pagamento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_formas_pagamentos_vendedores")
print('### Acessei Relatório de Comissão por Forma de Pagamento - Vendedor')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_visibilidades_documentos_filiais")
print('### Acessei Visibilidade de Documentos por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_clientes_sem_movimento")
print('### Acessei Relatório de Clientes sem Movimento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_movimentacoes_financeiras")
print('### Acessei Relatório de Movimentação Financeira por Conta Caixa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas_produtos")
print('### Acessei Relatório de Análise de Vendas - Totalizadas por Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_estoques_filiais")
print('### Acessei Visibilidade de Estoque por Filial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas")
print('### Acessei Relatório de Análise de Vendas - Composição de Comissão')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_metas")
print('### Acessei Relatório de Análise de Meta')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/descontos_recebimentos")
print('### Acessei Desconto - Recebimento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_atingimentos_metas")
print('### Acessei Relatório de Comissão por Atingimento de Meta')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_metas_totais")
print('### Acessei Configuração de Atingimento de Meta')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_contabeis")
print('### Acessei Exportação Contábil')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"exportacao_contabil[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_contabilidades_empresas")
print('### Acessei Definição de Contabilidade por Empresa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_integracoes_contabeis")
print('### Acessei Configuração de Integração Contábil')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_cobrancas")
print('### Acessei Relatório de Comissão por Cobrança - Lote')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_pagamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_cobrancas")
print('### Acessei Controle de Comissão por Cobrança')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/comissoes_metas")
print('### Acessei Comissão por Meta')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_recebimentos")
print('### Acessei Relatório de Comissão por Recebimento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_profissionais")
print('### Acessei Tipo de Profissional')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/profissionais")
print('### Acessei Profissional')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_tabelas_precos")
print('### Acessei Tipo de Tabela de Preço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_pedidos_compras")
print('### Acessei Tipo de Pedido de Compra')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pdv/configuracoes_integracoes")
print('### Acessei Configuração de Integração com PDV')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"token")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/orcamento/campanhas_marketings")
print('### Acessei Canal de Venda')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/justificativas")
print('### Acessei Justificativa')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sugestoes_observacoes")
print('### Acessei Observações')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_series_ecf")
print('### Acessei Configuração de Série de ECF')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_serie_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/informacoes_complementares_documentos")
print('### Acessei Informações Complementares do Documento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[mensagem_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_totais_vendas")
print('### Acessei Relatório de Análise de Vendas')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tef/tokens_filiais_usuarios")
print('### Acessei Configuração TEF por Filial/Usuário')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[filiais.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tef/consultas")
print('### Acessei Consulta de Transações via TEF')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sat/configuracoes_integracoes")
print('### Acessei Configuração de Integração PDV/SAT')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"configuracao_integracao_sat[][filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_servicos")
print('### Acessei Relatório de Serviços')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_liberacoes_analises_creditos")
print('### Acessei Configuração de Liberação Para Análise de Crédito')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_demonstracoes_produtos")
print('### Acessei Relatório de Demonstração de Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_demonstracao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_recebimentos")
print('### Acessei Controle de Comissão por Recebimento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"percentual_comissao_empresa")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_montadores")
print('### Acessei Controle de Comissão de Montagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes")
print('### Acessei Controle de Comissão')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"definicao_comissao[itens_definicoes_comissoes][-1][percentual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_aniversariantes")
print('### Acessei Relatório de Aniversariantes')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_controles_profissionais")
print('### Acessei Relatório do Controle de Profissionais')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_tir")
print('### Acessei Relatório de TIR')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_margem_contribuicao")
print('### Acessei Relatório de Margem de Contribuição')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_margens_brutas")
print('### Acessei Relatório de Margem Bruta')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_montadores")
print('### Acessei Relatório de Comissão dos Montadores')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_alteracoes_produtos")
print('### Acessei Relatório de Alterações de Preço do Produto')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_metas")
print('### Acessei Relatório de Comissão por Meta')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_vendedores")
print('### Acessei Relatório de Comissão dos Vendedores')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


#navegador.get("https://felipe.testes.smart.sgisistemas.com.br/analises_creditos")
#print('### Acessei Análise de Crédito')
#tela = tela + 1
#print('Tela: ', tela)
#error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
#if error_message:
#    print("A página foi aberta")
#else:
#    erro = erro+1
#    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
#cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contatos_crm")
print('### Acessei Contatos (CRM)')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/markup")
print('### Acessei Markup')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/liberacoes_vendas")
print('### Acessei Liberação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/margens_contribuicoes")
print('### Acessei Recálculo da Margem de Contribuição')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"autocompletar_filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_margens_contribuicoes")
print('### Acessei Configuração da Margem de Contribuição')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_tir")
print('### Acessei Definição de TIR')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_descontos")
print('### Acessei Controle de Desconto - Venda')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/metas")
print('### Acessei Controle de Meta')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_descontos_fornecedores")
print('### Acessei Definições de Descontos por Fornecedores')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestao_precos")
print('### Acessei Gestão de Preço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"tabela_preco_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_precos_fornecedores")
print('### Acessei Tabela de Preço por Fornecedor')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"tabela_preco_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_precos")
print('### Acessei Tabela de Preço')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_bonificacoes")
print('### Acessei Definição de Bonificação')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/paineis_gerenciais")
print('### Acessei Painel Gerencial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"data_inicial")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/dre")
print('### Acessei DRE')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_financeira")
print('### Acessei Relatório de Documentos de Saída - Financeira')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_orcamentos")
print('### Acessei Tipo de Orçamento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_devolucoes_vendas_ce")
print('### Acessei Configuração de Liberação Devolução de Venda com Encomenda')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_devolucoes_vendas_se")
print('### Acessei Configuração de Liberação Devolução de Venda sem Encomenda')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_montagens")
print('### Acessei Tabela de Montagem')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_fretes_entregas")
print('### Acessei Relatório de Fretes por Entrega')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simulacoes_vendas")
print('### Acessei Simulação de Venda')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"forma_pagamento_id_0")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_liberacoes_prorrogacoes_parcelas")
print('### Acessei Configuração Liberação Prorrogação do Primeiro Vencimento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/mdfe")
print('### Acessei MDF-e')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/autorizacoes_pagamentos")
print('### Acessei Autorização de Pagamento')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.NAME,"filtros[fornecedor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_definicoes_tributacoes_produtos")
print('### Acessei Consulta definições de tributação de produtos')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"pesquisar_produto")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_whatsapp")
print('### Acessei Configuração do Whatsapp')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"filiais.descricao_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_mensagens_whatsapp")
print('### Acessei Configuração de mensagem do Whatsapp')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"configuracoes_whatsapp.numero_whatsapp_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/chats")
print('### Acessei Instâncias do Whatsapp')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[2]/div/div/div")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_whatsapp/new")
print('### Acessei Adicionar configuração do Whatsapp')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"url")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_chats_whatsapp")
print('### Acessei Log do Whatsapp')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"telefone_conectado")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


print("################################################################################")
#ENCERRAMENTO
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")
print('### Acessei Tela Inicial')
tela = tela + 1
print('Tela: ', tela)
error_message = navegador.find_elements(By.ID,"botao_perfil_barra_menu")
if error_message:
    print("O menu foi aberto")
    navegador.find_element(By.ID,"botao_perfil_barra_menu").click()
    navegador.find_element(By.ID,"botao_sair_perfil_menu").click()
    print("Encerrado")

else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
#"""



hora_fim = datetime.datetime.now()
tempo_total = (hora_fim - hora_inicio)
if nr_lcto == 0:
    print("-------------------------------------")
    print("Verificar as seguintes funções: ", '\n' "cadastrar_venda", '\n' "recebimentos", '\n' "gestao_entrega", '\n' "devolucao_venda", '\n' "encomenda_de_produtos")
print("-------------------------------------")
print("Robô iniciado em ", hora_inicio,'\n' "Robô finalizado em ", hora_fim, '\n' "Tempo de execução", tempo_total, '\n' "Quantidade de telas verificadas", cont, '\n' "Telas com erro", erro, '\n' "Número do lançamento gerado:", nr_lcto )

#input("Pressione Enter para continuar...")


hora_fim = datetime.datetime.now()
tempo_total = (hora_fim - hora_inicio)

# Configurações do email
email_remetente = 'felipe.rossi@sgisistemas.com.br'
email_destinatarios = ['feliperossihav@icloud.com', 'sgi.felipe@gmail.com']  # Lista de destinatários
senha_remetente = 'TodasAsBoasSenhasJaEram!123'  # Senha do remetente

# Construindo o email
msg = MIMEMultipart()
msg['From'] = email_remetente
msg['To'] = ', '.join(email_destinatarios)  # Transforma a lista em uma string separada por vírgulas
msg['Subject'] = 'ENVIO AUTOMÁTICO - Verificação deploy - Felipe Rossi'



if nr_lcto == 0:
    corpo_email = f"""\
    -------------------------------------
    Verificar as seguintes funções: '\n' "cadastrar_venda", '\n' "recebimentos", '\n' "gestao_entrega", '\n' "devolucao_venda", '\n' "encomenda_de_produtos")
    **********************************************
    Robô iniciado em {hora_inicio}
    Robô finalizado em {hora_fim}
    Tempo de execução: {tempo_total}
    Quantidade de telas verificadas: {cont}
    Telas com erro: {erro}
    -----------------------------------------------
    Funções executadas
    cadastrar_venda(venda parcelada com entrega)
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
    venda_com_encomenda(avista com encomenda)
    faturamento_de_venda()
    encomenda_de_produto()
    cadastro_departamento()
    cadastro_grupo()
    cadastro_subgrupo()
    cadastro_produto()
    caixaconta_por_usuario()
    pdv_oline()
    conta_corrente()
    simulacao_venda()
    cadastro_grupo_receita_despesa()
    cadastro_subgrupo_historico_receita_despesa()
    cadastro_historico_receita_despesa()
"""
else:
    corpo_email = f"""\
    **********************************************
    Robô iniciado em {hora_inicio}
    Robô finalizado em {hora_fim}
    Tempo de execução: {tempo_total}
    Quantidade de telas verificadas: {cont}
    Telas com erro: {erro}
    Funções executadas
    cadastrar_venda(venda parcelada com entrega)
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
    venda_com_encomenda(avista com encomenda)
    faturamento_de_venda()
    encomenda_de_produto()
    cadastro_departamento()
    cadastro_grupo()
    cadastro_subgrupo()
    cadastro_produto()
    caixa_conta_por_usuario()
    pdv_oline()
    conta_corrente()
    simulacao_venda()
    cadastro_grupo_receita_despesa()
    cadastro_subgrupo_historico_receita_despesa()
    cadastro_historico_receita_despesa()
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