'''
Created on 09-Jun-2020

@author: jaspreet
'''
import pytest

@pytest.fixture(scope="module", autouse=True)
def base_fixture(request):
    print("Starting the test cases")
    yield 
    if request.session.testsfailed:
        print("")
        print("Test failed")
    else:
        print("")
        print("Test passed")
    print("Ending the test cases")