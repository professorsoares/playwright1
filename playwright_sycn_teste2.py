
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto("https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-fiction/")
    page.goto('https://sites.google.com/testleaf.com/ruto')
    # articles = page.locator("ol[data-testid='topic-llist']")
    # Click on <div> "FIND XPATH AND LOCATORS"
    page.click('#h\.p_4T6kRobPprIC_l > .CjVfdc')
    print(page.locator("h1").all_inner_texts())
    #browser.close()
