from selenium import webdriver
import time

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get('https://www.facebook.com/')

driver.maximize_window()

#driver.find_element_by_class_name('caret').click()

driver.find_element_by_name('birthday_day').send_keys('20')
time.sleep(5)

driver.find_element_by_name('birthday_month').send_keys('Sept')
time.sleep(5)
driver.find_element_by_name('sex').click()

# driver.close()

#action_chains = ActionChains(driver)
#action_chains.double_click(element).perform()

