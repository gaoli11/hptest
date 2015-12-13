# encoding = utf-8
from time import *
def Login(driver):
    username=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']")
    sleep(5)
    username.send_keys('gaoli152027@sina.com')
    password=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']")
    password.send_keys('gaoYan100')
    sleep(5)
    driver.find_element_by_xpath("//div[@class='info_header']/following-sibling::div[1]/div[6]//span").click()