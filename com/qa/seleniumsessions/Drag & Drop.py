import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chromedriver = "\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://jqueryui.com/draggable/#sortable")

driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))

source = driver.find_element_by_id("draggable")
target = driver.find_element_by_css_selector("#sortable>li:nth-child(3)")

mouse = ActionChains(driver).drag_and_drop(source, target)
mouse.perform()

time.sleep(5)
