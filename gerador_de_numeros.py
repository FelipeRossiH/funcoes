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



print("Gerar 6 números aleatórios")

# Probabilidades dos números (você pode ajustar conforme necessário)
probabilidades = [1] * 25

cont = 0
numeros_gerados = []

while cont < 15:
    numero_gerado = random.choices(range(1, 26), k=1, weights=probabilidades)[0]

    # Garante que o número não foi escolhido anteriormente
    if numero_gerado not in numeros_gerados:
        numeros_gerados.append(numero_gerado)
        print("Número:", numero_gerado)
        cont += 1
