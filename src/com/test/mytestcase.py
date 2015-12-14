#coding =utf-8
from selenium import webdriver
from time import *
from mydef import Login
from com.test.mydef import Loginout
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
sleep(5)
Login(driver)
sleep(10)
Loginout(driver)