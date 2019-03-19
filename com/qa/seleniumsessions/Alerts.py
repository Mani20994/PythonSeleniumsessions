from selenium import webdriver
import time

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get("http://demo.guru99.com/test/delete_customer.php")

driver.find_element_by_name("cusid").send_keys("123")
driver.find_element_by_name("submit").click()
time.sleep(5)
# alert = driver.switch_to.alert
# alert.accept()
# alert.dismiss()
# alert.send_keys("test")
driver.switch_to.alert.accept()
time.sleep(9)
# alert.dismiss()
