# encoding= utf-8
from selenium import webdriver
from time import *

driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(3)
#driver.maximize_window()
sleep(3)
js='window.scrollTo(0,10000)'
driver.execute_script(js)
sleep(3)
js2='window.scrollTo(10000,10000)'
driver.execute_script(js2)
sleep(5)
driver.quit()