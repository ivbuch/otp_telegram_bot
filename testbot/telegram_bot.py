import urllib, json
from testbot.bot_update import BotUpdate

class TelegramBot:

    lastUpdateId = -1

    def get_new_updates(self):
        url = "https://api.telegram.org/bot314217478:AAGHsjSvTO26nDr3mP7-RlWhGOTbVEgyOKA/getUpdates"
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        updates = []
        for update in data["result"]:
            updates.append(BotUpdate(update))
        return updates

    def get_status(self):
        url = "https://api.telegram.org/bot314217478:AAGHsjSvTO26nDr3mP7-RlWhGOTbVEgyOKA/getMe"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data







