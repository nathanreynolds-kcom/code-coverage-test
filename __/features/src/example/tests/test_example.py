import os.path
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

import example

class ExampleTestCase(unittest.TestCase):
    def test_success(self):
        assert example.add_one_to_one_times_two() == 4
