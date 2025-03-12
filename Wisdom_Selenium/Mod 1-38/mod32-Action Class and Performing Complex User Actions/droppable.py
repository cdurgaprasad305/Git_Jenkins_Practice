# ---TODO---
# Study in details in action chain class and methods

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
frames = driver.find_elements(By.TAG_NAME, "iframe")
print("No. of  frames are : " + str(len(frames)))

driver.switch_to.frame(0)
drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")

webdriver.ActionChains(driver).drag_and_drop(drag, drop).perform()
