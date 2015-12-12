# encoding= utf-8
from selenium import webdriver
import random
from time import *
# driver=webdriver.Firefox()
verify=random.randint(1000,9999)
print u"生成的验证码为：%d"%verify
name=int(raw_input(u'输入你的验证码'))
print type(verify)
print type(name)
if isinstance(name, str):
    print 'jj'

if name==verify:
    print "it's ok1"
elif name=='123456':
    print "it's ok2"
else:
    print"it's wrong"
sleep(5)
# driver.quit()
