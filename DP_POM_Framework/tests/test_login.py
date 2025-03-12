import time

import pytest
from pages.login_page import LoginPage
from utilities.excel_util import ExcelUtility
from utilities.config import BASE_URL, EXCEL_FILE_PATH
import allure


@pytest.mark.usefixtures("setup")
class TestLogin:

    def setup_method(self):
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.excel_util = ExcelUtility(EXCEL_FILE_PATH)

    @allure.feature("Login Feature")
    @allure.story("Valid Login")
    @allure.title("Test Valid Login")
    @allure.description("This is a test description")
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.dynamic.title("Test Valid Login")
    # @allure.dynamic.description("This is a test description")
    @allure.id("TC-001")
    @allure.tag("Login")
    # @allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=allure.attachment_type.PNG)

    def test_valid_login(self):
        # Read data from Excel
        username = self.excel_util.get_cell_data("LoginData", 2, 1)
        password = self.excel_util.get_cell_data("LoginData", 2, 2)

        # Perform login
        print("----Username :", username)
        print("----Password :", password)
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Login Screenshot", attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.login_page.click_login()
        assert "Web Testing Page" in self.driver.title  # Replace with actual validation step

