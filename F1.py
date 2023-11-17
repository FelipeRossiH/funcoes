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
import random

smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0
nr_lcto = 0


def cadastro_e_alteracao_de_escolaridade():

    try:
        print("######### TELA ESCOLARIDADE ##########")
        print("Cadastro e alteração de escolaridade")
        sleep(3)  # Espera até 3 segundos por elementos

        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escolaridades")
        print('### Abrindo cadastro de escolaridade')

        # Clique no botão para abrir o formulário de cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

        # Preenche o campo "descricao" com o valor "Escolaridade Automática"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Escolaridade Automática')
        print('### Preenchido campo "descricao" com "Escolaridade Automática"')

        # Clique no botão "Salvar"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
        sleep(3)

        # Preenche o campo "descricao" com o valor "Escolaridade Automática Alterada"
        nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
        nome_element.send_keys('Escolaridade Automática Alterada')
        print('### Preenchido campo "descricao" com "Escolaridade Automática Alterada')
        sleep(3)

        # Clique no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[1]').click()
        sleep(5)

        # Obtenha o código da escolaridade
        codigo_escolaridade = navegador.find_element(By.CLASS_NAME, "campo_id")
        print('### Código da escolaridade:', codigo_escolaridade.text)

    finally:
        print('>> Encerrando função cadastro_e_alteracao_de_escolaridade.')
        # Feche o navegador
        #navegador.quit()

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

        # Clique no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/input[1]').click()
        sleep(3)

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
        sleep(3)
        # Clique no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/input[1]').click()
        sleep(3)
        # Clique no link para excluir o cadastro
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
        sleep(3)
        # Clique no botão "Excluir"
        navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/a[2]').click()

        # Confirme a exclusão
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

        # Clique no botão "Salvar"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]'))
        ).click()
        sleep(3)
        # Clique no botão "Excluir"
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[2]'))
        ).click()
        sleep(2)

        # Confirme a exclusão
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

    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[18]/ul/li[2]/a').click()
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="tipo_endereco_id_0"]').click()
    nome_element = navegador.find_element(By.XPATH, '//*[@id="tipo_endereco_id_0"]')
    nome_element.send_keys('R')
    print('### Passei tipo de endereço.')

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
    elemento.click()

    hora_fim = datetime.datetime.now()
    print('Fim de execução: ', hora_fim)
    tempo_total = (hora_fim - hora_inicio)
    sleep(2)

    print('###### Pessoa física cadastrada com sucesso\n##### CPF cadastrado: ', CPFcopiado, 'Tempo de execução: ', tempo_total)
    print('Encerrado função cadastro_pessoa')


def cadastrar_venda(numero_cliente, numero_produto):

    try:
        global nr_lcto
        print('########## TELA PEDIDO DE VENDA ##########')
        navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")


        # Preencher o campo "Cliente"
        nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
        nome_element.send_keys(numero_cliente)
        print('### Passei Cliente', numero_cliente)
        sleep(2)
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
        sleep(3)
        nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
        sleep(2)
        nome_element.send_keys('1')
        print('### Passei quantidade.')
        pyautogui.hotkey('ENTER')
        sleep(3)

        # Preencher o campo "Forma de Pagamento"
        nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
        nome_element.send_keys('V')
        sleep(3)
        pyautogui.hotkey('ENTER')
        print('### Passei forma de pagamento carnê')

        # Preencher o campo "Quantidade de Parcelas"
        sleep(2)
        nome_element = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
        sleep(2)
        nome_element.send_keys('0')
        sleep(2)
        print('### Passei quantidade de parcelas.')

        # Clicar no botão "Salvar"
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        #sleep(10)
        print("Aguarda 20 segundos para liberação")
        for segundo_atual in range(30, 0, -1):
            print(f"Tempo restante: {segundo_atual} segundos")
            sleep(1)


    #    Preencher campos de liberação
        navegador.find_element(By.ID, 'login_liberacao_venda').click()
        nome_element = navegador.find_element(By.ID, 'login_liberacao_venda')
        nome_element.send_keys('projeto.casa')
        pyautogui.hotkey('tab')
        print('### Passei usuário de liberação')

        navegador.find_element(By.ID, 'senha_liberacao_venda').click()
        nome_element = navegador.find_element(By.ID, 'senha_liberacao_venda')
        nome_element.send_keys('@rlequin@2020')
        pyautogui.hotkey('tab')
        print('### Passei senha de liberação')
        pyautogui.hotkey('ENTER')
        sleep(2)

        # Clicar no botão "Salvar" novamente
        navegador.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/button').click()
        sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="botao_salvar"]').click()
        sleep(12)

        # Obter número do lançamento
        b_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/b')
        b_text = b_element.text
        nr_lcto = b_text[14:19]
        print('#### Número do lançamento: ', nr_lcto)
        sleep(2)

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

def gestao_entrega():
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
    sleep(3)
    print('Marcar lançamento...')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div[3]/table/tbody/tr/td[1]/label').click()
    sleep(2)
    print('Gerar romaneio...')
    navegador.find_element(By.XPATH, '//*[@id="btn_gerar_romaneio"]').click()
    sleep(2)
    print('Confirmando geração... ')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/button[2]').click()
    sleep(3)
    print('Alterar situação...')
    sleep(8)
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[2]/div[1]/button').click()
    sleep(2)
    print('Finalizar... ')
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[2]/div[1]/ul/li[1]/a').click()
    navegador.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/button[2]').click()
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
    nome_element.send_keys('01102023')
    print("Passei data inicial")
    sleep(2)
    nome_element = navegador.find_element(By.ID, 'data_final')
    nome_element.clear()
    nome_element.send_keys('31102023')
    print("Passei data final")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div/div[5]/span/div/div[1]/table/tbody/tr[1]/td[2]')
    actions = ActionChains(navegador)
    actions.double_click(nome_element).perform()
    print("Passei filial 1")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '//*[@id="btn-gerar-sped"]').click()
  finally:
    sleep(20)
    print("Encerrando funcao_gera_sped_fiscal")

def funcao_gera_sped_contribuicao():

  try:
    navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped_contribuicoes")
    tme = 30
    print("########## SPED CONTRIBUIÇÃO ##########")

    nome_element = navegador.find_element(By.ID, 'data_inicial')
    nome_element.clear()
    nome_element.send_keys('01102023')
    print("Passei data inicial")
    sleep(2)
    nome_element = navegador.find_element(By.ID, 'data_final')
    nome_element.clear()
    nome_element.send_keys('31102023')
    print("Passei data final")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
    actions = ActionChains(navegador)
    actions.double_click(nome_element).perform()
    print("Passei filial 1")
    sleep(2)
    nome_element = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
  finally:
    sleep(20)
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
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div/form/div/div[2]/div[2]/div/div[17]/div/button[1]').click()
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
    navegador.find_element(By.ID, 'cabecalho_aba_container_financeiro').click()
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
    navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div[5]/div[2]/div[1]/div[1]/div/div/div[2]/div/ul/li[8]/a').click()
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
usuario_element.send_keys('robo.casa')
print('### Passei usuário.')


senha_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'senha')))
senha_element.send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)





# Chamada de funções
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

print('#######################################################################')
print('#                LIBERADO USO MOUSE E TECLADO                         #')
print('#######################################################################')
sleep(3)

#"""
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pessoas")
print('########## TELA PESSOA ##########')
error_message = navegador.find_elements(By.NAME,"filtros[nome]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
    result_teste = ">>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO"
cont = cont +1

#sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos")
print('########## TELA PRODUTOS ##########')
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
    result_teste = ">>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO"
cont = cont +1


sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/empresas/1/edit")
print('########## TELA CONFIGURAÇÃO DA EMRPESA ##########')

error_message = navegador.find_elements(By.NAME,"pessoa[nome]")
if error_message:
    print("A página foi aberta")
    navegador.find_element(By.NAME,"commit").click()
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
sleep(3)
cont = cont +1

sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_inventarios")
print('### Acessei Relatório de Inventário')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ncm]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_precos_produtos")
print('### Acessei Relatório de Preços de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[status_produto]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_sef")
print('### Acessei SEF II')

error_message = navegador.find_elements(By.NAME,"exportacao_sef[data_base]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/demonstracoes")
print('### Acessei Demonstração de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entradas_manuais")
print('### Acessei Entrada Manual')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_fretes")
print('### Acessei Tabela de Frete')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_orcamentos")
print('### Acessei Relatório de Orçamentos')

error_message = navegador.find_elements(By.NAME,"filtros[detalhamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_servicos")
print('### Acessei Log de Integração Serviços')

error_message = navegador.find_elements(By.NAME,"filtros[lancamento_documento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escolaridades")
print('### Acessei Escolaridade')

error_message = navegador.find_elements(By.NAME,"filtros[escolaridades.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_dependentes")
print('### Acessei Tipo de Dependente')

error_message = navegador.find_elements(By.NAME,"filtros[tipos_dependentes.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_mva_antecipacoes")
print('### Acessei Configuração MVA Antecipação (%)')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_servicos")
print('### Acessei Configuração por Tipo de Serviço')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/especificacoes_produtos")
print('### Acessei Especificação do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_montagens_produtos")
print('### Acessei Configuração de Tipo de Montagem por Produto')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atualizacoes_codigos_pessoas")
print('### Acessei Atualização de Código de Pessoas')

error_message = navegador.find_elements(By.ID,"gerar_codigo_automaticamente")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_servicos")
print('### Acessei Definição de Serviço')

error_message = navegador.find_elements(By.ID,"servicos.descricao_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atualizacoes_automaticas_precos")
print('### Acessei Atualizações Automáticas de Tabela de Preço')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_variacoes_grades")
print('### Acessei Grupo Variações de Grade')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/variacoes_grades")
print('### Acessei Variações de Grade')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/designers_produtos")
print('### Acessei Designer do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_encomendas_produtos")
print('### Acessei Configuração de Encomenda de Produtos')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/mva")
print('### Acessei MVA')

error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cores_produtos")
print('### Acessei Cor')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/unidades_medidas")
print('### Acessei Unidade de Medida')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/origens_produtos")
print('### Acessei Origem do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[numero]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/marcas_produtos")
print('### Acessei Marca do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subgrupos_produtos")
print('### Acessei Subgrupo do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_produtos")
print('### Acessei Grupo do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/departamentos_produtos")
print('### Acessei Departamento do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/profissoes")
print('### Acessei Profissão')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/meios_contatos")
print('### Acessei Meio de Contato')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_referencias")
print('### Acessei Tipo de Referência')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/servicos")
print('### Acessei Serviço')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/kits_produtos")
print('### Acessei Kit de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/kits_produtos")
print('### Acessei Kit de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_compras")
print('### Acessei Relatório de Análise de Compras')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/baixar_xmls_mdfe")
print('### Acessei Baixar XML de MDF-e')

error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_detalhamentos_custos")
print('### Acessei Relatório de Detalhamento de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_liberacoes_pedidos_compras")
print('### Acessei Configuração de Liberação do Pedido de Compra')

error_message = navegador.find_elements(By.ID,"titulo_campo_tipos_pedidos_compras_ids")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_pedidos_compras")
print('### Acessei Relatório de Pedido de Compra')

error_message = navegador.find_elements(By.NAME,"filtros[data_inclusao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_cooperados")
print('### Acessei Relatório de Cooperado')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_entradas")
print('### Acessei Relatório de Documentos de Entrada')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/encomendas_produtos")
print('### Acessei Encomenda de Produtos')

error_message = navegador.find_elements(By.NAME,"filtros[encomendas_produtos.created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controles_impressoes_etiquetas")
print('### Acessei Controle de Impressão de Etiquetas')

error_message = navegador.find_elements(By.NAME,"configuracao_impressao_etiqueta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/impressoes_etiquetas")
print('### Acessei Impressão de Etiquetas')

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

error_message = navegador.find_elements(By.ID,"filtro_nome_fornecedor")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/xml_sefaz")
print('### Acessei Baixar XML de Documentos')

error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cancelamento_documentos")
print('### Acessei Cancelamento de Documentos')

error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/devolucoes_documentos")
print('### Acessei Devolução')

error_message = navegador.find_elements(By.ID,"autocompletar_numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/documentos")
print('### Acessei Documentos')

error_message = navegador.find_elements(By.NAME,"filtros[cliente_fornecedor.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/estoques_minimos_ecommerces")
print('### Acessei Estoque Mínimo do E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_ecommerces")
print('### Acessei Log do E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestoes_ecommerces")
print('### Acessei Gestão E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[pedidos_ecommerces.id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos_ecommerces")
print('### Acessei Produto E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/distribuicoes_mercadorias")
print('### Acessei Distribuição de Mercadoria')

error_message = navegador.find_elements(By.ID,"autocompletar_filial_entrega_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_enderecamentos_estoques")
print('### Acessei Relatório de Endereçamento de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[detalhamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_niveis_enderecamentos")
print('### Acessei Produto por Endereçamento')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/enderecamentos")
print('### Acessei Níveis de Endereçamento')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1




navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_estoques")
print('### Acessei Auditoria de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_encomendas_produtos")
print('### Acessei Relatório de Encomendas')

error_message = navegador.find_elements(By.NAME,"filtros[data_encomenda_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestoes_montagens")
print('### Acessei Gestão de Montagem')

error_message = navegador.find_elements(By.NAME,"filtros[previsao_montagem_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/romaneios_montagens")
print('### Acessei Romaneio de Montagem')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_locais_estocagens")
print('### Acessei Relatório Razão de Produto por Local de Estocagem')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/distribuicoes_estoques")
print('### Acessei Relatório de Distribuição de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[exibir_estoque_detalhado]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_entregas_transportador")
print('### Acessei Relatório de Entregas por Transportador')

error_message = navegador.find_elements(By.NAME,"filtros[data_venda_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_ordens_servicos")
print('### Acessei Tipo de Assistência Técnica')

error_message = navegador.find_elements(By.ID,"descricao_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escopos_configuracoes_custos")
print('### Acessei Configurações de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_movimentacoes_codigos_unicos")
print('### Acessei Relatório de Movimentações dos Códigos Únicos')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/codigos_unicos")
print('### Acessei Código Único')

error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_codigos_unicos")
print('### Acessei Configuração de Código Único')

error_message = navegador.find_elements(By.NAME,"filtros[definicao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_servicos_documentos")
print('### Acessei Assistência Técnica a partir do Documento')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_servicos")
print('### Acessei Assistência Técnica')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entregas_montagens")
print('### Acessei Controle de Agendamento de Serviços')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_estoque_minimo_maximo")
print('### Acessei Relatório De Estoque Mínimo/Máximo')

error_message = navegador.find_elements(By.NAME,"filtros[agrupamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_produtos")
print('### Acessei Relatório Razão de Produtos')

error_message = navegador.find_elements(By.NAME,"filtros[ativo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_giros_estoques")
print('### Acessei Relatório de Giro Médio do Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[opcoes]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_posicao_estoque")
print('### Acessei Relatório de Posição do Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[tipo_valor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_auditorias_estoques_produtos")
print('### Acessei Relatório de Auditoria do Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[filial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_transferencias_mercadorias")
print('### Acessei Relatório de Transferência de Mercadoria')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/reservas_produtos")
print('### Acessei Gestão de Entrega')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_produto]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/romaneios_separacoes")
print('### Acessei Romaneio de Separação')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_estoques_configuracoes")
print('### Acessei Configuração Auditoria de Estoque')

error_message = navegador.find_elements(By.ID,"autocompletar_operacao_documento_entrada_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_entradas_transferencias")
print('### Acessei Conferência de Entrada por Transferência')

error_message = navegador.find_elements(By.NAME,"filial_destino")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transferencias_mercadorias")
print('### Acessei Transferência de Mercadoria')

error_message = navegador.find_elements(By.NAME,"filtros[documentos_saidas.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/parametros_transferencias_mercadorias")
print('### Acessei Parâmetro para Transferência de Mercadoria')

error_message = navegador.find_elements(By.NAME,"filtros[filial_origem.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/requisicoes_mercadorias")
print('### Acessei Requisição de Mercadorias')

error_message = navegador.find_elements(By.ID,"autocompletar_filial_origem_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_locais_estocagens")
print('### Acessei Movimentação Local de Estocagem')

error_message = navegador.find_elements(By.NAME,"filtros[locais_estocagens.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/locais_estocagens")
print('### Acessei Local de Estocagem')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fechamentos_estoques")
print('### Acessei Fechamento de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[filiais.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/estoques_minimo_maximo")
print('### Acessei Estoque Mínimo/Máximo')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_estoques")
print('### Acessei Consulta de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simulacoes_guias_icms")
print('### Acessei Simulação de Guias de ICMS e ICMS ST')

error_message = navegador.find_elements(By.NAME,"nao_considerar")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_nfe_inutilizadas")
print('### Acessei Relatório de Notas Inutilizadas')

error_message = navegador.find_elements(By.NAME,"filtros[data_inutilizacao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contabilizacao")
print('### Acessei Relatório de Contabilização')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/guias_icms_st")
print('### Acessei Guia de Imposto')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/nf_complementar")
print('### Acessei NF-e Complementar')

error_message = navegador.find_elements(By.NAME,"nf_complementar[tipo_nfe]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_xml_nfe")
print('### Acessei Exporta XML NF-e e NFC-e')

error_message = navegador.find_elements(By.NAME,"exporta_xml_nfe[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sintegra")
print('### Acessei SINTEGRA')

error_message = navegador.find_elements(By.NAME,"sintegra[finalidade_arquivo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped")
print('### Acessei SPED Fiscal')

error_message = navegador.find_elements(By.NAME,"sped[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/inutilizacao_nfe")
print('### Acessei Inutilização NF-e')

error_message = navegador.find_elements(By.NAME,"filtros[numero_nfe_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simples_remessa")
print('### Acessei Simples Remessa')

error_message = navegador.find_elements(By.ID,"autocompletar_numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped_contribuicoes")
print('### Acessei SPED Contribuições')

error_message = navegador.find_elements(By.NAME,"sped[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_ecommerces")
print('### Acessei Configuração E-commerce')

error_message = navegador.find_elements(By.NAME,"configuracao_ecommerce[tipo_integracao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_ecommerces")
print('### Acessei Log de Integração do E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entrada")
print('### Acessei Entrada')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sugestoes_compras")
print('### Acessei  Sugestão de Compra')

error_message = navegador.find_elements(By.NAME,"filtros[tipo_custo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_compras")
print('### Acessei Pedido de Compra')

error_message = navegador.find_elements(By.NAME,"filtros[fornecedores.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cartas_correcoes_documentos")
print('### Acessei Carta de Correção NF')

error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/juros")
print('### Acessei Juros')

error_message = navegador.find_elements(By.NAME,"filtros[quantidade_dias_atraso_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_ecommerces")
print('### Acessei Pedidos E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/csosn_icms")
print('### Acessei CSOSN ICMS')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/situacoes")
print('### Acessei Situações')
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

error_message = navegador.find_elements(By.NAME,"filtros[colaboradores.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_vtex_tracking")
print('### Acessei Configuração VTEX Tracking')

error_message = navegador.find_elements(By.NAME,"configuracao_vtex_tracking[usuario]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_integracoes_financeiras")
print('### Acessei Importação Integração Financeira')

error_message = navegador.find_elements(By.NAME,"filtros[nome_arquivo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_impressoes_etiquetas")
print('### Acessei Configuração de Impressão de Etiquetas')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vinculos_contas_ordens")
print('### Acessei Vínculo de Conta e Ordem')

error_message = navegador.find_elements(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/button')
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/xml_cte")
print('### Acessei Importação de XML CT-e')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_losango_r0011_produtos")
print('### Acessei Tabela de Integração Losango R0011')

error_message = navegador.find_elements(By.NAME,"filtros[codigo_produto]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/odts")
print('### Acessei ODT')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")
print('### Acessei Pedido de Venda')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exposicoes")
print('### Acessei Exposição')

error_message = navegador.find_elements(By.NAME,"filtros[filial_exposicao.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/orcamento/orcamentos")
print('### Acessei Exposição')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_contato]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recuperacoes_servicos")
print('### Acessei Exposição')

error_message = navegador.find_elements(By.ID,"autocompletar_filtro_documento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_entregas")
print('### Acessei Controle de Ordem de Entrega')

error_message = navegador.find_elements(By.NAME,"filtros[clientes.codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_locais_estocagens_entregas")
print('### Acessei Configuração de Local de Estocagem para Entrega')

error_message = navegador.find_elements(By.ID,"filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas")
print('### Acessei Relatório de Documentos de Saída')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_por_itens")
print('### Acessei Relatório de Documentos de Saída por Item')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_vendedores")
print('### Acessei Relatório de Documentos de Saída - Vendedor')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_fornecedores")
print('### Acessei Relatório Documentos de Saída - Fornecedor')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_importacoes_bancarias_automaticas")
print('### Acessei Log de importação bancária automática')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_movimentacoes_diversas")
print('### Acessei Conferência de Movimentações Diversas')

error_message = navegador.find_elements(By.NAME,"filtros[movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_recebimentos")
print('### Acessei Relatório de Recebimentos')

error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_conciliacoes_bancarias")
print('### Acessei Importação Conciliação Bancária')

error_message = navegador.find_elements(By.NAME,"filtros[nome_arquivo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/categorias_lancamentos_bancarios")
print('### Acessei Categoria de Lançamento Bancário')

error_message = navegador.find_elements(By.NAME,"filtros[codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_conciliacoes_bancarias")
print('### Acessei Configuração da Conciliação Bancária')

error_message = navegador.find_elements(By.ID,"endereco_webservice")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_contas_correntes_colaboradores")
print('### Acessei Configuração da Conta Corrente do Colaborador')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_correntes_colaboradores")
print('### Acessei Relatório de Conta Corrente do Colaborador')

error_message = navegador.find_elements(By.NAME,"filtros[valor_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controle_pdds")
print('### Acessei Controle de PDD')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_historicos_por_centro_custo")
print('### Acessei Relatório de Históricos por Centro de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_fechamentos_caixas")
print('### Acessei Relatório de Fechamento de Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[listar_por]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_lotes_cobrancas")
print('### Acessei Relatório de Cobranças - Lote')

error_message = navegador.find_elements(By.NAME,"filtros[numero_lotes_cobrancas]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_fechamentos_caixas")
print('### Acessei Conferência de Fechamento de Caixa Cego')

error_message = navegador.find_elements(By.NAME,"filtros[numero_lotes_cobrancas]")
if error_message:
    print("A página foi aberta")
else:
    #erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  SEM CONFIGURAÇÃO DE CAIXA CEGO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_inadimplencias")
print('### Acessei Relatório de Inadimplência')

error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_receber_exportacoes")
print('### Acessei Relatório Contas a Receber - Exportação')

error_message = navegador.find_elements(By.NAME,"filtros[periodo_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_exportacoes_contas_receber")
print('### Acessei Configuração Exportação Contas a Receber')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/documentos_integracoes_financeiras")
print('### Acessei Integração Financeira')

error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_financeiras")
print('### Acessei Conta Financeira')

error_message = navegador.find_elements(By.NAME,"filtros[codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conciliacoes_cartoes")
print('### Acessei Conciliação de Cartão')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_recebimentos")
print('### Acessei Recebimentos de Caixa Aguardando Integração - DJPDV')

error_message = navegador.find_elements(By.NAME,"filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/status_conferencias_itens_cobrancas")
print('### Acessei Status das Conferências dos Lotes de Cobrança')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_juros_previstos_cobrados")
print('### Acessei Relatório de Juros Previstos X Juros Cobrados')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_lancamentos_creditos")
print('### Acessei Relatório Lançamentos de Créditos')

error_message = navegador.find_elements(By.NAME,"filtros[periodo_inclusao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/lotes_cobrancas")
print('### Acessei Lotes de Cobranças')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fechamentos_caixas_analiticos")
print('### Acessei Fechamento de Caixa - Analítico')

error_message = navegador.find_elements(By.NAME,"filtros[data_fechamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_extrato_movimentacoes")
print('### Acessei Relatório Extrato de Movimentações')

error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_caixas")
print('### Acessei Relatório de Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_cheques")
print('### Acessei Relatório de Cheques')

error_message = navegador.find_elements(By.NAME,"filtros[bom_para_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_transferencias_caixas")
print('### Acessei Conferência de Transferência de Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cheques")
print('### Acessei Controle de Cheques')

error_message = navegador.find_elements(By.NAME,"filtros[bom_para_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fechamentos_caixas")
print('### Acessei Fechamento de Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[data_fechamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/lancamentos_creditos")
print('### Acessei Lançamentos de Créditos')

error_message = navegador.find_elements(By.ID,"autocompletar_filtro_nome")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_saldos")
print('### Acessei Consulta Saldos')

error_message = navegador.find_elements(By.NAME,"conta_caixa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_caixas")
print('### Acessei Movimentações de Caixa')

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

error_message = navegador.find_elements(By.NAME,"filtros[titulos.numero_titulo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transferencias")
print('### Acessei Transferências de Caixa')

error_message = navegador.find_elements(By.NAME,"transferencia[transferencias][0][valor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recebimentos")
print('### Acessei Recebimentos')

error_message = navegador.find_elements(By.ID,"autocompletar_cliente_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/responsaveis_cobrancas")
print('### Acessei Responsável pela Cobrança')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_integracoes_bancarias")
print('### Acessei Configuração da Integração Bancária')

error_message = navegador.find_elements(By.ID,"autocompletar_banco_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_receitas_despesas")
print('### Acessei Histórico de Receita e Despesa')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subgrupos_historicos_rd")
print('### Acessei Subgrupos de Históricos de Receitas e Despesas')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_historicos_rd")
print('### Acessei Grupos de Históricos de Receitas e Despesas')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_caixas_usuarios")
print('### Acessei Conta Caixa por Usuário')

error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_por_ncm")
print('### Acessei Relatório de Documentos de Saída por NCM')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_difal")
print('### Acessei Relatório DIFAL')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_entregas_futuras")
print('### Acessei Relatório de Entrega Futura')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_entregas_montagens")
print('### Acessei Relatório de Entrega e Montagem')

error_message = navegador.find_elements(By.ID,"autocompletar_pessoas.id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_tickets_medios_vendas")
print('### Acessei Relatório Ticket Médio de Vendas')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_assistencia_tecnica")
print('### Acessei Relatório de Assistência Técnica')

error_message = navegador.find_elements(By.NAME,"filtros[data_abertura_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_movimentacoes_assistencias_tecnicas")
print('### Acessei Tipo de Movimentação da Assistência Técnica')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/formas_pagamentos")
print('### Acessei Forma de Pagamento')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_operacoes_documentos")
print('### Acessei Grupo de Operação')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/operacoes_documentos")
print('### Acessei Operação')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/operacoes_documentos_usuarios")
print('### Acessei Operações do Usuário')

error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendedores")
print('### Acessei Vendedor')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/formas_pagamentos_contas_caixas")
print('### Acessei Formas de Pagamento por Conta Caixa')

error_message = navegador.find_elements(By.ID,"autocompletar_forma_pagamento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_caixas")
print('### Acessei Conta Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_caixas")
print('### Acessei Tipo de Conta Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/multas")
print('### Acessei Multa')

error_message = navegador.find_elements(By.NAME,"filtros[quantidade_dias_carencia_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_movimentacoes_titulos")
print('### Acessei Histórico de Movimentação de Título')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/portadores_titulos")
print('### Acessei Portador de Título')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_portadores_titulos")
print('### Acessei Tipo de Portador de Título')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_titulos")
print('### Acessei Tipo de Título')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_correntes")
print('### Acessei Conta Corrente')

error_message = navegador.find_elements(By.NAME,"filtros[bancos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/agencias")
print('### Acessei Agência')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/bancos")
print('### Acessei Banco')

error_message = navegador.find_elements(By.NAME,"filtros[codigo_banco_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_evolucoes_inadimplencias")
print('### Acessei Relatório de Evolução da Inadimplência')

error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_renegociacoes_dividas")
print('### Acessei Relatório de Renegociações de Dívidas')

error_message = navegador.find_elements(By.NAME,"filtros[data_renegociacao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_cobranca")
print('### Acessei Relatório de Cobranças')

error_message = navegador.find_elements(By.NAME,"filtros[data_agendamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_receber_cobrancas")
print('### Acessei Relatório de Contas a Receber - Cobrança')

error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_clientes")
print('### Acessei Relatório Razão de Clientes')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_receber")
print('### Acessei Relatório Contas a Receber')

error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_pagar")
print('### Acessei Relatório Contas a Pagar')

error_message = navegador.find_elements(By.NAME,"filtros[data_vencimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_bancarias")
print('### Acessei Integração Bancária')

error_message = navegador.find_elements(By.NAME,"conta_caixa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/convenios")
print('### Acessei Convênio Bancário')

error_message = navegador.find_elements(By.NAME,"filtros[bancos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cartas_cobrancas")
print('### Acessei Impressões para Cobrança')

error_message = navegador.find_elements(By.NAME,"filtros[cliente_cpf]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fluxos_caixas")
print('### Acessei Relatório de Fluxo de Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[exibicao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/limites_creditos")
print('### Acessei Controle de Crédito (Financeiro)')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/renegociacoes_dividas")
print('### Acessei Renegociação de Dívida')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cobrancas")
print('### Acessei Controle de Cobrança')

error_message = navegador.find_elements(By.NAME,"filtros[cobrancas.id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_financeira")
print('### Acessei Consulta Financeira')

error_message = navegador.find_elements(By.ID,"autocompletar_cliente_fornecedor_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_titulos")
print('### Acessei Movimentação de Título')

error_message = navegador.find_elements(By.ID,"autocompletar_filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/titulos")
print('### Acessei Título')

error_message = navegador.find_elements(By.NAME,"filtros[numero_titulo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ncms_consultas_apis")
print('### Acessei Consultar NCM')

error_message = navegador.find_elements(By.NAME,"filtros[codigo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_moradias")
print('### Acessei Tipo de Moradia')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_integracoes_financeiras")
print('### Acessei Tabela de Integração Financeira')

error_message = navegador.find_elements(By.ID,"autocompletar_forma_pagamento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_fcp")
print('### Acessei Definição para FCP')

error_message = navegador.find_elements(By.NAME,"filtros[ufs.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/intermediadores")
print('### Acessei Intermediador')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/intermediadores")
print('### Acessei Intermediador')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_pagamentos_filiais")
print('### Acessei Configuração de Pagamentos por Filial')

error_message = navegador.find_elements(By.NAME,"configuracao[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/colaboradores")
print('### Acessei Colaborador')

error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/colaboradores")
print('### Acessei Colaborador')

error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_creditos_aproveitamentos_icms")
print('### Acessei Definição de Créditos de ICMS')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_financeiras")
print('### Acessei Log de Integração Financeira')

error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_sistemas")
print('### Acessei Auditoria')

error_message = navegador.find_elements(By.NAME,"filtros[mensagem]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/equipes_montagens")
print('### Acessei Equipe de Montagem')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_cst_icms_efetivos")
print('### Acessei Definição de CST Efetivo')

error_message = navegador.find_elements(By.NAME,"filtros[cst_icms.numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/motoristas")
print('### Acessei Motorista')

error_message = navegador.find_elements(By.NAME,"filtros[cpf]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/codigos_beneficios_fiscais")
print('### Acessei Definição de Código de Benefício Fiscal')

error_message = navegador.find_elements(By.NAME,"filtros[codigo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/composicoes_valores")
print('### Acessei Composição de Valores')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_transferencias_financeiras_clientes")
print('### Acessei Log de Transferências Financeiras de Clientes')

error_message = navegador.find_elements(By.NAME,"filtros[nome_pessoa_origem_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_cobrancas_usuarios_perfis")
print('### Acessei Configuração de Cobrança por Usuário/Perfil')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atributos_formas_pagamentos")
print('### Acessei Configuração de Formas Pagamentos - Atributos da Pessoa')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ncm_codigos_especificadores_st")
print('### Acessei Configuração de CEST com NCM')

error_message = navegador.find_elements(By.NAME,"filtros[codigos_especificadores_st.numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_economicos")
print('### Acessei Grupo Econômico')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/veiculos")
print('### Acessei Veículo')

error_message = navegador.find_elements(By.NAME,"filtros[motoristas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_recebimentos_filiais")
print('### Acessei Configuração de Recebimento por Filial')

error_message = navegador.find_elements(By.NAME,"configuracao[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_notificacoes")
print('### Acessei Controle de Notificação')

error_message = navegador.find_elements(By.NAME,"filtros[perfil_descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_horarios")
print('### Acessei Definição de Horário')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/centros_custos")
print('### Acessei Centro de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_vendas")
print('### Acessei Configuração de Liberação')

error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_reducoes")
print('### Acessei Configurações de Reduções')

error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_fornecedor_id_0")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_ibpt")
print('### Acessei Consulta IBPT')

error_message = navegador.find_elements(By.ID,"autocompletar_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transferencias_financeiras_clientes")
print('### Acessei Transferências Financeiras de Clientes')

error_message = navegador.find_elements(By.ID,"autocompletar_pessoa_origem_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_situacoes")
print('### Acessei Históricos de Alterações de Situações')

error_message = navegador.find_elements(By.NAME,"filtros[historicos_situacoes.created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fluxos_situacoes")
print('### Acessei Fluxos das Situações')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/categorias_historicos_contatos_crm")
print('### Acessei Categorias de Históricos de Contatos (CRM)')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_documentos")
print('### Acessei Importação de Documentos')

error_message = navegador.find_elements(By.ID,"nome_do_arquivo_arquivo")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_documentos")
print('### Acessei Exportação de Documentos')

error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/representantes")
print('### Acessei Representante')

error_message = navegador.find_elements(By.NAME,"filtros[representantes.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/compradores")
print('### Acessei Comprador')

error_message = navegador.find_elements(By.NAME,"filtros[compradores.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_despesas_variaveis")
print('### Acessei Despesas Variáveis')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_despesas_variaveis")
print('### Acessei Tipos de Despesas Variáveis')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cte")
print('### Acessei CT-e')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transportadores")
print('### Acessei Transportador')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/montadores")
print('### Acessei Montadores')

error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_dre")
print('### Acessei Configurações de DRE')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/dias_uteis")
print('### Acessei Definição de Dias Úteis')

error_message = navegador.find_elements(By.NAME,"filtros[data_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conversoes")
print('### Acessei Tabela de Conversões para Importação de XML')

error_message = navegador.find_elements(By.ID,"autocompletar_entrada_id_cfop_cfop_0")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contadores")
print('### Acessei Contador')

error_message = navegador.find_elements(By.NAME,"filtros[contadores.crc_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_nf")
print('### Acessei Configuração NF')

error_message = navegador.find_elements(By.NAME,"filtros[filiais.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/modelos_nf_filiais")
print('### Acessei Modelo de NF por Filial')

error_message = navegador.find_elements(By.NAME,"modelo_nf_filial[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/modelos_nf")
print('### Acessei Modelo de NF')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/programas_usuarios")
print('### Acessei Programas do Usuário')

error_message = navegador.find_elements(By.ID,"autocompletar_usuario")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/perfis_usuarios")
print('### Acessei Perfil do Usuário')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/usuarios")
print('### Acessei Usuário')

error_message = navegador.find_elements(By.ID,"pessoas.nome_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/filiais")
print('### Acessei Filial')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.cpf_cnpj_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/codigos_especificadores_st")
print('### Acessei CEST')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cfop")
print('### Acessei CFOP')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_ipi")
print('### Acessei Código de Situação Tributária do IPI')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_cofins")
print('### Acessei Código de Situação Tributária do COFINS')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_pis")
print('### Acessei Código de Situação Tributária do PIS')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_icms_produtos_ncm")
print('### Acessei Código de Situação Tributária do ICMS por Produto/NCM')

error_message = navegador.find_elements(By.NAME,"filtros[ufs_origem.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_icms_ufs")
print('### Acessei Código de Situação Tributária do ICMS por UF')

error_message = navegador.find_elements(By.NAME,"filtros[cst_icms.numero]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_especificas")
print('### Acessei Definição de CST Específico')

error_message = navegador.find_elements(By.NAME,"filtros[operacoes_documentos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cst_icms")
print('### Acessei Código de Situação Tributária do ICMS')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ncm")
print('### Acessei NCM')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/itens_ncm")
print('### Acessei Item de NCM')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subposicoes_dois_ncm")
print('### Acessei Subposições II de NCM')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subposicoes_um_ncm")
print('### Acessei Subposições I de NCM')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/posicoes_ncm")
print('### Acessei Posição de NCM')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/capitulos_ncm")
print('### Acessei Capítulo de NCM')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_enderecos")
print('### Acessei Tipo de Endereço')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ceps")
print('### Acessei CEP')

error_message = navegador.find_elements(By.NAME,"filtros[cep_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/bairros")
print('### Acessei Bairro')

error_message = navegador.find_elements(By.NAME,"filtros[bairros.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cidades")
print('### Acessei Cidade')

error_message = navegador.find_elements(By.NAME,"filtros[cidades.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ufs")
print('### Acessei UF')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/paises")
print('### Acessei País')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_romaneios_filiais")
print('### Acessei Visibilidade de Romaneio de Separação por Filial')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_aprovacoes_classificacoes_riscos")
print('### Acessei Configuração para Aprovação de Análise de crédito - Risco')

error_message = navegador.find_elements(By.NAME,"configuracoes_aprovacoes_classificacoes_riscos[0][classificacao_risco]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_romaneios_montagens_filiais")
print('### Acessei Visibilidade de Romaneio de Montagem por Filial')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_analises_creditos")
print('### Acessei Integração Análise de Crédito')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/classificacoes_riscos")
print('### Acessei Classificação de Risco - Análise de Crédito')

error_message = navegador.find_elements(By.NAME,"filtros[risco]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_integracoes_analises_creditos")
print('### Acessei Configuração de Integração para Análise de Crédito')

error_message = navegador.find_elements(By.NAME,"filtros[tipo_integracao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consultas_precos")
print('### Acessei Consulta de Preços')

error_message = navegador.find_elements(By.ID,"autocompletar_produto_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/competencias_documentos")
print('### Acessei Competências - Documentos')

error_message = navegador.find_elements(By.NAME,"filtros[numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_aprovacoes_analises_creditos")
print('### Acessei Configuração para Aprovação de Análise de créditos')

error_message = navegador.find_elements(By.NAME,"configuracoes_aprovacoes_analises_creditos[0][configuracoes_aprovacoes_analises_creditos_papeis_aprovacoes_attributes[0][papel_aprovacao_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_produtos")
print('### Acessei Visibilidade de Produtos por Usuário')

error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_atingimentos_metas_recebimentos")
print('### Acessei Relatório de Comissão por Atingimento de Meta - Recebimento')

error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_vendedores_descontos")
print('### Acessei Relatório de Comissão dos Vendedores - Desconto')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_descontos")
print('### Acessei Controle de Comissão - Desconto Venda')

error_message = navegador.find_elements(By.NAME,"definicao_comissao_desconto[itens_definicoes_comissoes_descontos_attributes][0][escopo][escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_creditos")
print('### Acessei Relatório de Análise de Crédito')

error_message = navegador.find_elements(By.NAME,"filtros[analises_creditos.created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_titulos")
print('### Acessei Visibilidade de Títulos por Usuário')

error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_renegociacoes_pendentes")
print('### Acessei Configuração de Liberação de Renegociações Pendentes')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_analises_creditos_usuarios")
print('### Acessei Visibilidade de Análise de Crédito por Usuário')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas_canais_vendas")
print('### Acessei Relatório de Análise de Vendas - Canal de Venda')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_emissoes_documentos_saidas")
print('### Acessei Configuração Emissão Documento de Saída no Caixa')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sequencias_tipos_custos")
print('### Acessei Sequência do Tipo de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_descontos_recebimentos")
print('### Acessei Desconto - Recebimento Por Nível de Aprovação')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_crm")
print('### Acessei Relatório CRM')

error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_operacoes_filiais")
print('### Acessei Visibilidade de Operação Por Filial')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_ordens_servicos")
print('### Acessei Visibilidade de Assistência Técnica')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_clientes_inadimplentes")
print('### Acessei Configuração de Liberação de Clientes Inadimplentes')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_tempos_medios_atendimentos")
print('### Acessei Definição Tempo Médio Atendimento')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_registros_spc")
print('### Acessei Relatório de Registros do SPC')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/registros_positivacoes_spc")
print('### Acessei Registro de Positivação do SPC')

error_message = navegador.find_elements(By.NAME,"filtros[numero_contrato]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/registros_negativacoes_spc")
print('### Acessei Registro de Negativação do SPC')

error_message = navegador.find_elements(By.NAME,"filtros[numero_contrato]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_registros_spc")
print('### Acessei Históricos de Registros do SPC')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simulacoes_precos")
print('### Acessei Simulação de Preço')

error_message = navegador.find_elements(By.ID,"autocompletar_produto_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_consultas_spc")
print('### Acessei Históricos de Consulta SPC')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/historicos_consultas_spc")
print('### Acessei Históricos de Consulta SPC')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_papeis_usuarios")
print('### Acessei Configuração de Papel de Aprovação por Usuário')

error_message = navegador.find_elements(By.NAME,"filtros[validade_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_niveis_tipos_liberacoes")
print('### Acessei Configuração de Nível por Tipo de Liberação')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/niveis_aprovacoes")
print('### Acessei Nível de Aprovação')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/papeis_aprovacoes")
print('### Acessei Papel de Aprovação')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/desvinculos_documentos_devolucoes")
print('### Acessei Desvínculo de Documentos de Devolução')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas_tabelas_precos")
print('### Acessei Relatório de Análise de Vendas Entre Tabelas de Preços')

error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_percentuais_atingimentos_tabelas_precos")
print('### Acessei Definição de Percentual de Atingimento por Tabela de Preço')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controles_comissoes_formas_pagamentos")
print('### Acessei Controle de Comissão por Forma de Pagamento')

error_message = navegador.find_elements(By.ID,"autocompletar_forma_pagamento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_formas_pagamentos_vendedores")
print('### Acessei Relatório de Comissão por Forma de Pagamento - Vendedor')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_visibilidades_documentos_filiais")
print('### Acessei Visibilidade de Documentos por Filial')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_clientes_sem_movimento")
print('### Acessei Relatório de Clientes sem Movimento')

error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_movimentacoes_financeiras")
print('### Acessei Relatório de Movimentação Financeira por Conta Caixa')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas_produtos")
print('### Acessei Relatório de Análise de Vendas - Totalizadas por Produto')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/visibilidades_estoques_filiais")
print('### Acessei Visibilidade de Estoque por Filial')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_vendas")
print('### Acessei Relatório de Análise de Vendas - Composição de Comissão')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_metas")
print('### Acessei Relatório de Análise de Meta')

error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/descontos_recebimentos")
print('### Acessei Desconto - Recebimento')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_atingimentos_metas")
print('### Acessei Relatório de Comissão por Atingimento de Meta')

error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_metas_totais")
print('### Acessei Configuração de Atingimento de Meta')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_contabeis")
print('### Acessei Exportação Contábil')

error_message = navegador.find_elements(By.NAME,"exportacao_contabil[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_contabilidades_empresas")
print('### Acessei Definição de Contabilidade por Empresa')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_integracoes_contabeis")
print('### Acessei Configuração de Integração Contábil')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_cobrancas")
print('### Acessei Relatório de Comissão por Cobrança - Lote')

error_message = navegador.find_elements(By.NAME,"filtros[data_pagamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_cobrancas")
print('### Acessei Controle de Comissão por Cobrança')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/comissoes_metas")
print('### Acessei Comissão por Meta')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_recebimentos")
print('### Acessei Relatório de Comissão por Recebimento')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_profissionais")
print('### Acessei Tipo de Profissional')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/profissionais")
print('### Acessei Profissional')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_tabelas_precos")
print('### Acessei Tipo de Tabela de Preço')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_pedidos_compras")
print('### Acessei Tipo de Pedido de Compra')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pdv/configuracoes_integracoes")
print('### Acessei Configuração de Integração com PDV')

error_message = navegador.find_elements(By.NAME,"token")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/orcamento/campanhas_marketings")
print('### Acessei Canal de Venda')

error_message = navegador.find_elements(By.NAME,"filtros[descricao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/justificativas")
print('### Acessei Justificativa')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sugestoes_observacoes")
print('### Acessei Observações')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_series_ecf")
print('### Acessei Configuração de Série de ECF')

error_message = navegador.find_elements(By.NAME,"filtros[numero_serie_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/informacoes_complementares_documentos")
print('### Acessei Informações Complementares do Documento')

error_message = navegador.find_elements(By.NAME,"filtros[mensagem_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_totais_vendas")
print('### Acessei Relatório de Análise de Vendas')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tef/tokens_filiais_usuarios")
print('### Acessei Configuração TEF por Filial/Usuário')

error_message = navegador.find_elements(By.NAME,"filtros[filiais.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tef/consultas")
print('### Acessei Consulta de Transações via TEF')

error_message = navegador.find_elements(By.ID,"autocompletar_usuario_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sat/configuracoes_integracoes")
print('### Acessei Configuração de Integração PDV/SAT')

error_message = navegador.find_elements(By.NAME,"configuracao_integracao_sat[][filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_servicos")
print('### Acessei Relatório de Serviços')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_liberacoes_analises_creditos")
print('### Acessei Configuração de Liberação Para Análise de Crédito')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_demonstracoes_produtos")
print('### Acessei Relatório de Demonstração de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[numero_demonstracao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_recebimentos")
print('### Acessei Controle de Comissão por Recebimento')

error_message = navegador.find_elements(By.NAME,"percentual_comissao_empresa")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes_montadores")
print('### Acessei Controle de Comissão de Montagem')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_comissoes")
print('### Acessei Controle de Comissão')

error_message = navegador.find_elements(By.NAME,"definicao_comissao[itens_definicoes_comissoes][-1][percentual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_aniversariantes")
print('### Acessei Relatório de Aniversariantes')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_controles_profissionais")
print('### Acessei Relatório do Controle de Profissionais')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_tir")
print('### Acessei Relatório de TIR')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_margem_contribuicao")
print('### Acessei Relatório de Margem de Contribuição')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_margens_brutas")
print('### Acessei Relatório de Margem Bruta')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_montadores")
print('### Acessei Relatório de Comissão dos Montadores')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_alteracoes_produtos")
print('### Acessei Relatório de Alterações de Preço do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_metas")
print('### Acessei Relatório de Comissão por Meta')

error_message = navegador.find_elements(By.ID,"autocompletar_meta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_comissoes_vendedores")
print('### Acessei Relatório de Comissão dos Vendedores')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/analises_creditos")
print('### Acessei Análise de Crédito')

error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contatos_crm")
print('### Acessei Contatos (CRM)')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/markup")
print('### Acessei Markup')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/liberacoes_vendas")
print('### Acessei Liberação')

error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/margens_contribuicoes")
print('### Acessei Recálculo da Margem de Contribuição')

error_message = navegador.find_elements(By.ID,"autocompletar_filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_margens_contribuicoes")
print('### Acessei Configuração da Margem de Contribuição')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_tir")
print('### Acessei Definição de TIR')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_descontos")
print('### Acessei Controle de Desconto - Venda')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/metas")
print('### Acessei Controle de Meta')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_descontos_fornecedores")
print('### Acessei Definições de Descontos por Fornecedores')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestao_precos")
print('### Acessei Gestão de Preço')

error_message = navegador.find_elements(By.NAME,"tabela_preco_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_precos_fornecedores")
print('### Acessei Tabela de Preço por Fornecedor')

error_message = navegador.find_elements(By.NAME,"tabela_preco_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_precos")
print('### Acessei Tabela de Preço')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_bonificacoes")
print('### Acessei Definição de Bonificação')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/paineis_gerenciais")
print('### Acessei Painel Gerencial')

error_message = navegador.find_elements(By.NAME,"data_inicial")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/dre")
print('### Acessei DRE')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_financeira")
print('### Acessei Relatório de Documentos de Saída - Financeira')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_orcamentos")
print('### Acessei Tipo de Orçamento')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_devolucoes_vendas_ce")
print('### Acessei Configuração de Liberação Devolução de Venda com Encomenda')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_liberacoes_devolucoes_vendas_se")
print('### Acessei Configuração de Liberação Devolução de Venda sem Encomenda')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_montagens")
print('### Acessei Tabela de Montagem')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_fretes_entregas")
print('### Acessei Relatório de Fretes por Entrega')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simulacoes_vendas")
print('### Acessei Simulação de Venda')

error_message = navegador.find_elements(By.ID,"forma_pagamento_id_0")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_liberacoes_prorrogacoes_parcelas")
print('### Acessei Configuração Liberação Prorrogação do Primeiro Vencimento')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/mdfe")
print('### Acessei MDF-e')

error_message = navegador.find_elements(By.NAME,"filtros[numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/autorizacoes_pagamentos")
print('### Acessei Autorização de Pagamento')

error_message = navegador.find_elements(By.NAME,"filtros[fornecedor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_definicoes_tributacoes_produtos")
print('### Acessei Consulta definições de tributação de produtos')

error_message = navegador.find_elements(By.ID,"pesquisar_produto")
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
print("-------------------------------------")
print("Robô iniciado em ", hora_inicio,'\n' "Robô finalizado em ", hora_fim, '\n' "Tempo de execução", tempo_total, '\n' "Quantidade de telas verificadas", cont, '\n' "Telas com erro", erro )


navegador.quit()
