import sys
import unittest

if __name__ == '__main__':
    name = 'puzzle_tests'
    suite = unittest.defaultTestLoader.loadTestsFromNames ([name])
    result = unittest.TextTestRunner().run (suite)
