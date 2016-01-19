#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import * 
import os
driver=webdriver.Firefox()
filepath='file:///'+os.path.abspath('frame.html')
driver.get(filepath)
driver.switch_to_frame('if')
sleep(3)
driver.find_element_by_id('kw').send_keys('i find it!')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
driver.switch_to_default_content()
print ('i come back!')
sleep(5)
driver.quit()