# coding=utf-8
from selenium import webdriver
from time import *
from ctypes.wintypes import SIZE
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
a=driver.find_element_by_id('kw')
size=a.size
print size
b=driver.find_element_by_id('cp').text
print b
atrbute=a.get_attribute('type')
print atrbute
result=a.is_displayed()
print result
a.send_keys('selenium')
a.submit()
driver.close()

