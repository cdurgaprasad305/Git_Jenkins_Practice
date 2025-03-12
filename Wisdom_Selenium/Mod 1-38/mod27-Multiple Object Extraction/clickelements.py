import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def element_present(locatorType, locator):
    # present = true
    # not present = false

    if locatorType == "xpath":
        element = driver.find_element(By.XPATH, locator)
    elif locatorType == "cssSelector":
        element = driver.find_element(By.CSS_SELECTOR, locator)
    elif locatorType == "id":
        element = driver.find_element(By.ID, locator)
    elif locatorType == "name":
        element = driver.find_element(By.NAME, locator)
    elif locatorType == "className":
        element = driver.find_element(By.CLASS_NAME, locator)
    else:
        element = driver.find_element(By.TAG_NAME, locator)

    if element == 0:
        return False
    else:
        return True


driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)
# maintab = driver.find_element_by_xpath("//*[@id='mc_mainWrapper']/nav/div/ul[2]")  #unique elements
# linklist = maintab.find_elements_by_tag_name("a")      #multiple elements
# print(type(linklist))
# print(len(linklist))

part1 = "//*[@id='mc_mainWrapper']/nav/div/ul[2]/li["
part2 = "]/a"

i = 2
while element_present("xpath", part1 + str(i) + part2):
    link = driver.find_element_by_xpath(part1 + str(i) + part2)
    linktext = link.text
    print(linktext)
    link.click()
    print(driver.title)
    time.sleep(5)
    driver.back()  # no runtime error...
    i = i + 1
else:
    print("No more elements found")

# you can use an `else:` condition in a `while` loop in Python.
# The `else:` block in a `while` loop runs after the loop exits,
# but only if the loop was not terminated by a `break` statement.
# This means the `else:` block is executed when the `while` loop's condition becomes `False`.

time.sleep(5)
driver.quit()

# - If the browser does not have forward or backward navigation history
# (e.g., after just opening a URL or not using `driver.back()` beforehand),
# calling `driver.forward()` will simply do nothing. Selenium
# does not throw an error or exception in this case.
# - It silently ignores the request if there is no "forward" action to perform.
