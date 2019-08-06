from selenium import webdriver
import time

driver = webdriver.Chrome("\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe")

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(5)

# Downloading Text File
driver.find_element_by_xpath(".//*[@id='textbox']").send_keys("testing download text file")
time.sleep(5)

# Generate file button
driver.find_element_by_xpath(".//*[@id='createTxt']").click()
time.sleep(2)

# Download file button
driver.find_element_by_xpath(".//*[@id='link-to-download']").click()
time.sleep(2)

# Downloading PDF file
driver.find_element_by_xpath(".//*[@id='pdfbox']").send_keys(" download text file")
time.sleep(3)

driver.find_element_by_xpath(".//*[@id='createPdf']").click()
time.sleep(5)

# Download file button
driver.find_element_by_xpath(".//*[@id='pdf-link-to-download']").click()
time.sleep(2)