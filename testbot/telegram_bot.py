import urllib, json

class TelegramBot:

    def get_updates(self):
        url = "https://api.telegram.org/bot314217478:AAGHsjSvTO26nDr3mP7-RlWhGOTbVEgyOKA/getUpdates"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data

    def get_status(self):
        url = "https://api.telegram.org/bot314217478:AAGHsjSvTO26nDr3mP7-RlWhGOTbVEgyOKA/getMe"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data







