# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""

import TestFixMockServer

class TestModify(TestFixMockServer):
    
  
    def modifyOrder(self):
        self.fs.addOrder(1234, "EUR/USD", "BUY", 110, 100000)
        result = self.fs.modifyOrder(1234, 200000)
        self.assertEqual('Updated', result.get('status'))
        

