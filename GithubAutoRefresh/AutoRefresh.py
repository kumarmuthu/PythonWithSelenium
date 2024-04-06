"""
AutoRefresh
"""

__version__ = "2019.11.15.01"
__author__ = "Muthukumar Subramanian"

from selenium import webdriver
import time

# set webdriver path here it may vary
browser = webdriver.Chrome()

website_URL = "https://github.com/kumarmuthu/PythonWithSelenium"
browser.get(website_URL)
browser.maximize_window()

for i in range(1, 6):
    time.sleep(2)
    browser.refresh()
    if i == 5:
        print("Break here")
        break

browser.close()
