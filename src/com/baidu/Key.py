#coding=utf-8
from selenium import webdriver
from time import  *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
sleep(2)
driver.find_element_by_id('kw').send_keys('seleniumm')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
sleep(2)
driver.find_element_by_id('kw').send_keys(u'教程')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
sleep(2)
