
from pyjavaproperties import Properties
from TestResources import constants

prod = Properties()
def base_fixture():
    prodpath = open(constants.ENVIRONMENT_PROPERTIES)
    prod.load(prodpath)
    prod.list()

base_fixture()
