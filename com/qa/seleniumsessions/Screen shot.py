from selenium import webdriver

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://lms.latitudelearning.com")
driver.maximize.window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("C:\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Store Screenshots\\LatitudeLearning.png")
driver.find_element_by_id("ctlTemplate_regMainBody_ctlLogin_sID").send_keys("MANI1")
driver.find_element_by_name("ctlTemplate$regMainBody$ctlLogin$sPassword").send_keys("Minds123")
driver.find_element_by_id("ctlTemplate_regMainBody_ctlLogin_cmdLogin").click()
driver.get_screenshot_as_file("C:\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Store Screenshots\\LatitudeLearning1.png")

driver.quit()
