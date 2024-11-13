# This project was created to save me 70 euros from these ukrainian lads

import asyncio
import time
from pyppeteer import launch

async def scraper():
    # Launch the browser
    browser = await launch({
        'headless': False,
        'executablePath': '/usr/bin/brave-browser', # If nothing starts, this is the issue
        })
    page = await browser.newPage()

    await page.goto("https://www.google.com/")
    time.sleep(5)

    await page.screenshot({'path': 'example.png'})

    await browser.close()

# Run the main function
if __name__ == "__main__":
    asyncio.run(scraper())