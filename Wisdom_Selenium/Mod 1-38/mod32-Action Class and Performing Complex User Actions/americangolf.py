from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randint

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.americangolf.co.uk/")
e = driver.find_element(By.ID, "//*[@id='header-navigation']/div[1]/ul/li[3]/a")

webdriver.ActionChains(driver).move_to_element(e).perform()
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "CLOTHFOOTW_1")))

links = element.find_elements(By.TAG_NAME, "a")
print("No. of links : " + str(len(links)))

l = links[randint(0, len(links))]
l.click()
# time.sleep(5)
# driver.quit()
