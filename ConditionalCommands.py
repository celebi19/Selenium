from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/hakan/PycharmProjects/Drivers/chromedriver")
driver.get("https://google.com/")
time.sleep(5)
print(driver.title) # Title of the page
assert "Google" in driver.title

# driver.find_element_by_id("fakebox-input").send_keys("hakan kilic")
search_button = driver.find_element_by_name("btnK")
print(search_button.is_enabled())  # returns True/False based on the element's status
print("Search button status:", search_button.is_displayed())  # returns True/False based on the element's status
# if want to add someting in print statement, the it in " " then use comma
#  the useage of "is selected " is the same as "is displayed, is enable"

"""
If theere are 2 elements with same type, name, but their values are different then use CSS selector.
1st element : input type = radio, name = tripType, value = roundTrip
2nd element : input type = radio, name = tripType, value = oneway

use below command to select the element
driver.find_elementP_by_css_selector("input[value=roundtrip]")
"""
#send.keys can be used like this
# searchbutton.send_keys("hakan kilic")

"""
To clear a box use below command then enter a text into the box

driver.find_element(By_ID,"FOO").clear()
driver.find_element(By_ID,"FOO").send_keys("abc...")

"""
"""
    WORKING WITH TEXT BOXES
status = driver.find_element(By.ID,'FOO').is_displayed()
print("Displayed or not:" , status)  # True or False

How to provide values into text box
driver.find_element(By,ID,'FOO').send_keys("abc")
or 
driver.find_element_by_id("foo").send_keys("abc")
"""

# CHECK BOXES and RADIO BUTTONS
# driver.find_elements_by_id("foo").click()

# DROP DOWNS
#import select class as follow
# from selenium.webdriver.support.ui. import Select
# element = driver.find_element_by_id("foo")
# drp = Select(element)  # use Select class
# select by visible text
# drp.select_by_visible_text('abc1')
#  select by index
# drp.select_by_index(2)
# select by value
# drp.select_by_value("abc2")
# To count the options in the dropdown use len
# print(len(drp.options))

"""
capture all options and print as an output

all_options = drp.options
for option in all_options:
    print(option.text)
""""
"""
Working with links
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present",len(links)) # prints how many links present
for links in links:
    print(link.test)  # prints all links
    
Clicking on links
driver.find_element_by_link_text("foo").click 
         or 
driver.find_elements_by_partial_link_text("fo").click        
         

"""
"""
WORKING WITH ALERTS
import time
time.sleep (5)
driver.switch_to_alert().accept()   # closes alert window using OK button
driver.switch_to_alert().dismiss()  # closes alert window using CANCEL button
"""
""" WORKING WITH FRAMES
Assume there are 3 freames on the same page.
First find the frame name by inspecting the page 
driver.switch_to.frame("foo")  # first frame
then find the link in the frame
driver.find_element_by_link_text("foo).click
time.sleep(5)
then go to main frame in order to go to 2nd frame

driver.switch_to_default_content()  # goes to default page 

driver.find_element_by_link_text("foo2).click  # second frame
driver.find_element_by_link_text("abc).click
time.sleep(5)

driver.switch_to_default_content()  # goes to default page 
driver.find_element_by_link_text("foo3).click  # third frame
driver.find_element_by_link_text("xyz).click

"""

driver.quit()

driver.switch_to_window(handle)

driver.execute_script()
