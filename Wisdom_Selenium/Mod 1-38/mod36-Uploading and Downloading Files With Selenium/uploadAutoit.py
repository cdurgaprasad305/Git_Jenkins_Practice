from selenium import webdriver
import subprocess

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://filebin.net/")
upload_button = driver.find_element(By.ID,"fileField")

webdriver.ActionChains(driver).click(upload_button).perform()
subprocess.Popen(["D:/eclipse/Modules/module21/upload.exe"])
