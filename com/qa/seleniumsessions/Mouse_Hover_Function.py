from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
driver.get('https://www.amazon.com')
driver.implicitly_wait(40)
element = driver.find_element_by_id('nav-link-accountList')

hover = ActionChains(driver).move_to_element(element)

hover.perform()

