#coding=utf-8
from selenium import webdriver
from com.sina.jiami import encrypt
from time import *

class Account():
    def __init__(self,username='',password=''):
        self.driver=webdriver.Firefox()
        self.driver.get('http://www.weibo.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.username=username
        self.password=password
        sleep(5)
    def do_login_as(self):
        driver=self.driver    
        username=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']")
        username.send_keys(self.username)
        password=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']")
        password.send_keys(self.password)
        sleep(5)
        driver.find_element_by_xpath("//div[@class='info_header']/following-sibling::div[1]/div[6]//span").click()
    def do_logout_as(self):
        driver=self.driver
        sleep(10)
        driver.find_element_by_xpath("//em[text()='*']").click()
        sleep(5)
        driver.find_element_by_xpath(u"//a[text()='退出']").click()
        sleep(3)
        driver.quit()
if __name__=='__main__':
        
    #实例化登陆信息
    admin1=Account(username='gaoli152027@sina.com',password=encrypt('b\jT\i325'))
    #admin2=Account(username='zhangsan',password='123456')
    #调用函数登陆
    
    admin1.do_login_as()
    admin1.do_logout_as()
    #do_login_as(admin2)
