import time

from _overlapped import NULL
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from TestResources import constants
global driver

class Base:
    def __init__(self):
        self.driver = NULL
        self.prod = conftest.prod

    def openbrowser(self, browsername):
        print("Opening browser")
        self.driver = constants.CHROME
        self.driver = webdriver.Chrome()

    def navigate(self):
        url = self.prod['URL']
        print(url)
        self.driver.get(url)
        self.driver.maximize_window()

    def click(self, obj):
        element = self.prod[obj]
        print("Login link xpath "+element)
        self.driver.find_element(By.XPATH,element).click()

    def type(self,obj,data):
        element = self.prod[obj]
        print("username text box xpath " +element)
        print ("User Id -- "+data)
        time.sleep(5)
        self.driver.find_element(By.XPATH, element).send_keys(data)

    # Common Utility

    def waitforpagetobeloaded(self):
        i=1
        while(i!=0):
            load_status = self.driver.execute_script("return document.readyState")
            if(load_status == 'complete'):
                break
            else:
                time.sleep(2)

    def iselementpresent(self):
        pass

    def iselementvisible(self,obj):
        wait = WebDriverWait(self.driver, 20)
        element = self.prod[obj]
        self.waitforpagetobeloaded()


        pass






