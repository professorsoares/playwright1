# https://www.zyte.com/join-community/

# https://www.youtube.com/watch?v=CK6MWehq7vI

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.zyte.com/join-community/")

    page.wait_for_timeout(5000)

    #    loginLink = page.query_selector("[href='/login']")
    #    loginLink.click()


    checkCookies = page.query_selector('[id="onetrust"]')
    try:
        page.wait_for_selector(checkCookies, timeout=2000)
        if checkCookies:
            checkCookies.click()
    except:
        print("nada feito....")

    lastname = page.query_selector('[name="lastname"]')
    try:
        page.wait_for_selector(lastname, timeout=2000)
        if lastname:
            lastname.type("Soares")
    except:
        print("nada feito....")
    #    camposenha = page.query_selector('[id="password"]')
    #    camposenha.type("teste")

    #    enviar = page.query_selector('//input[type="submit"]')
    #       enviar.click()



    page.wait_for_timeout(5000)


    browser.close()