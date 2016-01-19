#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import *
from com.sina.jiami import encrypt

def ElementExist(driver,pathmess):
    try:
        driver.find_element_by_xpath(pathmess)
        print("用户名或是密码错误，请重新登录。")
        return False
    except NoSuchElementException:
        print("欢迎登陆")
        return True        
driver=webdriver.Firefox()
driver.get('http://www.weibo.com/')
sleep(5)
user_file=open('myuserfile.txt','r')
values=user_file.readlines()
user_file.close()

print values
#结果以列表的形式返回
print type(values)

for i in values: 
    sleep(5)
    user=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='username']")
    user.send_keys(i.split(';')[0])
    password1=driver.find_element_by_xpath("//input[@class='W_input' and @node-type='password']")
    password1.send_keys(encrypt(i.split(';')[1]))
    print(i.split(';')[0],'==>',encrypt(i.split(';')[1]))
    sleep(2) 
    button1= WebDriverWait(driver,10,2).until(EC.presence_of_element_located((By.XPATH,"//div[@class='info_header']/following-sibling::div[1]/div[6]//span")))
    button1.click()
    sleep(2)
    result=ElementExist(driver,"//span[text()='用户名或密码错误。']")
    print(result)
    if result:
        break
    else:
        print(result)
        driver.refresh()
        sleep(5)
        continue
sleep(5)    
driver.find_element_by_xpath("//em[text()='*']").click()
sleep(2)
driver.find_element_by_xpath(u"//a[text()='退出']").click()
driver.quit()

