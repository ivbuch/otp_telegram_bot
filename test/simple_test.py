import unittest

from test import Car

class TestStringMethods(unittest.TestCase):

    def test_car(self):

        print "lalala"
        car = Car()
        car.print_name()
        self.assertEqual(111,111)

if __name__ == '__main__':
    unittest.main()