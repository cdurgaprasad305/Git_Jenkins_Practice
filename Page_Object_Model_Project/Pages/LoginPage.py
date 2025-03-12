import time

from Pages.EnterUserName import EnterUserName
from Pages.base import Base


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def dologin(self):
       self.click('loginlink')
       return EnterUserName(self.driver)