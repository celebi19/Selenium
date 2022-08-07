
# file name syntax :  test_*.py or *_test.py
from selenium import webdriver
import pytest


class TestOrangeHR():
    # class name should start with Test

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/hakan/PycharmProjects/Drivers/chromedriver")
        driver.implicitly_wait(10)
        driver.maximize_window()
        #yield
        #driver.close()
        #driver.quit()
        #print("Test completed")

    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x = driver.title
        assert x == "OrangeHRM"


    def test_navigation(self,test_setup):
      #driver.find_element_by_id("quickLinkText").click()
     # driver.find_element_by_xpath(
        #  "//div[@id='dashboard-quick-launch-panel-menu_holder']/table/tbody/tr/td/div/a/span").click()
        driver.find_element_by_class_name("quickLaungeContainer").click()
        #driver.find_elements_by_class_name("quickLaungeContainer").click()

# ps : to comment out multiple lines: cmd + /





