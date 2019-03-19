import time
import os
from selenium import webdriver

chromedriver = "\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


driver.get("http://the-internet.herokuapp.com/upload")

driver.find_element_by_id("file-upload").send_keys('‪‪C:\\Users\\Nxt\\Downloads\\Facebook Prg.txt')
driver.find_element_by_id("file-submit").click()

time.sleep(3)
