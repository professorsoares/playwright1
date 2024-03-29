# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch()
#         page = browser.new_page()
#         page.goto('http://whatsmyuseragent.org/')
#         page.screenshot(path=f'example-{browser_type.name}.png')
#         browser.close()



import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        #await page.screenshot(path=f'example.png')

        await print(page.locator("h1").all_inner_texts())
        await browser.close()


asyncio.run(main())