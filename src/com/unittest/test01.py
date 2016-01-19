#coding=utf-8
from com.unittest.calculator import Count

class TestCount():
    def test_Add(self):
        try:
            jc=Count(3,4)
            add=jc.countAdd()
            assert(add==7),"Integer addition result error!"
        except AssertionError,msg:
            print msg 
        else:
            print "test case passed"

testuser = TestCount()
testuser.test_Add()
        
        