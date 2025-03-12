'''
Created on 09-Jun-2020
@author: jaspreet
'''
import logging
import softest
class common():
    def logs(self,msg):
        l = logging.getLogger()
        l.setLevel(logging.INFO)
        l.info(msg)
        
    def failure(self,a1,a2):
        softest.TestCase.soft_assert(softest.TestCase.assertEqual, a1, a2)
        softest.TestCase.assert_all()
    