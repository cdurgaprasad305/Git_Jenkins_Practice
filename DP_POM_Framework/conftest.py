
import pytest
from jinja2.nodes import DerivedContextReference
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # New import for Service class
from selenium.webdriver.chrome.options import Options  # For ChromeOptions


from utilities.config import CHROME_DRIVER_PATH  # Ensure this path is set correctly

# driver = None
@pytest.fixture(scope="class")
def setup(request):
    # Configure ChromeOptions (you can add more options if needed)
    '''chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
'''
    # Set up the ChromeDriver service
    print("----Chrome Driver Path :",CHROME_DRIVER_PATH)
    service = Service(CHROME_DRIVER_PATH)

    # Pass the service and options to WebDriver
    driver = webdriver.Chrome(service=service)

    # Set the driver as an attribute of the test class

    request.cls.driver = driver
    request.cls.driver.maximize_window()

    yield
    driver.quit()



