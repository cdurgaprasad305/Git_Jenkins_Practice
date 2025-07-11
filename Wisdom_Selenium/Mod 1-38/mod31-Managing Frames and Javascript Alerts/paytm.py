import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://paytm.com/")

frames = driver.find_elements(By.TAG_NAME,"iframe")
print(len(frames))
time.sleep(5)

driver.find_element(By.XPATH,"//div[text()='Log In/Sign Up']").click()
driver.switch_to.frame(0)
print(driver.find_element(By.XPATH,"//*[@id='main-container']/div/div/div/div/div[1]/div/div/div[1]/ul/li[1]/span[2]").text)
driver.switch_to.default_content()

time.sleep(5)
driver.quit()
