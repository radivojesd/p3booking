from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(5)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://www.booking.com/")
time.sleep(10)
action = ActionChains(driver)
search_bar = driver.find_element_by_id("ss")
search_bar.click()
time.sleep(5)
search_bar.send_keys("Paris")
time.sleep(5)
paris = driver.find_element_by_xpath("//span[contains(.,'ParisIle de France, France')]").click()
time.sleep(5)
driver.find_element_by_class_name("bui-calendar__control.bui-calendar__control--next").click()
driver.find_element_by_class_name("bui-calendar__control.bui-calendar__control--next").click()
driver.find_element_by_class_name("bui-calendar__control.bui-calendar__control--next").click()
time.sleep(5)
driver.find_element_by_xpath("(//span[@aria-hidden='true'][contains(.,'19')])[2]").click()
time.sleep(5)
driver.find_element_by_xpath("(//span[@aria-hidden='true'][contains(.,'25')])[2]").click()
time.sleep(5)
driver.find_element_by_class_name("xp__guests__count").click()
time.sleep(5)
driver.find_element_by_xpath("//button[contains(@aria-label,'Increase number of Children')]").click()
time.sleep(5)
select = Select(driver.find_element_by_name("age"))
select.select_by_value("3")
time.sleep(5)
driver.find_element_by_xpath("//span[contains(.,'Search')]").click()
time.sleep(10)
driver.find_element_by_partial_link_text("Holida").click()
time.sleep(10)
driver.quit()