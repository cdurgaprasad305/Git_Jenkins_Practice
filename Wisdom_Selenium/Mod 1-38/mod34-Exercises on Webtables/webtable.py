from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

name = "Kaur"
# rowNumber = -1


def get_row_num_by_name(name):
    rows = driver.find_elements(By.XPATH, "//*[@id='dtBasicExample']/tbody/tr")
    for i in range(0, len(rows)):
        row = rows[i]
        cells = row.find_elements(By.TAG_NAME, "td")
        for j in range(0, len(cells)):
            if (cells[j].text) == name:
                return i + 1
    return -1


def isElementPresent(locator, locatorType):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_all_elements_located((locatorType, locator)))
        wait.until(EC.visibility_of_all_elements_located((locatorType, locator)))
    except Exception as e:
        print("Exception :", e)
        return False
    return True


op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")
op.add_argument("--start-maximized")
driver = webdriver.Chrome(options=op)
driver.implicitly_wait(10)
driver.get("https://mdbootstrap.com/docs/jquery/tables/pagination/")

page = 1
rowNumber = get_row_num_by_name(name)
while rowNumber == -1:
    if isElementPresent("//*[@id='dtBasicExample_next']/a", "xpath"):
        driver.find_element(By.XPATH, "//*[@id='dtBasicExample_next']/a").click()
        page = page + 1
        rowNumber = get_row_num_by_name(name)
    else:
        print("name not found")
        break
if rowNumber != -1:
    print("Page no. : " + str(page))
    print("Row no. : " + str(rowNumber))
    age = driver.find_element(
        By.XPATH, "//*[@id='dtBasicExample']/tbody/tr[" + str(rowNumber) + "]/td[4]"
    )
    print("age is : " + age.text)
else:
    print("code issue.....")
