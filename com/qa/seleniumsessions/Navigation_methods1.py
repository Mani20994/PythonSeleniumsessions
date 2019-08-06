from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
browser.get("https://jqueryui.com/checkboxradio/")

elm = browser.find_element_by_xpath("//a[contains(text(),'Themes')]")
time.sleep(5)
elm.click()
time.sleep(3)
browser.back()
time.sleep(6)
browser.forward()