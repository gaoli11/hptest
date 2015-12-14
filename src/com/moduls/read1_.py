#coding=utf-8
from selenium import webdriver
from time import *
from com.sina.jiami import encrypt
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
sleep(5)
user_file=open('myuserfile.txt','r')
values=user_file.readlines()
user_file.close()

print values
#结果以列表的形式返回
print type(values)
sleep(3)
for i in values:
    try:  
        user=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']")
        user.send_keys(i.split(';')[0])
        password=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']")
        password.send_keys(encrypt(i.split(';')[1]))
        sleep(5)
        driver.find_element_by_xpath("//div[@class='info_header']/following-sibling::div[1]/div[6]//span").click()
    except:
        print 'user is error'
    continue
sleep(5)    
driver.find_element_by_xpath("//em[text()='*']").click()
sleep(2)
driver.find_element_by_xpath(u"//a[text()='退出']").click()
driver.quit()

