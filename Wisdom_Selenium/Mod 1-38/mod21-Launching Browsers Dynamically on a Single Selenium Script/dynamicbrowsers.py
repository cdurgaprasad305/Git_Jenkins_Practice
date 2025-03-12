from selenium import webdriver

# browser_name = ""
webdriver.driver = None

browser_name = (input("Enter browser name: ")).lower()

if browser_name == "chrome":
    driver = webdriver.Chrome()

elif browser_name == "firefox":
    driver = webdriver.Firefox()

elif browser_name == "edge":
    driver = webdriver.Edge()

elif browser_name == "ie":
    driver = webdriver.Ie()

else:
    print("No browser specified.....")

try:
    if driver != None:
        driver.get("https://flipkart.com")
        driver.quit()

except NameError as n:
    print("---Error Description---", n)
