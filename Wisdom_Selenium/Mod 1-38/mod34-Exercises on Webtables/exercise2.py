from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name = "Jenette Caldwell"  # present on page 6 row no. 7


# common utility functions
def elementPresent(locator, locatorType):
    # present : true
    # not present : false
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_all_elements_located((locatorType, locator)))
        wait.until(EC.visibility_of_all_elements_located((locatorType, locator)))
    except Exception:
        return False
    return True


def getRowNumByName(name):
    a = driver.find_elements(By.XPATH, "//*[@id='dtBasicExample']/tbody/tr")
    for i in range(0, len(a)):
        row = a[i]
        column = row.find_elements(By.TAG_NAME, "td")
        for j in range(0, len(column)):
            if (column[j].text) == name:
                return i + 1
    return -1


# main script
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-bookmarks")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://mdbootstrap.com/docs/jquery/tables/pagination/")

page = 1
# rowNum = None
rowNum = getRowNumByName(name)
while rowNum == -1:
    if elementPresent("//li[@class='paginate_button page-item next']/a", "xpath"):
        driver.find_element(
            By.XPATH, "//li[@class='paginate_button page-item next']/a"
        ).click()
        page = page + 1
        rowNum = getRowNumByName(name)
    else:
        print("Name not found")

if rowNum != -1:
    print("Given name '" + name + "'" + " found")
    print("Page number - " + str(page))
    cellData = driver.find_element(
        By.XPATH, "//*[@id='dtBasicExample']/tbody/tr[" + str(rowNum) + "]/td[3]"
    )
    #     print("Age is : "+age.text)
    print(cellData.text)
time.sleep(1)
driver.quit()
