import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://www.saucedemo.com")
driver.implicitly_wait(3)
driver.maximize_window()
time.sleep(5)
print(driver.title)