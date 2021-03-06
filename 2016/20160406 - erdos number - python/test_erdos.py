#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from erdos import *

class TestErdos(unittest.TestCase):
    def test_erdos(self):
        papers = []
        self.assertEqual(erdos_number(papers, 'Erdos'), 0)

    def test_with_erdos(self):
        papers = [['Erdos', 'John']]
        self.assertEqual(erdos_number(papers, 'John'), 1)

    def test_without_erdos_papers(self):
        papers = []
        self.assertEqual(erdos_number(papers, 'John'), None)

    def test_with_erdos_as_a_second_paper(self):
        papers = [['Erdos', 'Mary'], ['Erdos', 'John']]
        self.assertEqual(erdos_number(papers, 'John'), 1)

    def test_without_erdos(self):
        papers = [['John', 'Mary']]
        self.assertEqual(erdos_number(papers, 'John'), None)

    def test_one_erdos_coauthor(self):
        papers = [['John', 'Mary'], ['Mary', 'Erdos']]
        self.assertEqual(erdos_number(papers, 'John'), 2)

    def test_one_erdos_coauthor_three_papers(self):
        papers = [['John', 'Mary'], ['Mary', 'John'], ['Mary', 'Erdos']]
        self.assertEqual(erdos_number(papers, 'John'), 2)

    def test_one_erdos_coauthor_with_hurricane_truck(self):
        papers = [['John', 'Fofão'], ['John', 'Mary'], ['Mary', 'Erdos']]
        self.assertEqual(erdos_number(papers, 'Fofão'), 3)


    def test_(self):
        papers = [['John', 'Mary'], ['Mary', 'John']]
        self.assertEqual(erdos_number(papers, 'John'), None)






if __name__ == "__main__":
    unittest.main()
