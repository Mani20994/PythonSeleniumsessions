from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")

driver.get("https://lms.latitudelearning.com")
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_sID']").send_keys("MANI1")
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_sPassword']").send_keys("Minds123")
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_cmdLogin']").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//a[@title='Administration']").click()
driver.find_element_by_xpath("//a[@href='javascript:void(0)'][contains(text(),'Courses')]").click()
driver.find_element_by_xpath("//a[@id='ctlTemplate_regLeftNav_ctlMenuUser_mnuUser_MenuSection4_SectionItemsRepeater_ctl01_SectionItem']").click()
driver.find_element_by_xpath("//a[contains(text(),'Choose Organizations')]").click()
print(driver.current_window_handle)
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlSearchList_ctlSearchList_ctlSearchPanel_btnSearch']").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@value='Add']").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlBasket_cmdCheckout']").click()
driver.implicitly_wait(20)
if driver.title == "Owner Organization Picker":
    driver.implicitly_wait(50)
    driver.close()
    driver.implicitly_wait(50)
    for handle in handles:
        driver.switch_to.default_content(handles)
        driver.implicitly_wait(50)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlCourseGeneralInfoEdit_ctl01_txtCode']").send_keys("CSE01")


