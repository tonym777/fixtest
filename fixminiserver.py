# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:07:35 2020

FixMiniServer is a smallest fix server (interface)
@author: Tony
"""


class fixminiserver :

     
    def __init__(self, hosts, port):
        pass
        
    def newOrdeMsg(self, id, symbol, side, price, size):
        pass
    
    def modifyOrderMsg(self, id, size):
        pass
        
    def removeOrderMsg(self, id):
        pass
        