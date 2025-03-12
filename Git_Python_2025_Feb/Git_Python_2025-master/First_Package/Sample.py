# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone X"})
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com")





input("Press Enter to Close")
driver.quit()