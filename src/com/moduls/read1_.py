#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import *
from com.sina.jiami import encrypt

def ElementExist(driver,value):
    try:
        driver.find_element_by_xpath(value)
        print("用户名或是密码错误，请重新登录。")
        return False
    except NoSuchElementException:
        print("登录成功")
        return True        
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.refresh()
sleep(5)
user_file=open('myuserfile.txt','r')
values=user_file.readlines()
user_file.close()

print values
#结果以列表的形式返回
print type(values)
for i in values: 
    sleep(8)
    user=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']")
    user.clear()
    user.send_keys(i.split(';')[0])
    password=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']")
    password.clear()
    password.send_keys(encrypt(i.split(';')[1]))
    print(i.split(';')[0],'==>',encrypt(i.split(';')[1]))
    sleep(2)
    driver.find_element_by_xpath("//div[@class='info_header']/following-sibling::div[1]/div[6]//span").click()
    sleep(4)
    fg=ElementExist(driver,u"//span[text()='用户名或密码错误。']")
    print(fg)
    if fg:
        break
sleep(5)    
driver.find_element_by_xpath("//em[text()='*']").click()
sleep(2)
driver.find_element_by_xpath(u"//a[text()='退出']").click()
driver.quit()

