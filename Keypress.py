import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//*[@id='content']/ul/li[31]/a").send_keys(Keys.ENTER);
time.sleep(3);