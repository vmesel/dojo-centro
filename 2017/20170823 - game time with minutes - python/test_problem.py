#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_minuto(self):
        value = '1 1 1 2'
        expected = 'O JOGO DUROU 0 HORA E 1 MINUTO'
        self.assertEqual(expected, time(value))

    def test_2_minuto(self):
        value = '1 1 1 3'
        expected = 'O JOGO DUROU 0 HORA E 2 MINUTOS'
        self.assertEqual(expected, time(value))

    def test_3_minuto(self):
        value = '1 1 1 4'
        expected = 'O JOGO DUROU 0 HORA E 3 MINUTOS'
        self.assertEqual(expected, time(value))

    def test_4_minuto(self):
        value = '1 1 1 5'
        expected = 'O JOGO DUROU 0 HORA E 4 MINUTOS'
        self.assertEqual(expected, time(value))

    def test_10_minuto(self):
        value = '1 1 1 11'
        expected = 'O JOGO DUROU 0 HORA E 10 MINUTOS'
        self.assertEqual(expected, time(value))

    def test_1_hora(self):
        value = '1 1 2 1'
        expected = 'O JOGO DUROU 1 HORA E 0 MINUTO'
        self.assertEqual(expected, time(value))

    def test_2_hora(self):
        value = '1 1 3 1'
        expected = 'O JOGO DUROU 2 HORAS E 0 MINUTO'
        self.assertEqual(expected, time(value))

    def test_50_minutos(self):
        value = '1 50 2 40'
        expected = 'O JOGO DUROU 0 HORA E 50 MINUTOS'
        self.assertEqual(expected, time(value))

    def test_10_minutos_2(self):
        value = '2 55 3 5'
        expected = 'O JOGO DUROU 0 HORA E 10 MINUTOS'
        self.assertEqual(expected, time(value))

    def test_24_horas(self):
        value = '1 1 1 1'
        expected = 'O JOGO DUROU 24 HORAS E 0 MINUTO'
        self.assertEqual(expected, time(value))

    def test_viradao_cultural_10_minutos(self):
        value = '23 59 0 9'
        expected = 'O JOGO DUROU 0 HORA E 10 MINUTOS'
        self.assertEqual(expected, time(value))
    def test_10_minutos_3(self):
        value = '0 9 23 59'
        expected = 'O JOGO DUROU 23 HORAS E 50 MINUTOS'
        self.assertEqual(expected, time(value))


if __name__ == "__main__":
    unittest.main()

