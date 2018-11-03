#import urllib3
from selenium import webdriver
'''
http = urllib3.PoolManager() # Create a connection pooling object
google = http.request('GET','https://google.com/trends/')

search_term = str(input('enter search term or a topic: '))

driver = webdriver.Chrome('C:/Users/sherv/OneDrive/Documents/GitHub/Projects')
search_box = driver.find_element_by_id('input-1')
search_box.send_keys(search_term)
'''
# try to log into fb see if it works

# Assign user variables
#myemail = input('enter email: ')
mypassword = 'Xmas2015'
#input('enter password: ')
myemail = 'shervinrad100@gmail.com'
# pool the web
driver = webdriver.Chrome('C:/Users/sherv/OneDrive/Documents/GitHub/Projects/chromedriver.exe')
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

