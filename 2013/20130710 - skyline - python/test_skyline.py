import unittest
from skyline import skyline

class TestSkyline(unittest.TestCase):
	def test_caso_vazio(self):
		entrada = []
		saida = []
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_um_predio(self):
		entrada = [(1,10,2)]
		saida = [(1, 10), (2, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_outro_predio(self):
		entrada = [(1,5,3)]
		saida = [(1, 5), (3, 0)]
		self.assertEqual(saida, skyline(entrada))



unittest.main()


