# encoding=utf-8
from selenium import webdriver
from time import *
import random
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com/')
driver.maximize_window()
driver.implicitly_wait(20)
sreach_windows=driver.current_window_handle
sleep(5)
driver.refresh()
#driver.find_element_by_class_name('tj_login').click()
driver.find_element_by_link_text(u'登录').click()
sleep(2)
driver.find_element_by_link_text(u'立即注册').click()
all_handles=driver.window_handles
for handle in all_handles:
    if handle!=sreach_windows:
        driver.switch_to_window(handle)
        print 'now register window!'
        try:
            code=raw_input('请输入验证码：')
            sleep(3)
            driver.find_element_by_id('TANGRAM__PSP_4__account').send_keys('gaoli152027@qq.com')
            driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('aaaaa11111')
            sleep(2)
            driver.find_element_by_id('TANGRAM__PSP_4__verifyCode').send_keys(code)
            driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
        except Exception,e:
            print e
            print 'register is fail！'
        finally:
            pass
    

    