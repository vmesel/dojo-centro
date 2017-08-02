#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.dojopuzzles.com/problemas/exibe/ocr-bancario/

#     _  _       _   _  _   _   _
#  |  _| _| |_| |_  |_   | |_| |_|
#  | |_  _|   |  _| |_|  | |_|  _|



import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        source = [
          "   ",
          "  |",
          "  |"
        ]
        self.assertEqual(ocr(source), 1)

    def test_2(self):
        source = [
          " _ ",
          " _|",
          "|_ "
        ]
        self.assertEqual(ocr(source), 2)

if __name__ == "__main__":
    unittest.main()
