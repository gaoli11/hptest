#coding=utf-8
from time import *
from com.sina.jiami import encrypt
class Logiout():
    def __init__(self,driver):
        self.driver=driver
    def Login(self,username,password2):
        driver=self.driver
        user=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']")
        sleep(3)
        user.send_keys(username)
        password=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']")
        password.send_keys(password2)
        sleep(3)
        driver.find_element_by_xpath("//div[@class='info_header']/following-sibling::div[1]/div[6]//span").click()
    def Loginout(self):
        driver=self.driver
        driver.find_element_by_xpath("//em[text()='*']").click()
        sleep(2)
        driver.find_element_by_xpath(u"//a[text()='退出']").click()
        driver.quit()
        