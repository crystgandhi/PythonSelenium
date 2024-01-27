# Import necessary libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the first tab and navigate to a website
driver.get("https://the-internet.herokuapp.com/")

# Find the page title element using its tag name ("h1")
page_title = driver.find_element(By.TAG_NAME, "h1")

# Retrieve the text content of the page title
actual_message = page_title.text

# Highlight the page title element by changing its style temporarily
driver.execute_script("arguments[0].setAttribute('style','background:yellow; border: 2px solid red;');", page_title)

# Pause script execution for 3 seconds for visibility (optional)
time.sleep(3)

# Print the actual page title message
print(actual_message)

# Define the expected page title message
expected_message = "The Internet"

# Perform assertion to check if actual message matches expected message
if actual_message == expected_message:
    assert True
else:
    # Save a screenshot if assertion fails
    driver.save_screenshot(".\\Screenshots\\" + "title.png")
    assert False
