#coding=utf-8
lists=[]
def is_Prime(n):
    if n<=1:
        print "it is not a prime!"
    else :
        for i in range(2,n):
            lists.append(n%i)
       # print lists
        if( 0  in lists):
            print "it is not a prime!"                          
        else:
            print   "it is a prime!"
        
is_Prime(11)    
    