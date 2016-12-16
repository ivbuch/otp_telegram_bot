import urllib, json
from testbot.bot_update import BotUpdate
from testbot.hotp_supplier import HOtpSupplier


class HOtpBot:

    lastUpdateId = -1

    def __init__(self, config):
        self.htopSupplier = HOtpSupplier(config.secretKey, config.counter)

    def process(self):

        updates = self.get_new_updates()
        for update in updates:
            self.sendToken(update)


    def get_new_updates(self):
        url = "https://api.telegram.org/bot314217478:AAGHsjSvTO26nDr3mP7-RlWhGOTbVEgyOKA/getUpdates"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        updates = []
        for update in data["result"]:
            botUpdate = BotUpdate(update)
            if botUpdate.update_id > self.lastUpdateId:
                updates.append(botUpdate)
                self.lastUpdateId = botUpdate.update_id
        return updates

    def get_status(self):
        url = "https://api.telegram.org/bot314217478:AAGHsjSvTO26nDr3mP7-RlWhGOTbVEgyOKA/getMe"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data

    def sendToken(self, update):
        print "Process new update " + str(update.update_id)
        token = self.htopSupplier.next()
        print "new token " + token


