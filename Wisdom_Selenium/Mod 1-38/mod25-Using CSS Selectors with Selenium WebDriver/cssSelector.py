
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")

# driver.find_element_by_class_name("._2zrpKA._1dBPDZ").send_keys("123")
# driver.find_element_by_css_selector("form[autocomplete=on] > div:nth-child(1) > input").send_keys("123")

driver.find_element(By.CSS_SELECTOR, "form[autocomplete=on] > div:nth-child(1) > input").send_keys("123")