import unittest

from src.fixmsg.new_single_order import NewSingleOrder


class TestNewOrderSingle(unittest.TestCase):

    def setUp(self):
        pass

    def test_new_single_order(self):
        order = NewSingleOrder("EUR/USD", "BUY", 110, 100000)
        fix = order.build_fix_message()

        self.assertEqual('Updated', fix.get('status'))
