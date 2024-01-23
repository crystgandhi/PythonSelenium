import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(3)

time.sleep(3);
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(5)

element_to_capture = driver.find_element(By.CSS_SELECTOR,".inventory_item:nth-child(6)")
element_to_capture.screenshot("screenshot.png")
driver.save_screenshot("screenshot.png")
