import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
time.sleep(5)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
time.sleep(5)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
driver.switch_to.alert.send_keys("Hello")
time.sleep(5)
driver.switch_to.alert.accept()