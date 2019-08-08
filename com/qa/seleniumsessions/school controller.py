from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox("C:\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\geckodriver.exe")
driver.get("http://school.itechscripts.com")
driver.maximize_window()

driver.find_element_by_xpath(".//*[@id='username']").send_keys("school")
driver.find_element_by_xpath(".//*[@id='password']").send_keys("schoolp")
driver.find_element_by_xpath(".//*[@id='loginBtn']").click()


driver.find_element_by_xpath(".//*[@id='sidebar']/div[2]/div[2]/ul/li[4]/a").click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='sidebar']/div[2]/div[2]/ul/li[4]/ul/li/a").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@id='ToolTables_DataTables_Table_0_2']").click()
time.sleep(2)
driver.find_element_by_xpath("//embed[@id='ZeroClipboard_TableToolsMovie_3']").click()
time.sleep(10)
driver.find_element_by_xpath("//a[@id='ToolTables_DataTables_Table_0_2']").click()
time.sleep(2)
driver.find_element_by_xpath("//embed[@id='ZeroClipboard_TableToolsMovie_3']").click()
time.sleep(2)

act = ActionChains(driver)
time.sleep(5)
act.send_keys(Keys.ENTER).perform()
