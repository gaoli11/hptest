#coding=utf-8
from selenium import webdriver
from com.sina.jiami import encrypt
from time import *
driver=webdriver.Firefox()
driver.get('http://mail.163.com/')
sleep(5)
print driver.title
sleep(2)
print driver.current_url
sleep(2)
name=driver.find_element_by_id('idPlaceholder')
sleep(2)
name.send_keys('gaoli152027')
password=driver.find_element_by_id('pwdPlaceholder')
sleep(2)
password.send_keys(encrypt('b\jt\i325'))
driver.find_element_by_id('loginBtn').click()
sleep(3)
print driver.title
sleep(3)
print driver.current_url
sleep(2)
usename=driver.find_element_by_id('spnUid').text
print usename
listname=['gaoli152027@163.com']
try:
    if usename in listname:
        print 'true,testcase is successful!'
    else:
        print 'false,testcase is fail!!!'

except Exception,e:
    print e
    print 'login is fail'
driver.quit()