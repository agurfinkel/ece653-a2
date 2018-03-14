import unittest
from a2q3.verbal_arithmetic import solve

class PuzzleTests (unittest.TestCase):

    def setUp (self):
        """Reset Z3 context between tests"""
        import z3
        z3._main_ctx = None
    def tearDown (self):
        """Reset Z3 context after test"""
        import z3
        z3._main_ctx = None
        
    def test_1 (self):
        """SEND + MORE = MONEY"""
        res = solve ('SEND', 'MORE', 'MONEY')
        self.assertEquals (res, (9567, 1085, 10652))

    def test_2 (self):
        """SINCE + JULIUS = CAESAR"""
        res = solve ('SINCE', 'JULIUS', 'CAESAR')
        self.assertEquals (res, (92685, 713219, 805904))

    def test_3 (self):
         """MENTAL + HEALTH = MATTERS"""
        res = solve ('MENTAL', 'HEALTH', 'MATTERS')
        self.assertEquals (res, (123408, 920849, 1044257))     

    def test_4 (self):
        """WINTER + INTO = SPRING"""
        res = solve ('WINTER', 'INTO', 'SPRING')
        self.assertEquals (res, (398167, 9815, 407982))
