from selenium import webdriver
import time
import unittest
from time import sleep

# driver = webdriver.Firefox("C:\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\geckodriver.exe")


class TestParallel(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",desired_capabilities={"browserName": "Chrome"})
        self.driver = webdriver.Chrome('C:\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_one(self):
        driver = self.driver
        driver.get("http://www.yahoo.com")
        driver.maximize_window()
        sleep(5)

    def test_two(self):
        driver = self.driver
        driver.get("http://www.youtube.com")
        driver.maximize_window()
        sleep(5)

    def test_three(self):
        driver = self.driver
        driver.get("http://www.twitter.com")
        driver.maximize_window()
        sleep(5)

    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    unittest.main()
