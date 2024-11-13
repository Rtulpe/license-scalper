# This project was created to save me 70 euros from these ukrainian lads

import os
from dotenv import load_dotenv
import asyncio
import time
from pyppeteer import launch

# Load the environment variables
load_dotenv()
# Small pauses to not ddos the website
sus_time = int(os.getenv('SUS_TIME'))

def init_enviroment():
    # Get paths
    executable_path = os.getenv('BROWSER_PATH')
    print(executable_path)
    image_path = os.getenv('IMG_PATH')

    # Make a folder for the images

    try:
        os.makedirs(image_path)
    except FileExistsError:
        pass

    return [image_path, executable_path]

async def launch_browser(executable_path):
    browser = await launch({
    'executablePath': executable_path, # If nothing starts, this is the issue
    'devtools': True,
    })

    return browser

async def accept_cookies(page):
    # Accept the damn cookies
    accept_button_selector = 'button.fc-button.fc-cta-consent.fc-primary-button'
    await page.waitForSelector(accept_button_selector, timeout=500)

    try:
        await asyncio.sleep(sus_time)  # Use asyncio.sleep instead of time.sleep
        await page.waitForSelector(accept_button_selector, timeout=5000)  # increased timeout
        
        button = await page.querySelector(accept_button_selector)
        if button is None:
            print("Accept button not found!")
        else:
            await button.click()
            print("The damn cookies have been accepted")

        await asyncio.sleep(sus_time)  # wait a bit after clicking
    except Exception as e:
        print(f"Error accepting cookies: {e}")

async def main():
    # Init
    [image_path, executable_path] = init_enviroment()

    # Launch the browser
    browser = await launch_browser(executable_path)
    pages = await browser.pages()
    page = pages[-1]
    

    # Navigate to the license plate gallery and the damn accept cookies
    await page.goto("https://platesmania.com/pl/gallery")
    await accept_cookies(page)

    #await page.screenshot({'path': '${image_path}/example.png'})

    #await browser.close() 

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())