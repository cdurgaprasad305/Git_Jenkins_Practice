from datetime import datetime
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

f = open("log_msg.txt", "a")
f.writelines("\n" + " ========================================")
ts = str(datetime.now())
f.writelines(ts)
f.writelines(" ========================================" + "\n")

driver = webdriver.Chrome()
driver.maximize_window()

rs = requests.get("https://practicetestautomation.com/practice-test-login")
f.writelines("Response Code : " + rs.text + "\n")
f.writelines("Status Code : " + str(rs.status_code) + "\n")


driver.get("https://practicetestautomation.com/practice-test-login")
driver.find_element(By.XPATH, "//*[@id='username']").send_keys("student")

# Finding Element using Name
driver.find_element(By.NAME, "password").send_keys("Password123**")
driver.find_element(By.XPATH, "//button[@id='submit']").click()

wait = WebDriverWait(driver, 10)  # WebDriverWait Explicit Wait
err_desc1 = wait.until(
    EC.text_to_be_present_in_element((By.ID, "error"), "Your password is invalid!")
)

# Finding Element using ID...
error_desc1 = driver.find_element(By.ID, "error").text
f.writelines(error_desc1 + "\n")

driver.find_element(By.XPATH, "//*[@id='username']").send_keys("student")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[@id='submit']").click()

# Finding Element using Class_Name
log_info = driver.find_element(By.CLASS_NAME, "post-title").text

f.writelines(log_info + "\n")

if log_info == "Logged In Successfully":
    print("Login Successful")
    f.writelines(log_info + "\n")
else:
    print("Login Failed")


links = driver.find_elements(By.TAG_NAME, "a")
# Print the href attributes of all links
for link in links:
    name = link.get_attribute("text")
    href = link.get_attribute("href")
    f.writelines(name + " -- " + href + "\n")

input("Press Enter to Close")
# Commit comments
