#coding=utf-8
class Count():
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
    def countAdd(self):
        return self.a+self.b

if __name__=="__main__":
    test=Count(4,5)
    print test.countAdd()