import os.path
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

import x

import unittest

class Test1(unittest.TestCase):
    def test_no_op(self):
        pass

    def test_fail(self):
        raise Exception()

if __name__ == '__main__':
    unittest.main(buffer=True)
