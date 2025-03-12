import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(
    "https://www.linkedin.com/jobs/jobs-in-sydney-ns?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0"
)
driver.implicitly_wait(10)

radiobuttons = driver.find_elements(By.ID,"sortBy")
print("Total no. of radio buttons : ",(len(radiobuttons)))

for i in range(0, len(radiobuttons)):
    check = radiobuttons[i].get_attribute("checked")
    print("----Check Status:",check)

driver.save_screenshot("radiobuttons.png")

time.sleep(5)
driver.quit()
