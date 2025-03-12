import time

from page_object_model.pages.HomePage import Homepage
from page_object_model.pages.base import basepage


#external files - properties , xlsx, csv....
#properties - locator
#excel - testdata



class EnterPassword(basepage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterpassword(self):
        self.type('passwordtextbox_id', self.prod['defaultpassword'])
        self.click('signinbtn_xpath')
        #homepage - zoho crm
        #wrong - stay on same page
        # obj - homepage
        return Homepage(self.driver)
