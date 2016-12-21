import argparse

class Config:

    def __init__(self):
        self.secretKey = "secretKey"
        self.parseParams()
        self.validateParams()

    def parseParams(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-bot', action='store', dest='bot_token', help='Bot token')
        parser.add_argument('-secret', action='store', dest='secretKey', help='SecretKey')
        parser.add_argument('-chat', action='store', dest='chat_id', help='Chat id')
        parser.add_argument('-sleep', action='store', dest='sleepTimeout', help='Sleep timeout', default = 5)
        parser.add_argument('-counter', action='store', dest='counter', help='Counter', default=0)
        args = parser.parse_args()
        self.secretKey = args.secretKey
        self.sleepTimeout = args.sleepTimeout
        self.counter = args.counter
        self.bot_token = args.bot_token
        self.chat_id = args.chat_id

    def validateParams(self):
        if not self.secretKey:
            raise ValueError("secretKey must be set")
        if not self.bot_token:
            raise ValueError("bot_token must be set")
        if not self.chat_id:
            raise ValueError("chat_id must be set")
