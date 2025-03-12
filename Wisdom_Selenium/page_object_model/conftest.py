import pytest
from pyjavaproperties import Properties
from pages.base import basepage
from testresources import constants
import allure

prod = Properties()
obj_list = []

@pytest.yield_fixture(scope="function", autouse=True)
def base_fixture():
    with allure.step("Initializing block...."):
        try:
            prod_path = open(constants.ENVIRONMENT_PROPERTIES)
            prod.load(prod_path)
            base = basepage()
            obj_list.append(base)
        except Exception as e:
            print("---Error Description--- ", e)
            pass
    yield locals()
    with allure.step("Finishing up...."):
        base.quit()
