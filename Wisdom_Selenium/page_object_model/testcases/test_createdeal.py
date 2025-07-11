import pytest
from conftest import obj_list
from pages.HomePage import Homepage
from pages.LandingPage import LandingPage
from testresources import constants
from testresources.readingexcel import getcelldata, isrunnable
import allure


# serial - pytest
# parallel - do something
@pytest.mark.usefixtures("base_fixture")
class TestDeal:
    @pytest.mark.parametrize(
        "argvals", getcelldata("CreateDeal", constants.XLS_FILEPATH)
    )
    def test_createdeal(self, argvals):
        # testcase - firstlevel check
        testrunmode = isrunnable("CreateDeal", constants.XLS_FILEPATH)
        # datasheet - secondlevel check
        datarunmode = argvals[constants.RUNMODE]
        if testrunmode:
            if datarunmode == constants.RUNMODE_Y:
                for i in range(0, len(obj_list)):
                    pass
                driver = obj_list[i].openbrowser(argvals[constants.BROWSERNAME])
                landing = LandingPage(driver)
                login = landing.landing()
                with allure.step("Loggin In..."):
                    username = login.dologin()
                    password = username.enterusername()
                    homepage = password.enterpassword()
                if isinstance(homepage, Homepage):
                    if argvals["ExpectedResult"] == "Success":
                        leadhomepage = homepage.homepage()
                        with allure.step("Creating Deal....."):
                            enterdealdetails = leadhomepage.adddeal()
                            dealcheck = enterdealdetails.leaddetails(
                                argvals["DealName"],
                                argvals["AccountName"],
                                argvals["Stage"],
                                argvals["ClosingDate"],
                            )
                    else:
                        obj_list[i].reportfailure("Lead cannot be created")
                    with allure.step("Validating deal creation...."):
                        obj_list[i].logging(argvals["DealName"])
                        dealcheck.checkdeal(argvals["DealName"])
                else:
                    obj_list[i].reportfailure("Login Failed!!!")
            else:
                pytest.skip("Testcase skipped due to run mode is no on data sheet")
        else:
            pytest.skip("Testcase skipped due to run mode is no on test sheet")
