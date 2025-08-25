"""
Created on Thu Aug 20 22:59:04 2020

FIXMockServer Mock server by using fixmsg packege implementation  for testing

@author: Tony
"""

from .fixminiserver import FIXMiniServer
from src.utils.mongodb_api import MongoDBAPI
from ..fixmsg.new_single_order import NewSingleOrder


class FIXMockServer(FIXMiniServer):

    def __init__(self, hosts=None, port=None):
        self.db = MongoDBAPI()
        self._fix_msg_dict = {}

    def new_order(self, order_id, symbol, side, price, size):
        try:
            fixmsg = NewSingleOrder(symbol, side, price, size)
            self._fix_msg_dict[order_id] = fixmsg
            self.db.insert_one("fix_orders", fixmsg)
            return fixmsg
        except KeyError:
            print("error insert order={id}")
            return {
                'order_id': order_id,
                'status': 'Rejected'
            }

    def modify_order(self, order_id, new_size):
        try:
            fixmsg = self._fix_msg_dict[order_id]
            fixmsg.set_body({'38': new_size})

            self._fix_msg_dict[order_id] = fixmsg
            self.db.insert_one('fix_orders', fixmsg)
            return fixmsg
        except KeyError:
            print("error update order={}", order_id)
            return {
                'order_id': order_id,
                'status': 'Update Rejected'
            }

    def delete_order(self, order_id):
        try:
            fixmsg = self._fix_msg_dict[order_id]
            self.db.insert_one('fix_orders', fixmsg)
            del self._fix_msg_dict[order_id]
            return fixmsg
        except KeyError:
            print("error remove order={}", order_id)
            return {
                'order_id': order_id,
                'status': 'Remove Rejected'
            }
