from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import time

import unittest


class LoginTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

        def test_login(self):

            driver = self.driver
            facebookUsername = 'anam123khan@gmail.com'
            facebookPassword = '123anam'

            emailFieldID = 'email'
            passFieldID = 'pass'
            loginButtonXpath = '//input[@value="Log In"]'
            #fbLogoXpath = '(//a[contains(@href, "logo")])[1]'

            emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
            passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
            loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpth(loginButtonXpath))
            emailFieldElement.clear()
            emailFieldElement.send_keys(facebookUsername)
            passFieldElement.clear()
            passFieldElement.send_Keys(facebookPassword)
            loginButtonElement.click()
            #WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xapth(fbLogoXpath))

        def tearDown(self):
            self.driver.quit()

if __name__=='__main__':

    unittest.main()


