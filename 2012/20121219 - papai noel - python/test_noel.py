#coding: utf-8
import unittest
from noel import noel
from math import sqrt

class NoelTestCase(unittest.TestCase):

    def test_uma_crianca(self):
        criancas = [(1, 0)]
        self.assertEqual(1, noel(criancas))

    def test_uma_crianca_longe(self):
        criancas = [(2, 0)]
        self.assertEqual(2, noel(criancas))

    def test_uma_crianca_pra_cima(self):
        criancas = [(0, 1)]
        self.assertEqual(1, noel(criancas))

    def test_uma_crianca_na_diagonal(self):
        criancas = [(1, 1)]
        self.assertEqual(sqrt(2), noel(criancas))

    def test_uma_crianca_em_1_2(self):
        criancas = [(1, 2)]
        self.assertEqual(sqrt(5), noel(criancas))

    def test_duas_criancas_inline(self):
        criancas = [(0, 1), (0, 2)]
        self.assertEqual(2, noel(criancas))

    def test_duas_criancas_inline_0_1_0_3(self):
        criancas = [(0, 1), (0, 3)]
        self.assertEqual(3, noel(criancas))

    def test_duas_criancas_inline_vertical(self):
        criancas = [(1, 0), (3, 0)]
        self.assertEqual(3, noel(criancas))

    def test_duas_criancas_em_L(self):
        criancas = [(0, 1), (1, 1)]
        self.assertEqual(2, noel(criancas))

    def test_duas_criancas_em_L_invertido(self):
        criancas = [(1, 1), (0, 1)]
        self.assertEqual(2, noel(criancas))

    def test_duas_criancas_em_L_certo(self):
        criancas = [(1, 0), (0, 1)]
        self.assertEqual(2, noel(criancas))

    def test_tres_criancas_em_C(self):
        criancas = [(1, 0), (0, 1), (1, 1)]
        self.assertEqual(3, noel(criancas))

    def test_tres_criancas_em_U_estiloso(self):
        criancas = [(1, 0), (0, 1), (2, 1)]
        self.assertEqual(2 + sqrt(2), noel(criancas))

    def test_tres_criancas_em_U_estiloso_invertido(self):
        criancas = [(0, 1), (1, 0), (2, 1)]
        self.assertEqual(2 + sqrt(2), noel(criancas))

    def test_tres_criancas_em_T(self):
        criancas = [(0, 1), (-1, 1), (1, 1)]
        self.assertEqual(3, noel(criancas))

    def test_tres_criancas_em_T_invertido(self):
        criancas = [(-1, 0), (0, 1), (1, 0)]
        self.assertEqual(3, noel(criancas))

    def test_tres_criancas_em_trapezio(self):
        criancas = [(1, 0), (-1, 1), (1, 1)]
        self.assertEqual(2 + sqrt(2), noel(criancas))

    def test_quatro_criancas_em_cadeira_deitada(self):
        criancas = [(1, 0), (0,1), (-1, 1), (1, 1)]
        self.assertEqual(4, noel(criancas))

    def test_quatro_criancas_em_espingarda(self):
        criancas = [(2, 0), (0,1), (-2, 1), (1, 1)]
        self.assertEqual(4 + sqrt(2), noel(criancas))

    def test_zero_criancas_todas_malvadas(self):
        criancas = []
        self.assertEqual(0, noel(criancas))    

unittest.main()