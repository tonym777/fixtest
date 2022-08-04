# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 22:59:04 2020

FixMiniServer Mock server for testing

@author: Tony
"""

from .fixminiserver import FIXMiniServer


class FIXMockServer(FIXMiniServer):

    def __init__(self, hosts=None, port=None):
        self._fix_msg_dict = {}

    def new_order(self, order_id, symbol, side, price, size):
        try:
            self._fix_msg_dict[order_id] = list((symbol, side, price, size))
            return {
                'id': order_id,
                'symbol': symbol,
                'side': side,
                'price': price,
                'size': size,
                'status': 'New'
            }
        except KeyError:
            print("error insert order={id}")
            return {
                'id': order_id,
                'status': 'Rejected'
            }

    def modify_order(self, order_id, new_size):
        try:
            symbol, side, price, size = self._fix_msg_dict[order_id]
            size = new_size
            self._fix_msg_dict[order_id] = list((symbol, side, price, size))
            return {
                'id': order_id,
                'symbol': symbol,
                'side': side,
                'price': price,
                'size': size,
                'status': 'Updated'
            }
        except KeyError:
            print("error update order={id}")
            return {
                'id': order_id,
                'status': 'Update Rejected'
            }

    def delete_order(self, order_id):
        try:
            symbol, side, price, size = self._fix_msg_dict[order_id]
            x = self._fix_msg_dict.pop(order_id)
            return {
                'id': order_id,
                'symbol': symbol,
                'side': side,
                'price': price,
                'size': size,
                'status': 'Deleted'
            }
        except KeyError:
            print("error remove order={order_id}")
            return {
                'id': order_id,
                'status': 'Remove Rejected'
            }
