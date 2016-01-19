#coding=utf-8
from selenium import webdriver
from mydef2 import Logiout
from time import *
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
sleep(5)
Logiout().Login(driver)
sleep(10)
Logiout().Loginout(driver)