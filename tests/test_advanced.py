# -*- coding: utf-8 -*-

from .context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        sample.hmm()
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()