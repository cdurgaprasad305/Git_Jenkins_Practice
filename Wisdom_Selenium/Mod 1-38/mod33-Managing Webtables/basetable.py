# ----TODO---- Work on web tables
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers")

rows = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr")
print("No. of rows : " + str(len(rows)))  # for rows it should be /tr

columns = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td")
print("No. of columns : " + str(len(columns)))  # for Columns it should be /tr[1]/td

companyNames = driver.find_elements(
    By.XPATH, "//table[@class='dataTable']/tbody/tr/td[1]"
)
currentPrice = driver.find_elements(
    By.XPATH, "//table[@class='dataTable']/tbody/tr/td[4]"
)

for i in range(0, len(companyNames)):
    name = companyNames[i].text
    price = currentPrice[i].text
    # print(name + " --- " + price)
    if name == "Rajasthan Cylinders":
        print(name + " --- " + price)
        break

time.sleep(1)
driver.quit()

# OP:
# No. of rows : 2689
# No. of columns : 6
# Rajasthan Cylinders --- 41.00
