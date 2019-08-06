import time
import os
from selenium import webdriver

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")


driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(5)
driver.find_element_by_id("file-upload").send_keys('C:\\Users\\Nxt\\Documents\\Smoke Testing Doc.docx')
time.sleep(5)
driver.find_element_by_id("file-submit").click()

time.sleep(3)
