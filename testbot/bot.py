import logging
import time

from testbot.telegram_bot import TelegramBot

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