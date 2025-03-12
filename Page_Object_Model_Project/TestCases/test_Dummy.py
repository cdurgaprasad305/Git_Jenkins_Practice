
from selenium import webdriver
from Pages.LandingPage import LandingPage
# from Pages.LandingPage import LandingPage


class TestDummy:

    def test_dummy(self):

        driver = webdriver.Chrome()
        lp = LandingPage(driver)
        login = lp.landing()
        username = login.dologin()
        username.enterUserName()





        input("Enter key to exit")