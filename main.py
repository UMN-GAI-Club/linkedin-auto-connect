import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from linkedin_scraper import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv


# Load environment variables
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
COOKIE = os.getenv("LINKEDIN_COOKIE")

# Argument parser
parser = argparse.ArgumentParser(description="LinkedIn auto connector")
parser.add_argument('--delay', type=int, default=1000, help='Delay between actions in milliseconds (default: 1000)')
parser.add_argument('--max-connection', type=int, default=10, help='Maximum number of connections to send (default: 10)')
args = parser.parse_args()

# Convert delay to seconds
delay_seconds = args.delay / 1000.0
max_connections = args.max_connection

def click_show_all(driver): 
    # locate the button under people you may know section
    section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
        By.XPATH,
        "//section[.//h3[normalize-space(.)='People you may know based on your recent activity']]"
    ))
)
    # find Show All button
    show_all_btn = section.find_element(
        By.XPATH,
        ".//button[.//span[normalize-space(.)='Show all']]"
    )
    # click it
    show_all_btn.click()
    
    return
    

if __name__ == '__main__':
    driver = webdriver.Chrome()

    # Login (use cookie or email/password)
    print(f"Logging in with {'cookie' if COOKIE else 'email and password'}...")
    driver.get("https://www.linkedin.com")
    actions.login(driver, EMAIL, PASSWORD, COOKIE, timeout=1000)

    print("Login successful. Navigating to the connections page...")
    driver.get("https://www.linkedin.com/mynetwork/grow/")
    
    click_show_all(driver)
    # input("You can now navigate to the desired LinkedIn page with connection requests, then press Enter here to continue...")
    
    # Wait for the page to load
    time.sleep(5)
    key_sender = ActionChains(driver)
    # get to the first connect button
    key_sender.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER)
    key_sender.perform()

    for i in range(max_connections):
        time.sleep(delay_seconds)
        print(f"Sending connection {i+1} of {max_connections}")
        key_sender.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER)
        key_sender.perform()


    input("Done. Press any keys to exit...")
    # driver.quit()

# python3 main.py --delay 1000 --max-connection 20
