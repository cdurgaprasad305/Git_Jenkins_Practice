'''
Created on 09-Jun-2020

@author: jaspreet
'''
import pytest
from BaseTest.logging import common
from DataProvider import info

@pytest.mark.usefixtures("base_fixture")
class TestP4(common):
    @pytest.mark.browser1
    @pytest.mark.parametrize("argVals,browsername",[(info.data(),info.browser1)])
#     @pytest.mark.dependency(depends=["test_b"])    
    def test_a(self,argVals,browsername):
        print("i am in test_p4")
        self.logs("Applying logging through inheriting the common class")
        print(argVals)
        print(browsername)
        self.logs("Browser name : "+browsername)
#         print("Presenting Running test case from : "+unittest.TestCase.id(self))
    
#     @pytest.mark.skip("skipping.....") 
    @pytest.mark.browser2
    @pytest.mark.parametrize("argVals,browsername",[(info.data(),info.browser2)])
    def test_b(self,argVals,browsername):
        print("i am in test_p4")
        self.logs("Applying logging through inheriting the common class")
        print(argVals)
        print(browsername)
#         assert False
    
#     @pytest.mark.browser2
#     @pytest.mark.parametrize("num1, num2, output", [(1,6,8),(9,2,11),(6,6,12)])
#     def test_c(self,num1, num2, output):
#         self.logs("Applying logging through inheriting the common class")
#         result = info.add(num1, num2)
#         assert output == result
        

        
        