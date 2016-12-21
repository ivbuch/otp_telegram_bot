from datetime import datetime

class BotUpdate:

    def __init__(self, update_json):

        self.text = update_json["message"]["text"]
        self.message_id = update_json["message"]["message_id"]
        self.update_id = update_json["update_id"]
        self.chat_id = update_json["message"]["chat"]["id"]
        self.date = datetime.fromtimestamp (update_json["message"]["date"])
