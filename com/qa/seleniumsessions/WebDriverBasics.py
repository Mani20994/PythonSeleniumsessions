from selenium import webdriver
#from selenium.webdriver.common.desired capabilities import DesiredCapabilities

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")


#Caps = DesiredCapabilities.FIREFOX
#Caps["marionetde"]=True
#Caps["binary"]=

#driver = webdriver.Firefox("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\geckodriver.exe")

driver.get("https://facebook.com")

title = driver.title

print(title)

#assert "log in or sign up" in title

driver.find_element_by_name("email").send_keys("abc@gamil.com")
driver.find_element_by_name("pass").send_keys("1234")

driver.quit()

