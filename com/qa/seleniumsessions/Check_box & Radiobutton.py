import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")

driver.get("https://jqueryui.com/checkboxradio/")
driver.maximize_window()
driver.implicitly_wait(10)

#Iframe
driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))

#Radio button
driver.find_element_by_xpath("//label[contains(text(),'Paris')]").click()
time.sleep(1)

#Checkbox
driver.find_element_by_xpath("//label[contains(text(),'4 Star')]").click()
time.sleep(1)
driver.find_element_by_xpath("//label[contains(text(),'5 Star')]").click()
time.sleep(1)

driver.find_element_by_xpath("//label[contains(text(),'2 Double')]").click()
time.sleep(1)
driver.find_element_by_xpath("//label[contains(text(),'2 Queen')]").click()
time.sleep(1)

driver.switch_to.frame(driver.find_element_by_xpath("//div[@id='container']"))


