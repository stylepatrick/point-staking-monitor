import requests


class TelegramBot:

    def __init__(self, bot_token, chat_id, prod):
        self.__base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=html&text="
        self.__prod = prod

    def send_message(self, message):
        url = self.__base_url + message
        if self.__prod:
            requests.get(url).json()
        else:
            print(url)
