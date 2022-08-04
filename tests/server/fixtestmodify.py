# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""
import unittest

from src.server.fixmockserver import FIXMockServer


class TestModify(unittest.TestCase):
    
    def setUp(self):
        self.fs = FIXMockServer()
        
    def test_modifyOrder(self):
        result = self.fs.new_order(1234, "IBM", "BUY", 110, 100000)
        self.assertEqual('New', result.get('status'))
        result = self.fs.modify_order(1234, 200000)
        self.assertEqual('Updated', result.get('status'))
