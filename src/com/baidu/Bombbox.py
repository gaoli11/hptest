# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import *
driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
driver.maximize_window()
sleep(3)
driver.refresh()
setting=driver.find_element_by_link_text(u'设置')
sleep(2)
ActionChains(driver).move_to_element(setting).perform()
driver.find_element_by_class_name('setpref').click()
sleep(2)
driver.find_element_by_name('NR').click()
sleep(2)
shezhi=driver.find_element_by_xpath(u"//option[text()='每页显示50条']")
sleep(2)
shezhi.send_keys(Keys.ENTER)
driver.find_element_by_class_name('prefpanelgo').click()
sleep(2)
driver.switch_to_alert().accept()
sleep(5)
print 'i got it !'
driver.quit()


