#coding=utf-8
import unittest
class Is_In(unittest.TestCase):
    def setUp(self):
        print "begin to test"
    def test_Isin(self):
        self.assertIn("we arer","we are family",msg="not contains")
    def tearDown(self):
        print "test end!"
        
if __name__=="__main__":
    unittest.main()        