from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
driver.get("http://www.theTestingWorld.com/testings")

driver.maximize_window()

#Enter data into the Textbox
# driver.find_element_by_name("fld_username").send_keys("helloworld")
# time.sleep(5)
# driver.find_element_by_xpath("//input[@placeholder='myusername@gmail.com']").send_keys("testingworldindia@gmail.com")
# time.sleep(5)
# driver.find_element_by_name("fld_password").send_keys("abcd123")
# time.sleep(5)
# driver.find_element_by_name("fld_cpassword").send_keys("abcd123")
# time.sleep(5)


#1.Select by Index
obj = Select(driver.find_element_by_name("sex"))
# time.sleep(5)
#
obj.select_by_index(1)

#2.Select by Value
#obj.select_by_value("2")

#3.Select by Visible Text
obj.select_by_visible_text("Female")
time.sleep(5)

