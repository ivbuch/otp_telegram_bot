from datetime import datetime

class BotUpdate:

    chat_id = None
    update_id = None
    message = None
    date = None

    def __init__(self, update_json):

        self.text = update_json["message"]["text"]
        self.update_id = update_json["update_id"]
        self.chat_id = update_json["message"]["chat"]["id"]
        self.date = datetime.fromtimestamp (update_json["message"]["date"])
