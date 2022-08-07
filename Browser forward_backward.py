from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/hakan/PycharmProjects/Drivers/chromedriver")
driver.get("http://google.com")
time.sleep(5)
print(driver.title) # Title of the page

driver.get("http://yahoo.com")
time.sleep(5)
print(driver.title) # Title of the page
print(driver.current_url)
driver.back()
print(driver.title)
driver.forward()
# print(driver.page_source)
print(driver.title)

driver.close()
