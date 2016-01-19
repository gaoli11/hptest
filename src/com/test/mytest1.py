# encoding: utf-8
'''
Created on 2015年12月4日

@author: hpyton
'''
from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
driver=webdriver.Firefox()
filepath='file:///'+os.path.abspath('movie')
driver.get(filepath)
fold=driver.find_element_by_xpath(u"//a[text()='新建文件夹']")
ActionChains(driver).double_click(fold).perform()
driver.close()
