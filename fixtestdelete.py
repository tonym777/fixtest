# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""

import unittest
from fixmockserver import fixmockserver


class TestDelete(unittest.TestCase):
    
    def setUp(self):
        self.fs = fixmockserver()

    def test_deleteOrder(self):
        result = self.fs.newOrdeMsg(1234, "EUR/USD", "BUY", 1.10, 100000)
        self.assertEqual('New', result.get('status'))
        result = self.fs.removeOrderMsg(1234)
        self.assertEqual('Deleted', result.get('status'))
 

