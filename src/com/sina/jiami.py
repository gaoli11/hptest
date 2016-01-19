# coding = utf-8
def  encrypt(x):
    z=[]
    y=list(x)
    for i in y:
        if i.isdigit():
            m=((int(i)+7)%3)
            z.append(str(m))
        elif i.isalpha():
            a=ord(i)
            if a>121 :
                z.append(str(chr(a-5)))
            else:
                z.append(str(chr(a+5)))
        else:           
            a=ord(i)
            if a<64:
                z.append(str(chr(2*a)))
            else:
                z.append(str(chr(a+5)))
    #z.extend(['-','+'])
    n=''.join(z)
    return n


