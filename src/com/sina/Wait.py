#coding=utf-8
from selenium import webdriver
from time import *
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
sleep(3)
input_=driver.find_element_by_id('kw')
element=WebDriverWait(driver,5,0.5).until(lambda driver : input_.is_displayed())
sleep(5)
input_.send_keys('selenium')
sleep(2)
driver.quit()