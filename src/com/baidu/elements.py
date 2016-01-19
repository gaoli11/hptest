#coding =utf-8
from selenium import webdriver
from time import *
import os
from itertools import count
driver=webdriver.Firefox()
file_path='file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
print len(checkboxes)
for checkbox in checkboxes:
    checkbox.click()
driver.find_elements_by_xpath("//input[@type='checkbox']").pop().click()
sleep(5)
driver.quit()