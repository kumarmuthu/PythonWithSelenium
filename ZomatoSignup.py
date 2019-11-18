'''
Created on Nov 15, 2019

@author: Muthukumar Subramanian
'''
from selenium import webdriver 
import time
  
# set webdriver path here it may vary 
browser = webdriver.Chrome(executable_path ="C:\\Users\\ms023673\\Documents\\Sel_driver\\Driver\\chromedriver_win32\\chromedriver.exe") 

# zomato link set 
browser.get('https://www.zomato.com/ncr') 
browser.maximize_window()
time.sleep(3)


# Enter your user name and email here.
fullname = "muthukumar"
email = "noreplymuthukumar@gmail.com"

# Signup
browser.find_element_by_xpath("//a[@id ='signup-link']").click() 
time.sleep(2) 
browser.find_element_by_xpath("//a[@id ='signup-email']").click()
# full name
a = browser.find_element_by_xpath("//input[@id ='sd-fullname']") 
a.send_keys(fullname) 
# email
a = browser.find_element_by_xpath("//input[@id ='sd-email']") 
a.send_keys(email)
# Check box click
# browser.find_element_by_id("sd-newsletter").click()
# or
browser.find_element_by_name("newsletter").click()
# submit button clicked
browser.find_element_by_xpath("//input[@id ='sd-submit']").click()
time.sleep(5)
browser.close()
