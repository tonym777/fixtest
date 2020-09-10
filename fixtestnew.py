# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""


import unittest
from fixmockserver import fixmockserver

class TestNew(unittest.TestCase):
    
    def setUp(self):
        self.fs = fixmockserver()
        
    def test_addOrder(self):
        result = self.fs.newOrdeMsg(1234, "EUR/USD", "BUY", 1.1501, 100000)
        print(result)
        self.assertEqual('New', result.get('status'))
        

