

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://demoqa.com/")
print(driver.current_url)
print(driver.title)
driver.back()
print(driver.current_url)
driver.refresh()
driver.forward()
print(driver.current_url)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("John")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Smith")
driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("3595803449")
driver.find_element(By.XPATH, "//*[@id='subjectsContainer']/div/div[1]").send_keys("Application")

try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='subjectsContainer']/div/div[1]")
     ))
    # Proceed with further actions after the element is clickable
    element.send_keys("Application")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()


