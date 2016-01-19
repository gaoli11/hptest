# coding = utf-8
from selenium import webdriver
from time import *
import jiami
driver=webdriver.Firefox()
driver.get('http://www.weibo.com')
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']").send_keys('gaoli152027@sina.com')
sleep(2)
driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']").send_keys(jiami.encrypt('b\jT\i325'))
sleep(2)
driver.find_element_by_xpath("//div[@class='info_header']/following-sibling::div[1]/div[6]//span").click()
sleep(10)
driver.maximize_window()
sleep(2)
driver.refresh()
driver.close()
