from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\Drivers\\chromedriver.exe')
driver.get('https://www.demo.iscripts.com/netmenus/mrml/cms')
driver.implicitly_wait(40)
driver.maximize_window()

#fetching title
print("Title of page is  " + driver.title)

driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("inputPassword").send_keys("admin")
driver.find_element_by_name("submit").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//a[@href='https://www.demo.iscripts.com/netmenus/mrml/cms?section=restaurant']").click()
driver.implicitly_wait(60)

#add record
driver.find_element_by_xpath("//a[@class='addrecord btn btn-info']").click()

#Restaurant
driver.find_element_by_id("venue_name").send_keys("Paradise")

#Description
driver.find_element_by_id("venue_description").send_keys("Good restaurant")

#Address
driver.find_element_by_id("venue_address_by_user").send_keys("Hyderabad")

#Zip
driver.find_element_by_id("zip_code").send_keys("1234")
driver.implicitly_wait(60)

#Phone
driver.find_element_by_id("phone").send_keys("9876543218")
driver.implicitly_wait(60)

#Cuisines
driver.find_element_by_id("tags").send_keys("Fast food")
driver.implicitly_wait(60)

#Paymenty option
driver.find_element_by_name("is_payment_direct").click()

#take out
driver.find_element_by_id("takout").click()
driver.implicitly_wait(60)

#reservation
driver.find_element_by_id("reservation").click()
driver.implicitly_wait(60)    

#restaurant owner
driver.find_element_by_id("created_by").send_keys("William Brown")
driver.implicitly_wait(60)

#manager
driver.find_element_by_id("store_manager").send_keys("Robert")

#manager email
driver.find_element_by_id("store_manager_email").send_keys("robert@gamil.com")
driver.implicitly_wait(60)

#minimum order amount
driver.find_element_by_id("min_order_amount").send_keys("1000")
driver.implicitly_wait(60)

#sales tax
driver.find_element_by_id("sales_tax").send_keys("10")

#Delivery fee
driver.find_element_by_id("delivery_fee").send_keys("5")
driver.implicitly_wait(60)

#Rate of commission
driver.find_element_by_id("commission").send_keys("8")
driver.implicitly_wait(60)

#save
driver.find_element_by_id("jqSubmitForm").click()
driver.implicitly_wait(60)

#add cuisines
driver.find_element_by_xpath("//a[contains(text(),'Cuisines')]").click()
driver.implicitly_wait(60)

#add record
driver.find_element_by_xpath("//a[@class='addrecord btn btn-info']").click()
driver.implicitly_wait(60)

#tag
driver.find_element_by_id("tag_name").send_keys("French drinks")
driver.implicitly_wait(60)

#Cuisines image
driver.find_element_by_xpath("//input[@id='tag_image']").send_keys("C:\\Users\\Nxt\\Pictures\\Restaurant.jpg")
driver.implicitly_wait(60)

#save
driver.find_element_by_id("jqSubmitForm").click()
driver.implicitly_wait(60)
