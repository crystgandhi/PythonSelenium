
import time

from selenium import webdriver
# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the first tab and navigate to a website
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)
# Open a new tab using JavaScript (Ctrl+T shortcut)
driver.execute_script("window.open('', '_blank');")
time.sleep(3)
# Switch to the second tab
driver.switch_to.window(driver.window_handles[1])
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.window_handles[1])

# Open another tab using JavaScript
driver.execute_script("window.open('', '_blank');")

# Switch to the third tab
driver.switch_to.window(driver.window_handles[2])
driver.get("https://the-internet.herokuapp.com/windows/new")
print(driver.window_handles[2])
# Close the third tab
driver.close()
time.sleep(3)
# Switch back to the second tab
driver.switch_to.window(driver.window_handles[1])

# Perform actions in the second tab
# ...

# Close the remaining tabs
driver.close()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
print(driver.window_handles[0])
driver.close()

# Quit the WebDriver
driver.quit()