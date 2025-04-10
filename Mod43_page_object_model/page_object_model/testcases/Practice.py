# import pytest
# @pytest.mark.parametrize("a, b, exp ", [(1, 2,3), (3, 4,7), (5, 6,11)])
# def test_add1(a, b, exp):
#    assert exp == (a+b)
#    pytest.mark.skip()
#    pytest.skip()


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///E:/Python2024/Example.html")

driver.find_element(By.ID, 'name').send_keys("Hello Durga")
driver.find_element(By.XPATH,'//*[@id="test-form"]/label[2]/following-sibling::input').send_keys("password")

cou = driver.find_elements(By.XPATH,"//button[@type='submit'] |//button[@id='click-me-button']")
print(len(cou))

for i in cou:
    print("Text on the Buttons:", i.text)
    print("Button Attribute:", i.get_attribute("id"))
    print("---------------")
# email_input = driver.find_element(By.XPATH,"//*[@id='email']")

driver.find_element(By.XPATH,"//textarea").send_keys("Information in text araa..")
driver.find_element(By.XPATH,"//button[@type='submit']").click()


# Use JavaScript to check the validity of the email input field
einput = driver.find_element(By.XPATH,"//*[@id='email']")

is_valid = driver.execute_script("return arguments[0].checkValidity()",einput)

validation_message = driver.execute_script("return arguments[0].validationMessage;", einput)

print("Is the email valid?", is_valid)
print("Validation message:", validation_message)

# OP:
# Is the email valid? False
# Validation message: Please include an '@' in the email address. 'password' is missing an '@'.


driver.find_element(By.XPATH, "//input[contains(@id, 'user_')]").send_keys("test")

driver.find_element(By.XPATH, "//button[starts-with(@id, 'btn-')]").click()

driver.find_element(By.XPATH, "//button[ends-with(@id, 'btn-')]").click() # not valid
# Below is workaround for above...
driver.find_element(By.XPATH, "//button[substring(@id, string-length(@id) - string-length('btn-') + 1) = 'btn-']").click()




input("Press Enter Key..")
driver.close()














