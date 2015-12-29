#coding=utf-8

def is_Prime(n):
    lists=[]
    if n<=1:
        return False
    else :
        for i in range(2,n):
            lists.append(n%i)
       # print lists
        if( 0  in lists):
            return False                        
        else:
            return True
            
is_Prime(10)    
    