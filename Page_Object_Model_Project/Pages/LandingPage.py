from Pages.LoginPage import LoginPage
from Pages.base import Base


class LandingPage(Base):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def landing(self):

        self.navigate()
        # self.driver.maximize_window()
        return LoginPage(self.driver)
