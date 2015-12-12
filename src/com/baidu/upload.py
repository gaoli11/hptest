# encoding=utf-8
from selenium import webdriver
import os
from time import *
driver=webdriver.Firefox()
filepath='file:///'+os.path.abspath('upfile.html')
driver.get(filepath)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@type='file']").send_keys('D:\pyst\python.txt')
sleep(5)
driver.quit()
