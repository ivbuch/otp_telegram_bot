import argparse

class Config:

    def __init__(self):
        self.secretKey = "secretKey"
        self.parseParams()
	self.validateParams()
        print "parse params" + self.secretKey

    def parseParams(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', action='store', dest='secretKey', help='SecretKey')
        parser.add_argument('-s', action='store', dest='sleepTimeout', help='Sleep timeout', default = 1000)
        parser.add_argument('-c', action='store', dest='counter', help='Counter', default=0)
        args = parser.parse_args()
        self.secretKey = args.secretKey
        self.sleepTimeout = args.sleepTimeout
        self.counter = args.counter

    def validateParams(self):
	    if not self.secretKey:
		    raise ValueError("secretKey must be set")
