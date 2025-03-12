'''
Created on 09-Jun-2020

@author: jaspreet
'''
import unittest
from BaseTest.logging import common

class TestP3(unittest.TestCase,common):
    def test_1(self):
        print("i am in test_p3")
        print("")
        print("Presenting Running test case from : "+unittest.TestCase.id(self))
        assert True,"Passing Test p3"
        