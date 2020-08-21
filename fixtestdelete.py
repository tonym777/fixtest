# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""

import TestFixMockServer

class TestNew(TestFixMockServer):
    
    def deleteOrder(self):
        result = self.fs.addOrder(1234, "EUR/USD", "BUY", 110, 100000)
        result = self.fs.removeOrder(1234)
        self.assertEqual('Deleted', result.get('status'))
 

