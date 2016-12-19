import urllib, json
from testbot.bot_update import BotUpdate
from testbot.hotp_supplier import HOtpSupplier
import requests

class HOtpBot:

    lastUpdateId = -1

    def __init__(self, config):
        self.htopSupplier = HOtpSupplier(config.secretKey, config.counter)
        self.config = config

    def process(self):

        updates = self.get_new_updates()
        for update in updates:
            self.sendToken(update)

    def get_url(self, resource):
        return "https://api.telegram.org/{}/{}".format(self.config.bot_token, resource)


    def get_new_updates(self):
        response = urllib.urlopen(self.get_url("getUpdates"))
        data = json.loads(response.read())
        updates = []
        for update in data["result"]:
            botUpdate = BotUpdate(update)
            if botUpdate.update_id > self.lastUpdateId and self.chat_id_valid(update):
                updates.append(botUpdate)
                self.lastUpdateId = botUpdate.update_id
        return updates

    def chat_id_valid(self, update):
        return self.config.chat_id == -1 or update.chat_id == self.config.chat_id

    def get_status(self):
        response = urllib.urlopen(self.get_url("getMe"))
        data = json.loads(response.read())
        print data

    def sendToken(self, update):
        print "Process new update " + str(update.update_id)
        token = self.htopSupplier.next()
        print "new token " + token
        data = {'chat_id': update.chat_id, 'text': 'your token is *{}*, sir'.format(token), "parse_mode": "Markdown"}
        requests.post(self.get_url("sendMessage"), data = data)


