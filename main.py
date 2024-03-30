import os
import time

import schedule
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from telegram import TelegramBot

env = os.environ['ENVIRONMENT']
staking_node = os.environ['STAKING_NODE']
bot_token = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']

# Initialize Chrome WebDriver Options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

telegram_bot = TelegramBot(bot_token, chat_id, env == 'PROD')


def crawle_staking_explorer():
    if env == "PROD":
        # Required for Docker Container in prod to get chromedriver
        service = Service(executable_path='/usr/local/bin/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    driver.get("https://cosmos.pointnetwork.io/point/staking/" + staking_node)

    wait = WebDriverWait(driver, 20)
    outstanding_rewards_elem = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "transaction-title"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select(".transaction-title")
    amount_coins = body[1].text.strip()
    driver.quit()
    send_message_telegram(amount_coins)


def send_message_telegram(amount_coins):
    message = "<b>Point Stacking Monitor</b> \n"
    message += "\n Amount: <b>" + amount_coins + "</b>"
    telegram_bot.send_message(message)
    return message


if __name__ == "__main__":
    print("Point Staking Monitor running ... :)")

# schedule.every().day.at("12:00").do(crawle_staking_explorer)
schedule.every(20).seconds.do(crawle_staking_explorer)

while True:
    schedule.run_pending()
    time.sleep(1)
