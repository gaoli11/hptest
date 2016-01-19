#coding=utf-8
from selenium import webdriver
from com.sina.jiami import encrypt
from mydef4 import Logiout
from time import *
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
sleep(5)
Logiout(driver).Login('gaoli152027@sina.com',encrypt('b\jT\i325'))
sleep(5)
Logiout(driver).Loginout()
