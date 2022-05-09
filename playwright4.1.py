# https://www.youtube.com/watch?v=CK6MWehq7vI
#
#   USING LOCATOR INSTEAD OF QUERY_WELECTOR
#

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://quotes.toscrape.com/")

    heading_title = "//h1/a"
    heading = page.locator(heading_title)

    print(heading.inner_text())
    lstQuadrados = page.query_selector_all("[class='quote']")

    print(len(lstQuadrados))

    loginLink = page.locator("[href='/login']")
    loginLink.click()

    campologin = page.locator('[id="username"]')
    campologin.type("Bruno")

    camposenha = page.locator('[id="password"]')
    camposenha.type("teste")

    enviar = page.locator('[type="submit"]')
    enviar.click()



    page.wait_for_timeout(2000)


    browser.close()