# https://www.youtube.com/watch?v=CK6MWehq7vI
# pandas, openpyxl


from playwright.sync_api import sync_playwright
import pandas as pd
import time
import pyautogui as pagui
import pyperclip

#
# import pyperclip
# import platform
#
# def type(text: str):
# pyperclip.copy(text)
# pyautogui.hotkey("command", "v")


df = pd.read_csv("DadosRH.csv", sep=";")
#, sheet_name=0, engine='openpyxl', index_col=0
#print(len(df))
#print((df.columns))

#
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://redmine.extremedigital.com.br/issues/63711/time_entries/new")
    time.sleep(5)

    pagui.press('tab')
    pagui.write('aline.nascimento', interval=0.10)
    pagui.press('tab')
    time.sleep(2)
    #pagui.write('', interval=0.20)
    time.sleep(10)
    pagui.press('enter')

    #page.goto("https://redmine.extremedigital.com.br/issues/63711/time_entries/new")
    time.sleep(4)
    heading_title = "//h1/span"
    heading = page.query_selector(heading_title)
    print("----------------------------------------------")
    print(heading.inner_text())
    print("----------------------------------------------")

    df = df[df.Nome == 'Aline']
    for i in df.index:
        time.sleep(2)
        pagui.press('tab')
        time.sleep(1)
        print("Total income in " + str(df["Nome"][i]))
        print("Data " + str(df["Data"][i]).replace("/", ""))
        pagui.write(str(df["Data"][i]).replace("/", ""), interval=0.30)

        time.sleep(1)
        pagui.press('tab')
        time.sleep(1)
        print("Horas " + str(df["Qtde_Horas"][i]).replace(",", "."))
        pagui.write(str(df["Qtde_Horas"][i]).replace(",", "."))

        time.sleep(1)
        pagui.press('tab')
        time.sleep(1)
        print("Texto " + str(df["Texto_Redmine"][i]))
        pyperclip.copy(str(df["Texto_Redmine"][i]))
        time.sleep(1)
        pagui.hotkey("ctrl", "v")
        #pagui.write(df["Texto_Redmine"][i])

        time.sleep(2)
        pagui.press('tab')
        time.sleep(1)
        pagui.write("Es")
        time.sleep(1)
        pagui.press('tab')
        time.sleep(1)
        pagui.press('tab')
        time.sleep(1)
        pagui.press('enter')
        print("FECHOU!!!!!!!")
        time.sleep(1)
        #break

    page.wait_for_timeout(2000)
    browser.close()

    #     # loginLink = page.query_selector("[href='/login']")
    #     # loginLink.click()
    #     #
    #     # campologin = page.query_selector('[id="username"]')
    #     # campologin.type("Bruno")
    #     #
    #     # camposenha = page.query_selector('[id="password"]')
    #     # camposenha.type("teste")
    #     #
    #     # enviar = page.query_selector('[type="submit"]')
    #     # enviar.click()
    #
    #
    #
    #     page.wait_for_timeout(2000)
    #     #
    #     #
    #     #     browser.close()