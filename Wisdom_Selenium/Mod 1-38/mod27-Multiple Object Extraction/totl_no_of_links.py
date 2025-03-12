import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)


linklist = driver.find_elements(By.TAG_NAME, "a")  # return value: List []
print("-----Type of the Element-----", type(linklist))
print("----Total No.of Links -----", len(linklist))
count = 0
total_links = len(linklist)
try:
    for i in range(0, total_links - 1):
        link_text = linklist[i].get_attribute("text")
        print(link_text + " - " + str(linklist[i].is_displayed()))
        print(link_text + " - " + str(linklist[i].is_enabled()))

        # if link_text.startswith("Advertise"):  # Check if text starts with "new_"
        if link_text == "Trending Videos":
            print(f"------Matched Link: {link_text}")
            count += 1
except Exception as e:
    print("--Exception Descriptin ---", e)

print(f"------Total number of links starting with 'Trending Videos': {count}")

time.sleep(5)
driver.quit()
