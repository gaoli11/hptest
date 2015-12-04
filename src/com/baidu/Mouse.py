#coding=utf-8
from selenium import webdriver
from time import *
import sys
sys.path.append('D:\116460\workspace\WYexercise\src\com\exercise\wangyi')
from com.sina import jiami
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get('http://pan.baidu.com/')
driver.implicitly_wait(20)
name=driver.find_element_by_id('TANGRAM__PSP_4__userName')
sleep(2)
name.clear()
name.send_keys(u'牵着蚂蚁溜11')
password=driver.find_element_by_id('TANGRAM__PSP_4__password')
sleep(2)
password.clear()
password.send_keys(jiami.encrypt('b\jt\i325'))
driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
sleep(5)
driver.maximize_window()
sleep(2)
#driver.find_element_by_xpath("//em[class='app-icon i-disk']").click()
#sleep(2)
driver.refresh()
sleep(10)
lastceng=driver.find_element_by_xpath("//div[@class='list']/div[last()]")
ActionChains(driver).move_to_element_with_offset(lastceng, 100, 100).perform()
print 123
sleep(5)
driver.close()
