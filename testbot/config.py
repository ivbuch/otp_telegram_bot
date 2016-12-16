import argparse

class Config:

    token = None

    def __init__(self):
        self.token = "some_token"
        self.parseParams()
	self.validateParams()
        print "parse params" + self.token

    def parseParams(self):
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', action='store', dest='token', help='Bot token')
	parser.add_argument('-s', action='store', dest='sleepTimeout', help='Sleep timeout', default = 1000)
	args = parser.parse_args()
	self.token = args.token
	self.sleepTimeout = args.sleepTimeout
    def validateParams(self):
	if not self.token:
		raise ValueError("token must be set")
