import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")

driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(4)

driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))
source = driver.find_element_by_xpath("//div[@id='draggable']")
time.sleep(5)
target = driver.find_element_by_xpath("//div[@id='droppable']")
time.sleep(5)
mouse = ActionChains(driver).drag_and_drop(source,target)
mouse.perform()

time.sleep(5)