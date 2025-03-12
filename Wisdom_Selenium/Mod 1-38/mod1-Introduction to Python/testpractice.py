import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(5)
driver.forward()

# - If the browser does not have forward navigation history
# (e.g., after just opening a URL or not using `driver.back()` beforehand),
# calling `driver.forward()` will simply do nothing. Selenium
# does not throw an error or exception in this case.
# - It silently ignores the request if there is no "forward" action to perform.


print("--Execution completed--")