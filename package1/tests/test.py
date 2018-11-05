import os.path
import sys
import unittest

sys.path = [os.path.join(os.path.dirname(__file__), '../src')] + sys.path

import module1

class TestCase(unittest.TestCase):
    def test_x(self):
        pass
