from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get("http://www.theTestingWorld.com/")
driver.maximize_window()
act = ActionChains(driver)

#click operation
act.click().perform()
act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

#Context Click (right click)
act.context_click().perform()
act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

act.double.click().perform()
act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

driver.close()
