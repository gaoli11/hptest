#coding=utf-
from com.unittest.calculator import Count
import unittest

class CountTest(unittest.TestCase):
    def setUp(self):
        print "test begin!"
    def test_Add(self):
            jd=Count(5,6)
            self.assertEqual(jd.countAdd(),11)
    def tearDown(self):
        print "test end"
        
if __name__=="__main__":
    unittest.main()