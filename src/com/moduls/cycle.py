#coding=utf-8
from selenium import webdriver
from time import sleep
# from time import *
# driver=webdriver.Firefox()
# driver.get('https://www.baidu.com/')
# cast=['python','selenium','how to learn']
# for item in cast:  
#     driver.find_element_by_id('kw').send_keys(item)
#     sleep(2)
#     driver.find_element_by_id('kw').send_keys(' ')
# driver.find_element_by_id('su').click()
# sleep(3)
# driver.quit()

cast=['python','selenium','how to learn']
for search in cast:
    driver=webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(5)
    driver.quit()
  