# encoding= utf-8
from selenium import webdriver
from time import *

driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
try:   
    driver.find_element_by_id('kwerror').send_keys('selenium')
    driver.find_element_by_id('su').click()
except:
    driver.get_screenshot_as_file('baidu_error.jpg')
else:
    print"it's ok"
finally:
    print "the procedure is over"
sleep(5)
driver.quit()
