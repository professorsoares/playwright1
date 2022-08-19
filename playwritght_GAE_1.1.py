# https://www.youtube.com/watch?v=CK6MWehq7vI
# pandas, openpyxl


from tkinter import Frame
from playwright.sync_api import sync_playwright
import pandas as pd
import time
import pyautogui as pagui
import pyperclip
from datetime import datetime

import senhas
# import pyperclip
# import platform
#

inicio = datetime.today().strftime('%d/%m/%Y %H:%M:%S:%f')
print(f"INICIO:  {inicio}")

df = pd.read_excel(r"C:\git\playwright1\dadosValeSocial.xlsx", engine='openpyxl')

################################################ DEFINIÇÕES ################################################


# nome  = "bruno.soares"
nome = senhas.loginAline
senha = senhas.senhaAline
abaPlanilha = senhas.planilhaAline
strMail = "@extreme.digital"

tarefa = "https://gae.extremedigital.com.br/portal/"
linkLancamentos = "https://gae.extremedigital.com.br/gae-web/pages/apropriacao-esforco"
linkPagina = "https://login.microsoftonline.com/"

f = '%d/%m/%Y %H:%M:%S:%f'

MODO_DEBUG = True
############################################################################################################

def type(text):
    pyperclip.copy(text)
    pagui.hotkey("ctrl", "v")


def abrePagina(linkPagina, linkLancamentos):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Abre a página inicial do GAE
        # page.goto(tarefa)
        page.goto(linkPagina)
        time.sleep(4)

        lancaDados(page, linkLancamentos)
        fazLogin(page, nome, strMail, senha)
        return page, browser


def fazLogin(page, nome, strMail, senha):
    if MODO_DEBUG: print("----------------------------------------------")


    #pagui.press('tab')
    time.sleep(2)
    pagui.press('tab')
    pagui.press('enter')
    time.sleep(2)

    # Digita o login e senha.
    pagui.write(nome + strMail, interval=0.10)
    pagui.press('enter')
    time.sleep(2)
    # pagui.write(senha, interval=0.20)
    type(senha)

    time.sleep(5)
    pagui.press('enter')
    time.sleep(2)

    print("LOGOU")
    # Aperta Enter quando aparece a mensagem.
    #time.sleep(4)
    #pagui.press('enter')
    #time.sleep(4)


def lancaDados(page, linkLancamentos):
    print("ENTROU LANÇA")
    # Vai para a página sem o Frame

    time.sleep(4)
    page.goto(linkLancamentos)
    time.sleep(4)

    # Preenche a data
    page.fill('#data', '01/06/2022')
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

def finalizaTudo(browser):
    browser.close()

page, browser = abrePagina(linkPagina, linkLancamentos)
#fazLogin(page, nome, strMail, senha)
#lancaDados(page, linkLancamentos)
finalizaTudo(browser)
