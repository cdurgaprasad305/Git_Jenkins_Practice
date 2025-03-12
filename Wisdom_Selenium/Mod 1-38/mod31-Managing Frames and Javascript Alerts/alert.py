from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.ID,"login1").send_keys("hello")

proceedBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "proceed")))
proceedBtn.click()

a = WebDriverWait.until(EC.alert_is_present())
print(a.text)
# a.accept()
a.dismiss()
