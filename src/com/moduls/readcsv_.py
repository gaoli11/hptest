#coding=utf-8
from selenium import webdriver
from time import *
import csv

myfile=open('user_info.csv','r')
date=csv.reader(myfile)

print date
  
for item in date:
    print item[0]
    print item[1]



