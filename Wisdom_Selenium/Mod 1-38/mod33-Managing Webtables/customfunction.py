# ----TODO---- Work on web tables

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

name = "Rajasthan Cylinders"


def get_row_num_by_name(name):
    rows = driver.find_elements(
        By.XPATH, "//table[@class='dataTable']/tbody/tr"
    )  # Rows :14
    for i in range(0, len(rows)):
        cells = rows[i].find_elements(By.XPATH, "td")  # Columns : 6
        for j in range(0, len(cells)):
            cell = cells[j].text
            if cell == name:
                return i + 1  # loop Exit


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers")

rowNum = get_row_num_by_name(name)
print("Row num for " + name + " is : " + str(rowNum))

currentPrice = driver.find_element(
    By.XPATH, "//table[@class='dataTable']/tbody/tr[" + str(rowNum) + "]/td[4]"
)
print("Price is : " + currentPrice.text)

cells = driver.find_elements(
    By.XPATH, "//table[@class='dataTable']/tbody/tr[" + str(rowNum) + "]/td"
)
rowdata = ""
for i in range(0, len(cells)):
    cellData = cells[i].text
    print(cellData)
    rowdata = rowdata + " --- " + cellData
time.sleep(1)
print("\nComplete row data :")
print(rowdata.lstrip(" --- "))
driver.quit()


# OP:
# Row num for Rajasthan Cylinders is : 14
# Price is : 41.00
# Rajasthan Cylinders
# X
# 34.81
# 41.00
# + 17.78
# Buy  |  Sell
#
# Complete row data :
# Rajasthan Cylinders --- X --- 34.81 --- 41.00 --- + 17.78 --- Buy  |  Sell
