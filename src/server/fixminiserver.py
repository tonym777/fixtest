# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:07:35 2020

FixMiniServer is a smallest fix server (interface)
@author: Tony
"""


class FIXMiniServer:

    def new_order(self, order_id, symbol, side, price, size):
        pass

    def modify_order(self, order_id, size):
        pass

    def delete_order(self, order_id):
        pass
