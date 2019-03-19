from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get('https://www.facebook.com/')

#driver.find_element_by_class_name('caret').click()
driver.implicitly_wait(40)
driver.find_element_by_name('birthday_day').send_keys('20')
driver.implicitly_wait(40)

driver.find_element_by_name('birthday_month').send_keys('Sept')
driver.implicitly_wait(40)
driver.find_element_by_name('sex').click()

#action_chains = ActionChains(driver)
#action_chains.double_click(element).perform()

