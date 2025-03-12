from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None
browserName = ""

if browserName == "chrome":
    driver = webdriver.Chrome()

elif browserName == "firefox":
    driver = webdriver.Firefox()

elif browserName == "ie":
    driver = webdriver.Ie()

elif browserName == "edge":
    driver = webdriver.Edge()

else:
    print("no browser specified")

driver.maximize_window()
driver.get("https://www.facebook.com/")

# textbox = driver.find_element_by_name("firstname")
textbox = driver.find_element(By.NAME, "firstname")
textbox.send_keys("hello")

# emailtextbox = driver.find_element_by_id("email")
emailtextbox = driver.find_element(By.ID, "email")
emailtextbox.send_keys("hello")

# firstname = driver.find_element("name", "firstname")
firstname = driver.find_element(By.NAME, "firstname")
firstname.send_keys("hello")
