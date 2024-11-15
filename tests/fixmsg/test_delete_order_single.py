import unittest

from src.fixmsg.new_single_order import NewSingleOrder
from src.fixmsg.cancel_single_order import CancelSingleOrder


class TestCancelOrderSingle(unittest.TestCase):

    def setUp(self):
        pass

    def test_cancel_single_order(self):
        order = NewSingleOrder("IBM", "BUY", 110, 100000)
        fix = order.build_fix_message()
        self.assertEqual(True, fix.__contains__('55=IBM'))
        self.assertEqual(True, fix.__contains__('44=110'))
        self.assertEqual(True, fix.__contains__('38=100000'))
        self.assertEqual(True, fix.__contains__('10='))
        order = CancelSingleOrder(order.get_field('11'))
        fix = order.build_fix_message()
        self.assertEqual(True, fix.__contains__('41='))
        self.assertEqual(True, fix.__contains__('10='))
