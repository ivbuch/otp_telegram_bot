import urllib, json
from bot_update import BotUpdate
from hotp_supplier import HOtpSupplier
import requests
from datetime import datetime

class HOtpBot:

    last_update_date = datetime.now()

    def __init__(self, config):
        self.htopSupplier = HOtpSupplier(config.secretKey, config.counter)
        self.config = config

    def process(self):

        updates = self.get_new_updates()
        for update in updates:
            self.sendToken(update)

    def get_url(self, resource):
        return "https://api.telegram.org/bot{}/{}".format(self.config.bot_token, resource)

    def check_not_found(self, data):

        ok = data["ok"] == True
        if not ok:
            print "not ok response {}".format(data)
            raise StandardError("not ok response")

    def get_new_updates(self):
        response = urllib.urlopen(self.get_url("getUpdates"))
        data = json.loads(response.read())
        self.check_not_found(data)

        updates = []
        for update in data["result"]:
            botUpdate = BotUpdate(update)
            if self.is_valid_command(botUpdate) and botUpdate.date > self.last_update_date and self.chat_id_valid(update):
                updates.append(botUpdate)

        self.last_update_date = datetime.now()
        return updates

    def is_valid_command(self, update):
        return update.text == "one more"

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


