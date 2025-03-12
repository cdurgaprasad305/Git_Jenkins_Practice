import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)

part1 = "//*[@id='repo']/div[3]/div[2]/ul/li["
part2 = "]/a"


for i in range(1, 8):
    link = driver.find_element(By.XPATH,(part1 + str(i) + part2))
    print("---Dynamic Xpath: ",(part1 + str(i) + part2))
    linktext = link.text
    print(linktext)
time.sleep(5)
driver.quit()
