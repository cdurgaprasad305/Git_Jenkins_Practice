import sys
import time
import json
import traceback
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, JavascriptException
from selenium.webdriver import ActionChains, Keys, DesiredCapabilities
"""
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
"""
# driver.get("https://www.google.com")
# driver.get("https://www.amazon.in")
# driver.get("file:///E:/Python%202024_6/First.html")
# driver.get("https://practicetestautomation.com/practice-test-login")
# driver.get("https://testbook.com/tspsc-group-2/test-series")

# 1 save_screenshot, send_keys and CSS Selector
"""
# student_input = driver.find_element(By.XPATH, "//*[@id='username']")
student_input = driver.find_element(By.CSS_SELECTOR, "input#username")
student_input.send_keys("student")
student_input.screenshot("ex2.png")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[@id='submit']").click()
driver.save_screenshot("ex.png")
"""

# 2 Page title, selected link in a group of web elements, reading data using JSON file
"""
with open("Data.json", "r") as file:
    js_data = json.load(file)

mobile_link ="//a[text()='Mobiles']"
def page_title():
    # driver.find_element(By.XPATH, "//a[text()='Mobiles']").click
    # driver.find_element(By.LINK_TEXT, "Mobiles").click
    # driver.find_element(By.PARTIAL_LINK_TEXT, "Mobi").click()
    driver.find_element(By.XPATH, mobile_link).click()
    print("Sell Page Title :", driver.title)

page_title()

# Click on a selected link, in a group of web elements banners
def link_in_set(l_name):
    link_list = driver.find_element(By.ID, "nav-xshop")
    link_count = link_list.find_elements(By.TAG_NAME, "a")


    # for i in range(len(link_count)):
    for lc in link_count:
        if lc.text == l_name:
            lc.click()
            print("Page Title :", driver.title)
            break

link_in_set(js_data["link_name"]) # Calling the Function
"""

# 3 Link_text, Partial_link_text, mouse_move (Action Class)
"""
driver.find_element(By.LINK_TEXT,js_data["link_name"]).click()
print("-------Page Title :", driver.title)

driver.find_element(By.PARTIAL_LINK_TEXT, "Mobi").click()
print("-------Page Title-------- :", driver.title)

# OP:
# Page Title: Mobile Phones: Buy New Mobiles Online at Best Prices in India |
# Buy Cell Phones Online - Amazon.in

mov_element = driver.find_element(By.XPATH, "//*[@id='nav-link-accountList']")
ac=ActionChains(driver)
ac.move_to_element(mov_element).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='nav-al-your-account']/ul/li[1]/a/span").click()
# driver.find_element(By.XPATH, "//*[contains(text(),'Your Account')]").click()
print("Your Account Page Title :", driver.title)
"""

# 4 clear text, retrieve the text, double-click, right-click,
# static text information, Entire page text
"""
# Entering value in text field
driver.find_element(By.ID, "name").send_keys("Student")
driver.find_element(By.ID, "message").send_keys("Hello Selenium")

print("----Name :", driver.find_element(By.ID, "name").get_attribute("value"))
driver.find_element(By.ID, "name").clear()  # Clear text field

# static text information
test_box = driver.find_element(By.XPATH, "//label[text() ='Message:']").text
print("----Text_box_name :", test_box)

# OP:
# ----Name : Student
# ----Text_box_name : Message:

# Get all visible text from the <body> tag
entire_text = driver.find_element(By.TAG_NAME, "body").text
print("----Entire Page Text: ", entire_text)

rc = driver.find_element(By.ID, "right-click-area")
ac = ActionChains(driver)
ac.double_click(rc).perform()  # Double Click
ac.context_click(rc).perform()  # Right Click
"""

# 5 Selecting drop-down values
"""
select_element = driver.find_element(By.ID, "country")
select_object = Select(select_element)

default_val = select_object.first_selected_option
select_object.select_by_value("india")
tot_opt = len(select_object.options)
print("-------Default Value :", default_val.text)
print("-------Total Options :", tot_opt)
# OP:
# -------Default Value : Select your country
# -------Total Options : 5

# --- Selecting drop-down without Select class
select_element = driver.find_element(By.ID, "country")
# Find the dropdown with xpath, and perform click operation 
select_element.click()
driver.find_element(By.XPATH, "//*[@id='country']/option[3]").click()
driver.find_element(By.XPATH, "//*[@id='test-form']/label[5]").click()
# Select the list value using xpath, and click on static text, to close the 
# dropdown list box 
"""

# 6 Check box, Radio button, Total no.of check box in a page
"""
#---Check box---
if driver.find_element(By.ID,'terms').is_selected():
    pass
else:
    print("----Else block is executed----")
    driver.find_element(By.ID,'terms').click()
# or

if not driver.find_element(By.ID,'terms').is_selected():
    driver.find_element(By.ID,'terms').click()

#---Radio button---
# //input[@type='radio' and @value = 'male' and @id='male']
# Locate the nth radio button in a group: (//input[@type='radio'])[n]
# //*[@type='radio' and @value = 'male' and @id='male']

# ----Explanation----
# //* : Matches any element in the DOM.
# [@type='radio'] : Ensures the element is an `input` element of type `radio`.
# [@value='male'] : Adds a filter to match only the radio button with the value `male`.
# [@id='male'] : Ensures that the specific radio button has an ID of `male`.

driver.find_element(By.XPATH , "//input[@type='radio' and @value = 'male' and @id='male']").click()
# if already RADIO button is selected, it will keep as it is.. 
# //*[@id="terms"] 

tot_check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @id='terms']")
print("----Total no.of check box with Id = terms :", len(tot_check_box))
# OP: ----Total no.of check box with Id = terms : 2

tot_check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @id!='terms']")
print("----Total no.of check box with Id not equal to terms :", len(tot_check_box))
# ----Total no.of check box with Id not equal to terms : 2
"""

# 7 Explicit Wait, Fluent Wait, Implicit Wait, Static Wait
"""
time.sleep(5) # Static Wait
driver.implicitly_wait(10) # Implicit Wait

wait = WebDriverWait(driver ,10)
web_element = wait.until(EC.visibility_of_element_located((By.XPATH , "//input[@type='text' and @id='name']")))
# or

web_element = WebDriverWait(driver ,4).until(EC.visibility_of_element_located((By.XPATH , "//input[@type='text' and @id='name']")))
web_element.send_keys("Info")

# Fluent Wait
# 1. Allowing polling intervals (i.e., how often to check the condition).
# 2. Ignoring certain types of exceptions while waiting (e.g., `NoSuchElementException`).

wait1 = WebDriverWait(driver, timeout=20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])

web_element = wait1.until(EC.visibility_of_element_located((By.XPATH , "//input[@type='text' and @id='name']")))
web_element.send_keys("Info")
"""

# 8 Alerts, alert exception
"""
driver.find_element(By.XPATH, "//button[@onclick='showAlert()']").click()
al_text = driver.switch_to.alert.text
print("----Alert Text :", al_text)  # OP: ----Alert Text : This is an alert box!

driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//input[@type='text' and @id='name']").send_keys("Info")

# if we have active alert box, we can't perform operations on web page
# UnexpectedAlertPresentException
# NoAlertPresentException
"""

# 9 iFrames, Switch to frame, No.of frames, element inside the frame
"""

# //*[@id="message"] -- main page xpath for message box
# //*[@id="message"] -- frame page xpath for message box
# We can have same xpath for main page and frame page for a web_element
# Even if we have unique element_id in frame, it will not interact with the element,unless we switch_to the frame 

try:
    driver.switch_to.frame("FrameA") # Provide ID or Frame NAME
    driver.find_element(By.XPATH ,"//*[@id='message']").send_keys("Frame page text")
except NoSuchElementException:
    pass

driver.switch_to.default_content()
driver.find_element(By.XPATH ,"//*[@id='message']").send_keys("Main page text")

tot_frames = driver.find_elements(By.TAG_NAME, "iframe")
print("----Total no.of frames :", len(tot_frames))
# OP: ----Total no.of frames : 2
"""

# 10 Browser Tab, window handle, close specific window, browser tab with an action chain
"""
# We have to open the new browser in the below formate only...
driver.execute_script("window.open('https://www.google.com', '_blank');")
driver.execute_script("window.open('https://bbc.com');")
driver.execute_script("window.open('https://practicetestautomation.com/practice-test-login');")
driver.execute_script("window.open('https://www.amazon.in');")

# driver.execute_script("window.scrollBy(0, 1000);") # Similar to pageDown key

parent_window= driver.current_window_handle
print("----Parent Window :", parent_window)

all_window= driver.window_handles
print("----All Window :", all_window)

# OP:
# ----Parent Window : C60E12308DF5940AB310E4F8F41783D5
# ----All Window : ['C60E12308DF5940AB310E4F8F41783D5', 'F4C97BA1C5E77832778DF849AF6EB662',
#                   'DEC21EB40158198B581920B4C6B19ED8', '29A3A2FD8E103A736F5A3F00F23FBA5C',
#                   'C62EF1696AA4EE6652E0418D471AC37E']

parent_window= driver.current_window_handle
driver.execute_script("window.open('https://practicetestautomation.com/practice-test-login');")
window_handle = driver.window_handles

# todo Challenge..
driver.switch_to.window(window_handle[-1]) # Focuses on the recently opened tab
driver.find_element(By.XPATH, "//*[@id='username']").send_keys("student")
print("----New Window Handle :", driver.current_window_handle)
print("----New Window Title :", driver.title)
driver.close() # closing newly open window

driver.switch_to.window(parent_window)
print("----Parent window title : ",driver.title)

# OP:
# ----New Window Handle : 659A28B7F8A9E0B634AD18EBCC5C82B5
# ----New Window Title : Test Login | Practice Test Automation
# ----Parent window title :  Web Testing Page

# Open new browser tab using ActionChains Class 
ac=ActionChains(driver)
ac.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
"""

# 11 Dynamic web element, scroll to a specific element, console logs
"""
scroll_element = driver.find_element(By.ID,'click-me-button')
driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
scroll_element.click()
"""

# 14 mobile devices, JavaScript, CAPTCHA, 2FA (two-factor-authentication)
"""
options = Options()
options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone X"})
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com")

# locate an element and change its text content using JavaScript
driver.execute_script("document.getElementById('some-id').innerText ='New Text';")

# Gives the value of the element
value = driver.execute_script("return document.getElementById('input-id').value;")
print(value)

#------- CAPTCHA ---------
# Take a screenshot of the CAPTCHA image
# Solve CAPTCHA using 2Captcha API
# Submit CAPTCHA for solving using 'requests.post'
# poll for CAPTCHA solution
# Enter CAPTCHA solution into the input field

# use reCAPTCHA plugins
# http://2captcha.com/

# Manual Solving - Pause automation to solve the CAPTCHA

"""

# 15 Click element and set value in Input field using JavaScript
# MouseOver and Keyboard Input using JavaScript
"""
input_name= driver.find_element(By.XPATH ,"//input[@type='text' and @id='name']")
driver.execute_script("arguments[0].value = 'Ravi Kumar';", input_name)

click_element = driver.find_element(By.ID,'click-me-button')
driver.execute_script("arguments[0].click();", click_element)
"""

# 16 retrieve all cookies
"""
    Cookies are small pieces of data that websites store on a 
    user’s browser to track, remember, and manage specific information 
    about their interaction with the website. They are essential for
    modern web functionality, providing a way to maintain stateful 
    information in an otherwise stateless protocol (HTTP). 

all_cookies = driver.get_cookies()
print("----All Cookies :", all_cookies) 

for cookie in all_cookies:
    print("----Cookie Name :", cookie["name"])

    
    OP:
    ----All Cookies : [{'domain': 'www.amazon.in', 'expiry': 1771672557, 'httpOnly': False, 'name': 'csm-hit',
    'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tb:s-H99JS3DA0HE9R86AY11J|1741432556540&t
    :1741432557258&adb:adblk_no'}, {'domain': '.amazon.in', 'expiry': 1772968556, 'httpOnly': False, 'name': 
    'ubid-acbin', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '262-1893304-4941547'},
    {'domain': '.amazon.in', 'expiry': 1772968555, 'httpOnly': False, 'name': 'i18n-prefs', 'path': '/', 'sameSite':
    'Lax', 'secure': False, 'value': 'INR'}, {'domain': '.amazon.in', 'expiry': 1772968555, 'httpOnly': False, 'name': 
    'session-id-time', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '2082787201l'},
    {'domain': '.amazon.in', 'expiry': 1772968555, 'httpOnly': False, 'name': 'session-id',
    'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '260-6639929-8961061'}]

----Cookie Name : csm-hit
----Cookie Name : ubid-acbin
----Cookie Name : i18n-prefs
----Cookie Name : session-id-time
----Cookie Name : session-id  

"""

# 17 Network traffic, Performance metric TODO..
"""

"""

# 18 Navigate back and forward
"""
driver.back()
driver.forward()
"""


# 20 Integrate Selenium with PyTest, Generate a Test report for Selenium tests
# Integrate Selenium with Jenkins and GitHub
# Integrate with Allure reports

# Recursive function to generate XPaths for all elements
"""
def get_all_xpaths(element, current_xpath=""):
    try:
        # Get the tag name of the element
        tag_name = element.tag_name

        # Build the current XPath
        current_xpath = current_xpath + f"/{tag_name}"

        # Print the current XPath
        print(current_xpath)

        # Find all child elements
        children = element.find_elements(By.XPATH, "*")

        # Run the function recursively for every child element
        for child in children:
            get_all_xpaths(child, current_xpath)

    except NoSuchElementException:
        pass  # If an element is not found during traversal, ignore and continue


# Start from the root element (HTML element)
html_element = driver.find_element(By.XPATH, "/html")
get_all_xpaths(html_element)
"""

# input("Press Enter to Close")
# driver.quit()




















