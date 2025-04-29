import pytest
from selenium import webdriver
driver = webdriver.Chrome()
driver.save_screenshot("c:\\path")

@pytest.fixture
def test_alert():
    driver.get("https://www.example.com")
    alert = driver.switch_to.alert
    alert.accept()
    assert "Alert accepted" in driver.page_source

@pytest.fixture
def test_alert_dismiss():
    driver.get("https://www.example.com")
    alert = driver.switch_to.alert
    alert.dismiss()
    assert "Alert dismissed" in driver.page_source
    driver.quit()

