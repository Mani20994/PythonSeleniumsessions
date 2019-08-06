from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
driver.get('https://wikipedia.org')
driver.maximize_window()
elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(5)
elm.send_keys(Keys.PAGE_UP)
time.sleep(5)
elm.send_keys(Keys.HOME)

# driver.close()
