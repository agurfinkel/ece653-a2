import unittest
from verbal_arithmetic import solve, print_sum

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
		print("\nVerbal Arithmetic puzzle is:")
		print_sum (s1, s2, s3)
		print("\n")
        res = solve ('SEND', 'MORE', 'MONEY')
		
        self.assertEquals (res, (9567, 1085, 10652))
		print (res[0], res[1], res[2])
		print("\n")
		print ("Verbal Arithmetic Sum values are:")
        print_sum (res[0], res[1], res[2])

    def test_2 (self):
        """SINCE + JULIUS = CAESAR"""
		print("\nVerbal Arithmetic puzzle is:")
		print_sum (s1, s2, s3)
		print("\n")
        res = solve ('SINCE', 'JULIUS', 'CAESAR')
		
        self.assertEquals (res, (92685, 713219, 805904))
		print (res[0], res[1], res[2])
		print("\n")
		print ("Verbal Arithmetic Sum values are:")
        print_sum (res[0], res[1], res[2])

    def test_3 (self):
         """MENTAL + HEALTH = MATTERS"""
		 print("\nVerbal Arithmetic puzzle is:")
		print_sum (s1, s2, s3)
		print("\n")
        res = solve ('MENTAL', 'HEALTH', 'MATTERS')
		
        self.assertEquals (res, (123408, 920849, 1044257)) 
		print (res[0], res[1], res[2])
		print("\n")
		print ("Verbal Arithmetic Sum values are:")
        print_sum (res[0], res[1], res[2])

    def test_4 (self):
        """WINTER + INTO = SPRING"""
		print("\nVerbal Arithmetic puzzle is:")
		print_sum (s1, s2, s3)
		print("\n")
        res = solve ('WINTER', 'INTO', 'SPRING')
		
        self.assertEquals (res, (398167, 9815, 407982))
		print (res[0], res[1], res[2])
		print("\n")
		print ("Verbal Arithmetic Sum values are:")
        print_sum (res[0], res[1], res[2])
        
