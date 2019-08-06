from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
driver.get('https://www.amazon.com')
driver.maximize_window()
driver.implicitly_wait(20)

element = driver.find_element_by_id('nav-link-accountList')
driver.implicitly_wait(20)

hover = ActionChains(driver).move_to_element(element)
driver.implicitly_wait(40)
hover.perform()
driver.close()

