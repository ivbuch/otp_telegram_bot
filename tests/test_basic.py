# -*- coding: utf-8 -*-

from .context import testbot

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()