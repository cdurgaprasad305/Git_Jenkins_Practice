from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://flipkart.com")

driver = webdriver.Firefox()
driver.get("https://flipkart.com")

path = "C:\\Webdriver\\msedgedriver.exe"
driver = webdriver.Edge(executable_path=path)
driver.get("https://flipkart.com")

driver = webdriver.Ie()
driver.get("https://flipkart.com")
