from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demoqa.com/text-box")
driver.implicitly_wait(3)
driver.maximize_window()
print(driver.title)
driver.find_element(By.ID, "userName").send_keys("Mr.Peter Haynes")
driver.find_element(By.ID,"userEmail").send_keys("PeterHaynes@toolsqa.com")
driver.find_element(By.ID, "currentAddress").send_keys("43 School Lane London EC71 9GO")
driver.find_element(By.ID, "currentAddress").send_keys(Keys.CONTROL + "A")
driver.find_element(By.ID, "currentAddress").send_keys(Keys.CONTROL + "C")
driver.find_element(By.ID, "permanentAddress").send_keys(Keys.CONTROL + "V")
