from selenium import webdriver
import time

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
driver.get("https://lms.latitudelearning.com")
driver.maximize_window()

#login
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_sID']").send_keys("MANI1")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_sPassword']").send_keys("Minds123")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_cmdLogin']").click()
time.sleep(2)

#Admin link
driver.find_element_by_xpath("//a[@class='header-admin']").click()
time.sleep(2)
#click on course
driver.find_element_by_xpath("//a[@id='ctlTemplate_regLeftNav_ctlMenuUser_mnuUser_MenuSection4_SectionHeader']").click()
time.sleep(2)
#click on add course
driver.find_element_by_xpath("//a[@id='ctlTemplate_regLeftNav_ctlMenuUser_mnuUser_MenuSection4_SectionItemsRepeater_ctl01_SectionItem']").click()

#choose organization
driver.find_element_by_xpath("//a[@id='ctlTemplate_regMainBody_ctlCourseGeneralInfoEdit_ctl01_Highest_org_multi_selection1_ctlOwnerOrgPicker_lnkPicker']").click()

#Switching from parent window to child window
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlSearchList_ctlSearchList_ctlSearchPanel_btnSearch']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlSearchList_ctlSearchList_ctlSearchList_Results_ctl01_lnkAdd']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlBasket_cmdCheckout']").click()
time.sleep(2)

#switching back to parent window
driver.switch_to.window(driver.window_handles[0])

#Code
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlCourseGeneralInfoEdit_ctl01_txtCode']").send_keys("CSE11")