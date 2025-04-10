from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("file:///E:/Python2024/Example.html")


driver.find_element(By.XPATH,"//input[@id='male' and @type='radio']").click()
cm = driver.find_element(By.XPATH,"//button[@id='click-me-button']")

# tc = driver.find_elements(By.)


input("Press Enter Key..")
driver.quit()