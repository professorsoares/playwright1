# https://www.youtube.com/watch?v=CK6MWehq7vI
# pandas, openpyxl


from tkinter import Frame
from playwright.sync_api import sync_playwright
import pandas as pd
import time
import pyautogui as pagui
import pyperclip
from datetime import datetime

# import pyperclip
# import platform
#
# def type(text: str):
# pyperclip.copy(text)
# pyautogui.hotkey("command", "v")

inicio = datetime.today().strftime('%d/%m/%Y %H:%M:%S:%f')
print(f"INICIO:  {inicio}")

df = pd.read_excel(r"C:\git\playwright1\dadosValeSocial.xlsx", engine='openpyxl')

################################################ DEFINIÇÕES ################################################

# nome  = "Deborah.mesquita"
# senha = '52Debs@52'
nome = "Bruno.soares"
strMail = "@extreme.digital"
senha = 'N@159Esp&7531'

tarefa = "https://gae.extremedigital.com.br/portal/"
tarefa2 = "https://gae.extremedigital.com.br/gae-web/pages/apropriacao-esforco"

f = '%d/%m/%Y %H:%M:%S:%f'

MODO_DEBUG = True
############################################################################################################
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Abre a página inicial do GAE
    page.goto(tarefa)
    time.sleep(4)

    if MODO_DEBUG: print("----------------------------------------------")

    # Digita o login e senha.
    pagui.write(nome + strMail, interval=0.10)
    pagui.press('enter')
    time.sleep(2)
    pagui.write(senha, interval=0.20)
    time.sleep(1)
    pagui.press('enter')
    time.sleep(2)

    # Aperta Enter quando aparece a mensagem.
    pagui.press('enter')
    time.sleep(4)

    # Vai para a página sem o Frame
    page.goto(tarefa2)
    time.sleep(4)

    # Preenche a data
    page.fill('#data', '01/04/2022')
    time.sleep(2)

    # Clica no Botão Adicionar.
    element = page.query_selector_all('a')
    for elem in element:
        if elem.inner_text() == "ADICIONAR":
            elem.click()
            elem.click()
    time.sleep(2)

    # Preenche o Cliente
    page.select_option("select#cliente", label="PRODERJ")
    time.sleep(2)

    # Preenche o Projeto
    page.select_option("select#projeto", label="0134_RJ_PRODERJ_MANT_REDHAT")
    time.sleep(2)

    # Preenche o esforço
    page.fill('#esforco', '08:00')
    time.sleep(2)

    # Preenche a Observação.
    page.fill('#observacao', 'Foco na demanda de requisito do RH')
    time.sleep(2)

    # Clica no Salvar.
    page.locator("//span[contains(@class,'icon-save-outline')]").click()
    time.sleep(2)

    fim = datetime.today().strftime(f)
    print(f"FIM:  {fim}")

    dif = (datetime.strptime(fim, f) - datetime.strptime(inicio, f)).total_seconds()
    print(str(dif / 60))