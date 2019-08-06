from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()
driver.find_element_by_name('fld_username').send_keys('Hello')

act = ActionChains(driver)
time.sleep(5)
# act.send_keys(Keys.CONTROL).send_keys('a').perform()
# act.send_keys(Keys.TAB).perform()
# time.sleep(5)
act.send_keys(Keys.SPACE).perform()
# time.sleep(5)
# act.send_keys(Keys.BACK_SPACE).perform()
time.sleep(5)
# driver.close()


