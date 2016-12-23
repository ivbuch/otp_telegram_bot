from otp_bot.hotp_supplier import OtpSupplier

import unittest

class BasicTestSuite(unittest.TestCase):

    def test_get_otp_values(self):

        supplier = OtpSupplier("base32secret3232", 0)
        self.assertEqual(supplier.next(), "260182")
        self.assertEqual(supplier.next(), "055283")
        self.assertEqual(supplier.next(), "795760")

if __name__ == '__main__':
    unittest.main()