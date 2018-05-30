#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: zhisiying 
@contact: 643424678@qq.com 
@site: http://zhisy.top 
@software: PyCharm 
@file: login.py 
@time: 2018/5/30/030 10:58 
"""
from config import username,password
from selenium import webdriver
import time
import json


post = {}
driver = webdriver.Chrome()
driver.get('https://mp.weixin.qq.com/')
time.sleep(2)
driver.find_element_by_xpath('//input[@name="account"]').clear()
driver.find_element_by_xpath('//input[@name="account"]').send_keys(username)
driver.find_element_by_xpath('//input[@name="password"]').clear()
driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
# 在自动输完密码之后记得点一下记住我
time.sleep(5)
driver.find_element_by_xpath("//a[@class='btn_login']").click()
#手机扫二维码！
time.sleep(15)
driver.get('https://mp.weixin.qq.com/')
cookie_items = driver.get_cookies()
for cookie_item in cookie_items:
    post[cookie_item['name']] = cookie_item['value']
cookie_str = json.dumps(post)
with open('cookie.txt', 'w+', encoding='utf-8') as f:
    f.write(cookie_str)
