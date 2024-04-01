from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurações
contatos = ["Felipe SGI", "Gabi Amor"]  # Lista de contatos para enviar mensagem
mensagem = "Olá! Esta é uma mensagem de teste enviada pelo Python."  # Mensagem a ser enviada

# Inicializar o navegador
driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")
input("Escaneie o código QR do WhatsApp Web e pressione Enter para continuar...")

# Enviar mensagem para cada contato
for contato in contatos:
    try:
        # Encontrar o campo de pesquisa e enviar o nome do contato
        search_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(contato)
        time.sleep(2)  # Espera um pouco para o resultado da pesquisa ser carregado
        
        # Clicar no contato
        driver.find_element_by_xpath(f'//span[@title="{contato}"]').click()
        time.sleep(2)  # Espera um pouco para a conversa ser carregada
        
        # Encontrar o campo de mensagem e enviar a mensagem
        message_box = driver.find_element_by_xpath('//div[@class="_3uMse"][@contenteditable="true"][@data-tab="1"]')
        message_box.send_keys(mensagem)
        message_box.send_keys(Keys.ENTER)
        time.sleep(1)  # Espera um pouco antes de enviar a próxima mensagem
    except Exception as e:
        print(f"Erro ao enviar mensagem para {contato}: {str(e)}")

# Fechar o navegador
driver.quit()

print("Mensagens enviadas com sucesso!")
