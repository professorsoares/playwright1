# https://www.youtube.com/watch?v=CK6MWehq7vI
# pandas, openpyxl


from tkinter import Frame

from numpy.f2py.auxfuncs import throw_error
from playwright.sync_api import sync_playwright
import pandas as pd
import time
import pyautogui as pagui
import pyperclip
from datetime import datetime

# import pyperclip
from websockets import exceptions

import senhas

################################################ DEFINIÇÕES ################################################

# nome  = "bruno.soares"
nome = senhas.loginAline
senha = senhas.senhaAline
abaPlanilha = senhas.planilhaAline
strMail = "@extreme.digital"

linkPortalGAE = "https://gae.extremedigital.com.br/portal/"
linkLancamentoPonto = "https://gae.extremedigital.com.br/gae-web/pages/apropriacao-esforco"
linkPaginaMS = "https://login.microsoftonline.com/"

f = '%d/%m/%Y %H:%M:%S:%f'

MODO_DEBUG = True
############################################################################################################

inicio = datetime.today().strftime('%d/%m/%Y %H:%M:%S:%f')
print(f"INICIO:  {inicio}")


df = pd.read_excel(r"./Lançamento_Horas_Equipe - Junho22.xlsx",
                   engine='openpyxl',
                   date_parser='Data',
                   sheet_name=abaPlanilha
                   )

# Pega os dados para o GAE.
dfGAE = df[["Projeto GAE", "Cliente", "Descrição", "Data", "Horas", "Lancado"]]
dfGAE = dfGAE.loc[dfGAE["Lancado"] == "Não"].sort_values(by=['Data'])

def type(text):
    pyperclip.copy(text)
    pagui.hotkey("ctrl", "v")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Abre a página inicial do GAE
    # page.goto(tarefa)
    page.goto(linkPaginaMS)
    time.sleep(4)

# ---------------------------------------------------------------------
# FAZ LOGIN:

    if MODO_DEBUG: print("----------------------------------------------")

    #pagui.press('tab')
    time.sleep(2)
    print("Click_CANCEL")
    # try:
    #     page.click('//*[@id="desktopSsoCancel"]')
    # except Exception as e:
    #     print("NÃO CANCELOU")
    pagui.press('tab')
    pagui.press('enter')

    # Digita o login e senha.
    #pagui.write(nome + strMail, interval=0.10)
    # time.sleep(4)
    print("LOGIN")

    try:
        page.fill("loginfmt", nome + strMail)
    except Exception as e:
        print('Failed_001: ' + str(e))

    try:
        page.query_selector("loginfmt").fill(nome + strMail)
    except Exception as e:
        print('Failed_002: ' + str(e))

    try:
        # Clica no Botão Adicionar.
        element = page.query_selector('loginfmt')
        if(element):
            element.fill(nome + strMail)
            print("TUDO OK")
        else:
            print("DEU RUIM MAS VAI")
            pagui.write(nome + strMail, interval=0.10)

    except Exception as e:
        print('==> Failed_003: ' + str(e))
        pagui.write(nome, interval=0.10)
        time.sleep(20)

    #pagui.press('enter')
    print("CLICOU 01")
    time.sleep(1)

    try:
        page.click("#idSIButton9")
    except Exception as e:
        print('==> Failed_004: ' + str(e))
        print('CLICA NO ENVIAR LOGIN')

    time.sleep(20)

    print("SENHA")
    pagui.write(senha, interval=0.20)
    type(senha)

    time.sleep(20)
    pagui.press('enter')
    time.sleep(2)

    print("LOGOU")
    # Aperta Enter quando aparece a mensagem.
    time.sleep(2)
    pagui.press('enter')


# ---------------------------------------------------------------------
# LANÇA DADOS:

    time.sleep(4)
    page.goto(linkLancamentoPonto)
    print("ENTROU LANÇA")
    # Vai para a página sem o Frame
    time.sleep(4)


    for i in dfGAE.index:
        # Trata os dados:
        dataFormatada = str(dfGAE["Data"][i].strftime("%d/%m/%Y"))
        projeto = str(dfGAE["Projeto GAE"][i])
        cliente = str(dfGAE["Cliente"][i])
        descricao = str(dfGAE["Descrição"][i])
        if str(dfGAE["Horas"][i]).split(".").__len__() == 2:
            esforcoHora = ("0"+str(dfGAE["Horas"][i]).split(".")[0])[slice(2)]
            esforcoMinuto = "30" if str(dfGAE["Horas"][i]).split(".")[1] == "5" else "00"
        else:
            raise Exception("ESFORÇO NÃO ENCONTRADO! VERIFIQUE A PLANILHA")

        print("ESFORÇO: " + esforcoHora + "-" + esforcoMinuto)
        print("->: " + projeto + "-" + cliente + "-" + dataFormatada)

        # Preenche a data
        page.fill('#data', dataFormatada)
        time.sleep(2)

        # Clica no Botão Adicionar.
        element = page.query_selector_all('a')
        for elem in element:
            if elem.inner_text() == "ADICIONAR":
                elem.click()
                elem.click()
        time.sleep(2)

        # Preenche o Cliente
        page.select_option("select#cliente", label=cliente)
        time.sleep(2)

        # Preenche o Projeto
        page.select_option("select#projeto", label=projeto)
        time.sleep(2)

        # Preenche o esforço
        page.fill('#esforco', esforcoHora + ":" + esforcoMinuto)
        time.sleep(2)

        # Preenche a Observação.
        page.fill('#observacao', descricao)
        time.sleep(2)

        # Clica no Salvar.
        page.locator("//span[contains(@class,'icon-save-outline')]").click()
        time.sleep(2)

    fim = datetime.today().strftime(f)
    print(f"FIM:  {fim}")

    dif = (datetime.strptime(fim, f) - datetime.strptime(inicio, f)).total_seconds()
    print(str(dif / 60))

    browser.close()
