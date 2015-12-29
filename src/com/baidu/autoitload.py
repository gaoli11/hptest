# encoding=utf-8
from selenium import webdriver
import os
from time import *
driver=webdriver.Firefox()
filepath='file:///'+os.path.abspath('upfile.html')
driver.get(filepath)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@type='file']").click()
os.system(r'.\app\upfile.exe')
sleep(10)
driver.quit()
