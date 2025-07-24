import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from linkedin_scraper import actions
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

if __name__ == '__main__':
    driver = webdriver.Chrome()

    # Login (use cookie or email/password)
    print(f"Logging in with {'cookie' if COOKIE else 'email and password'}...")
    driver.get("https://www.linkedin.com")
    actions.login(driver, EMAIL, PASSWORD, COOKIE, timeout=1000)

    driver.get("https://www.linkedin.com/mynetwork/grow/")
    input("Navigate to the desired LinkedIn page, then press Enter here to continue...")

    key_sender = ActionChains(driver)

    for i in range(max_connections):
        print(f"Sending connection {i+1} of {max_connections}")
        key_sender.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER)
        key_sender.perform()
        time.sleep(delay_seconds)

    input("Done. Press any keys to exit...")
    # driver.quit()

# python3 main.py --delay 1000 --max-connection 20
