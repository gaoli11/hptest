# coding=utf-8
from selenium import webdriver
from time import *
driver=webdriver.Firefox()
driver.get('http://www.youdao.com')
#获得cookie
cookie=driver.get_cookies()
#打印
#print cookie
sleep(5)
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbb'})
cookies=driver.get_cookies()

for cookie in cookies:
    print "%s -> %s" % (cookie['name'], cookie['value'])
driver.quit()
