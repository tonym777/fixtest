# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:33:29 2020

@author: Tony
"""
import unittest
from unittest.mock import patch, Mock
import mongomock

from src.server.jsonmockserver import JSONMockServer


class TestModify(unittest.TestCase):

    @patch('pymongo.MongoClient', new_callable=mongomock.MongoClient)
    def setUp(self):
        self.fs = JSONMockServer()

    def test_modifyOrder(self):
        result = self.fs.new_order(1234, "IBM", "BUY", 110, 100000)
        self.assertEqual('New', result.get('status'))
        result = self.fs.modify_order(1234, 200000)
        self.assertEqual('Updated', result.get('status'))
