import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//a[normalize-space()='File Upload']").click()
driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("C://Users/Nikil/Desktop/History/1.png")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='file-submit']").click()
print(driver.find_element(By.XPATH, "//h3[normalize-space()='File Uploaded!']").text)
