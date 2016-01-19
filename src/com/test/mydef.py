#coding=utf-8
from time import *
from com.sina.jiami import encrypt
def Login(driver):
    username=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']")
    sleep(5)
    username.send_keys('gaoli152027@sina.com')
    password=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']")
    password.send_keys(encrypt('b\jT\i325'))
    sleep(5)
    driver.find_element_by_xpath("//div[@class='info_header']/following-sibling::div[1]/div[6]//span").click()
def Loginout(driver):
    driver.find_element_by_xpath("//em[text()='*']").click()
    sleep(2)
    driver.find_element_by_xpath(u"//a[text()='退出']").click()
    driver.quit()
    