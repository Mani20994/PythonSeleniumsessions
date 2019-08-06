from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.implicitly_wait(40)

driver.find_element_by_xpath("//a[@title='Log in to your customer account']").click()
driver.find_element_by_id("email").send_keys("ra123@gmail.com")
driver.find_element_by_class_name("is_required validate account_input form-control").send_keys("Minds123")
driver.find_element_by_xpath("//p[@class='submit']//span[1]").click()


