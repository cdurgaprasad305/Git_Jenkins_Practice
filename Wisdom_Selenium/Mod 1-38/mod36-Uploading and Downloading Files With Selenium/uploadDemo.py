
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://filebin.net/")
upload_button = driver.find_element(By.ID, "fileField")
# webdriver.ActionChains(driver).click(upload_button).perform()
upload_button.send_keys("C:/Users/Desktop/flowers.jfif")


