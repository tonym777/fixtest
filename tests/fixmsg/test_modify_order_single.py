import unittest

from src.fixmsg.new_single_order import NewSingleOrder
from src.fixmsg.modify_single_order import ModifySingleOrder


class TestModifyOrderSingle(unittest.TestCase):

    def setUp(self):
        pass

    def test_modify_single_order(self):
        order = NewSingleOrder("IBM", "BUY", 110, 100000)
        fix = order.build_fix_message()
        self.assertEqual(True, fix.__contains__('55=IBM'))
        self.assertEqual(True, fix.__contains__('44=110'))
        self.assertEqual(True, fix.__contains__('38=100000'))
        order = ModifySingleOrder(order.get_field('11'), 90, 990000)
        fix = order.build_fix_message()
        self.assertEqual(True, fix.__contains__('44=90'))
        self.assertEqual(True, fix.__contains__('38=990000'))
