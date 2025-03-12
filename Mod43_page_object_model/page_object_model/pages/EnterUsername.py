import time

from page_object_model.pages.EnterPassword import EnterPassword
from page_object_model.pages.base import basepage


#external files - properties , xlsx, csv....
#properties - locator
#excel - testdata


class EnterUsername(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterusername(self):
        self.type('usernametextbox_id', self.prod['defaultusername'])
        self.click('submitemailbtn_xpath')
        return EnterPassword(self.driver)

