from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
browser.get("http://google.com")

elm = browser.find_element_by_link_text("About")
time.sleep(5)
elm.click()
time.sleep(3)
browser.back()
time.sleep(6)
browser.forward()
