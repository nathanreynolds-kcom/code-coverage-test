import os.path
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

import myexamplelib

class ExampleTestCase(unittest.TestCase):
    def test_success(self):
        assert myexamplelib.add_one_to_one() == 2
