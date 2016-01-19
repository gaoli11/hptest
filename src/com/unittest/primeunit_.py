#coding=utf-8
from com.base_.prime_ import is_Prime
import unittest

class Primer(unittest.TestCase):
    def setUp(self):
        print "test is begining !"
    def test_Primer(self):
        self.assertTrue(is_Prime(11), msg="It is not a prime")
        
    def tearDown(self):
        print"test is over！"

if __name__=="__main__":
    unittest.main()