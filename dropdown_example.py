import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Dropdown']").click()
driver.find_element(By.XPATH, "//select[@id='dropdown']").send_keys("Option 2")
time.sleep(5)