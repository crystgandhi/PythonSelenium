from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.saucedemo.com")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollBy(0,500);")
driver.get_screenshot_as_file("screen.png")
print("Executed")
