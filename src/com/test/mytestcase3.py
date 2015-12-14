#coding=utf-8
from selenium import webdriver
from mydef3 import Logiout
from time import *
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
sleep(5)
Logiout(driver).Login()
sleep(10)
Logiout(driver).Loginout()