


import asyncio
from playwright.async_api import async_playwright

async def main():


    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        page = await browser.new_page()
        async with page.expect_worker("**/*Scrum*.pdf") as first:
            await page.goto("https://pt.wikipedia.org/wiki/Scrum")
            first_request = await first.value
            print(first_request.url)


asyncio.run(main())