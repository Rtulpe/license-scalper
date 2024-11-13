# This project was created to save me 70 euros from these ukrainian lads

import os
from dotenv import load_dotenv
import asyncio
import time
from pyppeteer import launch

# Load the environment variables
load_dotenv()

async def scraper():
    # Launch the browser
    executable_path = os.getenv('BROWSER_PATH')
    browser = await launch({
        'headless': False,
        'executablePath': executable_path, # If nothing starts, this is the issue
        })
    page = await browser.newPage()

    await page.goto("https://platesmania.com/pl/gallery")
    time.sleep(5)

    await page.screenshot({'path': 'screenlog.png'})

    await browser.close()

# Run the main function
if __name__ == "__main__":
    asyncio.run(scraper())