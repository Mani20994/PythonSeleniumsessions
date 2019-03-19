from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get("http://www.theTestingWorld.com/testings")

driver.maximize_window()

#fetching title
print("Title of page is  " + driver.title)

#Fetch URL of page
print("Page URL is" + driver.current_url)

#Fetch Complete page HTML
print("***********************************************")
print(driver.page_source)
