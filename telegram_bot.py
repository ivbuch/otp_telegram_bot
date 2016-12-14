import urllib, json

class TelegramBot:

    def get_updates(self):
        url = "https://api.telegram.org/bot314217478:xxx/getUpdates"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data

    def get_status(self):
        url = "https://api.telegram.org/bot314217478:xxx/getMe"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data







