import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://news18.com")
# dynamic waiting technique - implicit wait-global wait driver.find
driver.implicitly_wait(10)

# home_link = driver.find_element_by_xpath("//*[@id='mc_mainWrapper']/nav/div/ul[2]/li[1]/a")
home_link = driver.find_element(By.ID, "mc_mainWrapper")
print(home_link.is_displayed())
print(home_link.is_enabled())
print("- - - - - - - - - - -")

# india_link = driver.find_element_by_xpath("//*[@id='mc_mainWrapper']/nav/div/div[2]/div[2]/ul/li[4]/a")
india_link = driver.find_element(By.ID, "mc_mainWrapper")
print(india_link.is_displayed())
print(india_link.is_enabled())

time.sleep(5)
driver.quit()
