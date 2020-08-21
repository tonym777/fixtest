# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 00:32:20 2020

@author: Tony
"""

import unittest

import fixmockserver

class TestFixMockServer(unittest.TestCase):

    @fixmockserver

    def setUp(self):
        self.fs = fixmockserver()
        pass
    

