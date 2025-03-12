
from page_object_model.pages.LoginPage import LoginPage
from page_object_model.pages.base import basepage


class LandingPage(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def landing(self):
        self.navigate()
        self.validatetitle()
        return LoginPage(self.driver)