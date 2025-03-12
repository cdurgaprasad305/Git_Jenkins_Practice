import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)

sports_block = driver.find_element(By.XPATH,"//*[@id='true']/div[5]/div[2]/ul")  # unique elements
linklist = sports_block.find_elements(By.TAG_NAME,"a")  # multiple elements
print(len(linklist))

for i in range(0, len(linklist)):
    linktext = linklist[i].text
    print(linktext)


time.sleep(5)
driver.quit()
