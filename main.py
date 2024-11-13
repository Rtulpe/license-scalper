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
        'devtools': True, # Magically skips cloudflare checks
        'args': [
            '--incognito',  # Start in incognito mode (no previous session)
            '--no-first-run',  # Skip first-run prompts
            '--disable-restore-session-state',  # Disable restoring last session
        ],
        })
    page = await browser.newPage()

    # Make a folder for the images
    image_path = os.getenv('IMG_PATH')
    try:
        os.makedirs(image_path)
    except FileExistsError:
        pass

    await page.goto("https://platesmania.com/pl/gallery")

    # Accept the damn cookies
    accept_button_selector = 'button.fc-button.fc-cta-consent.fc-primary-button'
    try:
        time.sleep(5)
        await page.waitForSelector(accept_button_selector, timeout=500)
        await page.click(accept_button_selector)
        time.sleep(5)
        print("The damn cookies have been accepted")
    except Exception as e:
        print(f"Error accepting cookies: {e}")

    await page.screenshot({'path': 'screenlog.png'})

    await browser.close() 

# Run the main function
if __name__ == "__main__":
    asyncio.run(scraper())