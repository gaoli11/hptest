# encoding = utf-8
from selenium import webdriver
from time import *
from mydef import Login
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
sleep(5)
Login(driver)