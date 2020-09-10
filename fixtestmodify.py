# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""
import unittest
from fixmockserver import fixmockserver


class TestModify(unittest.TestCase):
    
    def setUp(self):
        self.fs = fixmockserver()
        
    def test_modifyOrder(self):
        result = self.fs.newOrdeMsg(1234, "EUR/USD", "BUY", 110, 100000)
        self.assertEqual('New', result.get('status'))
        result = self.fs.modifyOrderMsg(1234, 200000)
        self.assertEqual('Updated', result.get('status'))
        

