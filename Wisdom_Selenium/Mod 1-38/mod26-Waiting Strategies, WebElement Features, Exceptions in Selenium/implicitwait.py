import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://zoho.com")
# dynamic waiting technique - implicit wait-global wait driver.find
driver.implicitly_wait(10)
# Global Wait
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a[4]").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/a[4]").click()
# time.sleep(5)       #pause
user_name_textbox = driver.find_element(By.ID,"login_id")
user_name_textbox.send_keys("hello")
print(user_name_textbox.get_attribute("name"))


time.sleep(5)
driver.quit()
