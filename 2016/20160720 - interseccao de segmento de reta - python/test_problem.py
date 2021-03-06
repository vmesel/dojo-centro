#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sure
import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        expected = [(0,0), (1,0)]
        point_a = (0, 0)
        point_b = (1, 0)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_2(self):
        expected = [(0,0), (0,1)]
        point_a = (0, 0)
        point_b = (0, 1)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_3(self):
        expected = [(0,0), (0,1), (0,2)]
        point_a = (0, 0)
        point_b = (0, 2)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_4(self):
        expected = [(0,0), (0,-1), (0,-2)]
        point_a = (0, 0)
        point_b = (0, -2)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_5(self):
        expected = [(0,0), (1, 0), (2, 0)]
        point_a = (0, 0)
        point_b = (2, 0)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_6(self):
        expected = [(-3,0), (-2, 0), (-1, 0)]
        point_a = (-3, 0)
        point_b = (-1, 0)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_7(self):
        expected = [(0, 0), (1, 1), (2, 2)]
        point_a = (0, 0)
        point_b = (2, 2)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_8(self):
        expected = [(0, 0), (1, 2)]
        point_a = (0, 0)
        point_b = (1, 2)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_9(self):
        expected = [(0, 0), (1, 2), (2, 4)]
        point_a = (0, 0)
        point_b = (2, 4)
        create_reta(point_a, point_b).should.be.equal(expected)

    def test_10(self):
        expected = [(0, 0), (-1, -2), (-2, -4)]
        point_a = (0, 0)
        point_b = (-2, -4)
        create_reta(point_a, point_b).should.be.equal(expected)


if __name__ == "__main__":
    unittest.main()

