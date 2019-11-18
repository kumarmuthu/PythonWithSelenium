'''
Created on Nov 15, 2019
 
@author: Muthukumar Subramanian
'''
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import time
import sys
 
# set webdriver path here it may vary 
browser = webdriver.Chrome(executable_path ="C:\\Users\\muthu\\Documents\\Sel_driver\\Driver\\chromedriver_win32\\chromedriver.exe") 
 
# zomato link set 
browser.get('https://www.zomato.com/ncr') 
# browser.maximize_window()
time.sleep(3) 
# Enter your user name and email here. 
 
fullname = "muthukumar"
email = "noreplymuthukumar@gmail.com"
 
# Sign in
# Sign in element clicked
browser.find_element_by_xpath("//a[@id ='signin-link']").click() 
time.sleep(3)
 
# Login clicked 
browser.find_element_by_xpath("//a[@id ='login-email']").click()
     
# username/email send 
a = browser.find_element_by_xpath("//input[@id ='ld-email']") 
a.send_keys(email)
# # password send 
# b = browser.find_element_by_xpath("//input[@id ='ld-password']") 
# b.send_keys(password)

# submit button clicked
browser.find_element_by_xpath("//input[@id ='ld-submit-global']").click()
 
print("Enter OTP: ")
input_a = sys.stdin.readline()
input_a = input_a.strip()
print("OTP is: ",input_a)
b = browser.find_element_by_class_name("verification-code-value")
b.send_keys(input_a)

# Go click
# WRONG TRY
# browser.find_element_by_class_name("mtop ui button fluid massive red verif-code-submit").click()
# It is correct
browser.find_element_by_xpath("//*[@id='ld-login-otp-page']/div[2]/a").click()
print('Login Successful')
# import pdb;pdb.set_trace()
time.sleep(10)
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Muthukumar'])[1]/i[1]").click()
time.sleep(10)
browser.find_element_by_link_text("Profile").click()
print("Profile click")
time.sleep(10)
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Muthukumar'])[1]/i[1]").click()
time.sleep(10)
browser.find_element_by_id("logout").click()
print("Logout successful")
time.sleep(10)
browser.close()
