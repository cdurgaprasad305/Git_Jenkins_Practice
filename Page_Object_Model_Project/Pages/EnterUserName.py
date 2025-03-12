
import time
from selenium.webdriver.common.by import By
from Pages.base import Base


class EnterUserName(Base):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def enterUserName(self):
        time.sleep(7)
        self.type('usernametextbox', 'xxyy@dmin.com')

