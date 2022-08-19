
import asyncio
from playwright.async_api import async_playwright
import time
import pyautogui as pagui

async def run(playwright):
    tag_selector = """
      {
          // Returns the first element matching given selector in the root's subtree.
          query(root, selector) {
              return root.querySelector(selector);
          },
          // Returns all elements matching given selector in the root's subtree.
          queryAll(root, selector) {
              return Array.from(root.querySelectorAll(selector));
          }
      }"""

    # Register the engine. Selectors will be prefixed with "tag=".
    await playwright.selectors.register("tag", tag_selector)
    browser = await playwright.chromium.launch(headless = False)
    page = await browser.new_page()
    linkPagina = "https://login.microsoftonline.com/"

    # await page.goto("https://gae.extremedigital.com.br/gae-web/pages/apropriacao-esforco")
    await page.goto("https://login.microsoftonline.com")
        #'<div id="teste"><button>Click me</button></div><div><button>Click me2</button></div>')

    print(await page.title())
    #strLogin = await page.query_selector("name=loginfmt").__getattribute__("text")
        # .inner_text( "bruno.soares@extreme.digital", 10, None)
    # ("1")

    await page.fill('loginfmt', 'bruno.soares@extreme.digital')

    print("ATÉ AQUI FOI")
    # Use the selector prefixed with its name.
    button = await page.query_selector('tag=button')
    # Combine it with other selector engines.
    #await page.click('tag=div >> text="Click me"')
    # Can use it in any methods supporting selectors.
    button_count = await page.locator('tag=button').count()
    print(button_count)
    # await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
