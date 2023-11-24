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

cont = 0
while cont < 6:
    # Considere as probabilidades da Mega-Sena
    numero_titulo_gerado = random.choices(range(1, 61), k=1, weights=[1]*60)[0]
    print("Número:", numero_titulo_gerado)
    cont += 1
