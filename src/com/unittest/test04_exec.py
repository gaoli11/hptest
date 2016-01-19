#coding=utf-8
from com.unittest.calculator import  Count
import unittest
class MyInput(unittest.TestCase):
    def setUp(self):
        dight=raw_input("输入一个整形数字：")
        self.dight=dight
    def test_Input(self):
        self.assertEqual(int(self.dight), 10,msg='The data entered is not valid!')
    def tearDown(self):
        print 'end'

if __name__=="__main__":
  #  unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(MyInput("test_Input"))
     
    runner=unittest.TextTestRunner()
    runner.run(suite)
     
