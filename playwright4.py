# https://www.youtube.com/watch?v=CK6MWehq7vI

from playwright.sync_api import sync_playwright
import pandas as pd

df = pd.read_excel("DadosRH.xlsx")
print(df)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://quotes.toscrape.com/")
    heading_title = "//h1/a"
    heading = page.query_selector(heading_title)

    print(heading.inner_text())
    lstQuadrados = page.query_selector_all("[class='quote']")

    print(len(lstQuadrados))

    page.goto("http://quotes.toscrape.com/")

    import time

    time.sleep(3)

    loginLink = page.query_selector("[href='/login']")
    loginLink.click()

    campologin = page.query_selector('[id="username"]')
    campologin.type("Bruno")

    camposenha = page.query_selector('[id="password"]')
    camposenha.type("teste")

    enviar = page.query_selector('[type="submit"]')
    enviar.click()



    page.wait_for_timeout(2000)


    browser.close()