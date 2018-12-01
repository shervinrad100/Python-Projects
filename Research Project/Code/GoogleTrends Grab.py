import urllib3
from selenium import webdriver

http = urllib3.PoolManager() # Create a connection pooling object
google = http.request('GET','https://google.com/trends/')

search_term = str(input('enter search term or a topic: '))

driver = webdriver.Chrome('C:/Users/sherv/OneDrive/Documents/GitHub/Projects/Research Project/chromedriver.exe')
search_box = driver.find_element_by_id('input-1')
search_box.send_keys(search_term)


