#coding=utf-8
from com.unittest.calculator import  Count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        print "test begin !"
    def testAdd1(self):
        mytest1=Count(4,6)
        self.assertEqual(mytest1.countAdd(),10)
    def testAdd2(self):
        mytest1=Count(7,9)
        self.assertEqual(mytest1.countAdd(),16)
    def tearDown(self):
        print "test over !"
        
if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestCount("testAdd1"))
    suite.addTest(TestCount("testAdd2"))
    
    runner=unittest.TextTestRunner()
    runner.run(suite)