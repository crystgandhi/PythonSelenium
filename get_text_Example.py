
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(3)
print(driver.find_element(By.TAG_NAME, "h1").text)