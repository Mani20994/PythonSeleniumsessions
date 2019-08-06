from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get("http://automationpractice.com")

driver.maximize_window()

#fetching title
print("Title of page is  " + driver.title)
time.sleep(5)

#Fetch URL of page
print("Page URL is" + driver.current_url)
time.sleep(5)

# #Fetch Complete page HTML
# print("***********************************************")
# print(driver.page_source)
# time.sleep(5)
# driver.quit()

