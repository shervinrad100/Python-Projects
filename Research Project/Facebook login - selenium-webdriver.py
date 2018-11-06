# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 23:22:04 2018

@author: sherv
"""

from selenium import webdriver

# Assign user variables
#myemail = input('enter email: ')
mypassword = ''
#input('enter password: ')
myemail = 'shervinrad100@gmail.com'
# pool the web
driver = webdriver.Chrome('C:/Users/sherv/OneDrive/Documents/GitHub/Projects/Research Project/chromedriver.exe')
driver.set_page_load_timeout(30) # in sec
driver.get('https://www.facebook.com/')
# find username and password fields
'''
username = driver.find_element_by_id('email')
pwd = driver.find_element(id,'pass')
# insert uername and pass
username.send_keys(myemail)
pwd.send_keys(mypassword)
'''
username = driver.find_element_by_id('email').send_keys(myemail)
pwd = driver.find_element_by_id('pass').send_keys(mypassword)
# find login botton
login = driver.find_element_by_id('u_0_3')
# press the login botton
login.submit()

driver.maximize_window()
