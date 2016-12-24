import json, time, requests

import urllib.request, urllib.parse, urllib.error
from datetime import datetime
from threading import Timer
from bot_update import BotUpdate
from hotp_supplier import HOtpSupplier


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
            print("not ok response {}".format(data))
            raise Exception("not ok response")

    def make_json_call(self, method, data):
        response = requests.post(self.get_url(method), data=data)
        response_json = json.loads(response.text)
        return response_json

    def get_new_updates(self):

        request_data = {"limit": 100}
        if hasattr(self, "update_id"):
            request_data["offset"] = self.update_id + 1

        data = self.make_json_call("getUpdates", request_data)
        self.check_not_found(data)

        updates = []
        for update in data["result"]:
            botUpdate = BotUpdate(update)
            if (self.is_valid_command(botUpdate) and self.chat_id_valid(botUpdate)):
                updates.append(botUpdate)
                self.update_id = update["update_id"]

       return updates

    def is_valid_command(self, update):
        return update.text == self.config.command

    def chat_id_valid(self, update):
        result = update.chat_id == int(self.config.chat_id)
        if not result:
            print("incorrect chat id {}".format(update.chat_id))
        return result

    def get_status(self):
        response = urllib.request.urlopen(self.get_url("getMe"))
        data = json.loads(response.read())
        print(data)

    def sendToken(self, update):
        print("Process new update " + str(update.update_id))
        token = self.htopSupplier.next()
        print("new token " + token)
        data = {'chat_id': update.chat_id, 'text': 'your token is *{}*, sir'.format(token), "parse_mode": "Markdown"}
        response_json = self.make_json_call("sendMessage", data)
        if response_json["ok"]:
            self.schedule_invalidate_message(response_json["result"]["message_id"])

    def schedule_invalidate_message(self, message_id):
        Timer(30, self.invalidate_message, [message_id]).start()

    def invalidate_message(self, message_id):

        print("invalidated token " + str(message_id))
        data = {'chat_id': self.config.chat_id, 'text': 'invalidated message', "message_id": message_id}
        self.make_json_call("editMessageText", data)
