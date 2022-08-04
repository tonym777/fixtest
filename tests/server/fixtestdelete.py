# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""

import unittest

from src.server.fixmockserver import FIXMockServer


class TestDelete(unittest.TestCase):
    
    def setUp(self):
        self.fs = FIXMockServer()

    def test_deleteOrder(self):
        result = self.fs.new_order(1234, "EUR/USD", "BUY", 1.10, 100000)
        self.assertEqual('New', result.get('status'))
        result = self.fs.delete_order(1234)
        self.assertEqual('Deleted', result.get('status'))
