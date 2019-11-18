'''
Created on Nov 15, 2019

@author: Muthukumar Subramanian
'''
from selenium import webdriver 
import time

# set webdriver path here it may vary
browser = webdriver.Chrome(executable_path ="C:\\Users\\ms023673\\Documents\\Sel_driver\\Driver\\chromedriver_win32\\chromedriver.exe") 
  
# website_URL ="https://www.google.co.in/"
browser.get("https://github.com/kumarmuthu/python_logic") 
browser.maximize_window() 

# refresh time
refreshrate = int(2) 
while True: 
    b = 0
    for i in range(1, 6, 1):
        print("I: ",i)
        # This would keep running until you stop the compiler. 
        time.sleep(refreshrate) 
        browser.refresh() 
        if i == 5:
            b =1
            print("break here")
    if b == 1:
        break
browser.close()
