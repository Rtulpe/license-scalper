# This project was created to save me 70 euros from these ukrainian lads

import asyncio
from pyppeteer import launch

async def scraper():
    # Launch the browser
    browser = await launch({'headless': False})
    page = await browser.newPage()

    await page.goto("https://www.google.com/")

    await page.screenshot({'path': 'example.png'})

    await browser.close()

# Run the main function
if __name__ == "__main__":
    asyncio.run(scraper())