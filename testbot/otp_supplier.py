import pyotp

class OtpSupplier:

    counter = None
    hotp = None

    def __init__(self, base32secret3232, count = 0):
        self.counter = count
        self.hotp = pyotp.HOTP(base32secret3232)

    def next(self):
        value = self.hotp.at(self.counter)
        self.counter = self.counter + 1
        return value







