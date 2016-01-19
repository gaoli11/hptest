#coding=utf-8
from selenium import webdriver
from time import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  as EC
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
sleep(3)
#inputer=EC.presence_of_element_located(By.ID,"kw")
#print type(inputer)
inputer=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
inputer.send_keys('selenium')
#element=WebDriverWait(driver,5,0.5).until(lambda driver : input_.is_displayed())
# element=WebDriverWait(driver,5,0.5).until(lambda driver : input_.is_displayed())
# sleep(5)
# input_.send_keys('selenium')
# sleep(2)
# driver.quit()