import logging
import time

from config import Config
from telegram_bot import TelegramBot

config = Config()
logging.basicConfig(filename='example.log',level=logging.INFO)

if __name__ == "__main__":

    bot = TelegramBot()

    while True:
        logging.info('Waiting 10 seconds')
        time.sleep(3)
        updates = bot.get_new_updates()
        try:
            logging.debug("do work")
        except:
            logging.exception("Failed to get updates.")
