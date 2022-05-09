# https://www.youtube.com/watch?v=CK6MWehq7vI
# pandas, openpyxl


from playwright.sync_api import sync_playwright
import pandas as pd
import time
import pyautogui as pagui
import pyperclip
from datetime import datetime

#
# import pyperclip
# import platform
#
# def type(text: str):
# pyperclip.copy(text)
# pyautogui.hotkey("command", "v")

inicio = datetime.today().strftime('%d/%m/%Y %H:%M:%S:%f')
print(f"INICIO:  {inicio}")

#df = pd.read_csv("DadosRH.csv", sep=";")

df = pd.read_excel(r"C:\git\playwright1\dadosValeSocial.xlsx", engine='openpyxl')

#, sheet_name=0, index_col=0
#print(len(df))
#print((df.columns))

################################################ DEFINIÇÕES ################################################

nome = "Deborah.mesquita"
# "Bruno.soares"
tarefa = "https://redmine.extremedigital.com.br/issues/55508/time_entries/new"

MODO_DEBUG = False
############################################################################################################
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(tarefa)
    time.sleep(4)

    pagui.press('tab')
    pagui.write(nome, interval=0.10)
    pagui.press('tab')
    time.sleep(1)
    pagui.write('52Debs@52', interval=0.20)
    time.sleep(2)
    pagui.press('enter')
    time.sleep(5)

    if MODO_DEBUG:
        heading_title = "//h1/span"
        heading = page.query_selector(heading_title)
        print("----------------------------------------------")
        print(heading.inner_text())
        print("----------------------------------------------")

    df = df[df.Nome == nome.split(".")[0]]
    df = df[df.Lancado != "s"]
    df.head(5)
    cont = 1
    for i in df.index:
        if i%7 == 0:
            time.sleep(3)
        cont +=1
        print("\nID: " + str(df["ID"][i]))
        print("CONT: " +str(cont))
        pagui.press('tab')
        time.sleep(1)
        print(f'Nome: {df["Nome"][i]} - Data:' + str((df["Data"]).dt.strftime('%d%m%Y')[i]))
        pagui.write(str((df["Data"]).dt.strftime('%d%m%Y')[i]), interval=0.30)
        if MODO_DEBUG: print("aki1")
        time.sleep(1)
        pagui.press('tab')
        print("Horas " + str(df["Qtde_Horas"][i]).replace(",", "."))
        pagui.write(str(df["Qtde_Horas"][i]).replace(",", "."))

        if MODO_DEBUG: print("aki2")
        time.sleep(1)
        pagui.press('tab')
        print("Texto " + str(df["Texto_Redmine"][i]))
        pyperclip.copy(str(df["Texto_Redmine"][i]))
        time.sleep(1)
        pagui.hotkey("ctrl", "v")

        if MODO_DEBUG: print("aki3")
        time.sleep(1)
        pagui.press('tab')
        time.sleep(1)
        pagui.write("Es")
        time.sleep(1)
        if MODO_DEBUG: print("aki4")
        pagui.press('tab')
        pagui.press('tab')
        time.sleep(1)
        if MODO_DEBUG: print("aki5")
        pagui.press('enter')
        print("FECHOU!!!!!!!")
        time.sleep(3)
        if MODO_DEBUG: print("aki6")

    page.wait_for_timeout(2000)
    browser.close()

fim = datetime.today().strftime('%d/%m/%Y %H:%M:%S:%f')
print(f"FIM:  {fim}")

f = '%d/%m/%Y %H:%M:%S:%f'
dif = (datetime.strptime(fim, f) - datetime.strptime(inicio, f)).total_seconds()
print(str(dif/60))