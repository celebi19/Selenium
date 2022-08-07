from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="/Users/hakan/PycharmProjects/Drivers/chromedriver")
# driver = webdriver.Firefox(executable_path=" enter path here")
# driver = webdriver.Ie(executable_path=" enter path here")
# driver.get("http://newtours.demoaut.com/")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) # Title of the page
print(driver.current_url)
# print(driver.page_source)
driver.close()
