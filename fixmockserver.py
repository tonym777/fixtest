# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 22:59:04 2020

FixMiniServer Mock server for testing

@author: Tony
"""

import fixminiserver

class fixmockserver:
    
    _fix_msg_dict = None

    def __init__(self, hosts=None, port=None):
        self._fix_msg_dict = {}
        
    def newOrdeMsg(self, id, symbol, side, price, size):
        try:
            self._fix_msg_dict[id] = list((symbol, side, price, size))
            return  {
                'id': id,
                'symbol': symbol,
                'side': side,
                'price': price,
                'size': size,
                'status': 'New'
                }
        
        except KeyError:
            print("error insert order={id}")
            return  {
                'id': id,
                'status': 'Rejected'
            }
                

    def modifyOrderMsg(self, id, newsize):
        try:
            symbol, side, price,size = self._fix_msg_dict[id]
            size = newsize
            self._fix_msg_dict[id] = list((symbol, side, price,size))
            return  {
                'id': id,
                'symbol': symbol,
                'side': side,
                'price': price,
                'size': size,
                'status': 'Updated'
                }
        
        except KeyError:
            print("error update order={id}")
            return  {
                'id': id,
                'status': 'Update Rejected'
            }

               
    def removeOrderMsg(self, id):
        try:
            symbol, side, price,size = self._fix_msg_dict[id]
            x = self._fix_msg_dict.pop(id)
            print(x)
            return  {
                'id': id,
                'symbol': symbol,
                'side': side,
                'price': price,
                'size': size,
                'status': 'Deleted'
                }
        
        except KeyError:
            print("error remove order={id}")      
            return  {
                'id': id,
                'status': 'Remove Rejected'
            }
        
