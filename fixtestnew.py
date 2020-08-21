# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""

import TestFixMockServer

class TestNew(TestFixMockServer):
    
    def addOrder(self):
        self.fs.addOrder(1234, "EUR/USD", "BUY", 110, 100000)
 
#    def removeOrder(self):
#        self.fs.removeOrder(1234)
        
#    def updateOrder(self, size):
#        self.fs.updateOrder(1234, size)
        

