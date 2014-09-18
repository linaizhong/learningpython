import sys
# volta um diretorio acima
sys.path.append('..')
# importa todas as funcoes do modulo algorithms.fibonacci
from algorithms.fibonacci import *

# Importa o teste unitario
import unittest

# Herda da classe de teste
class TestFibonacci(unittest.TestCase):

	"""Primeiro metodo chamado, antes de todos os outros
	"""
	def setUp(self):
		self.sequence = range(11)

	def testCase0(self):
		self.assertEqual(iterative_fibonacci(10), 55)

	def testCase1(self):
		self.assertEqual(iterative_fibonacci(1), 1)

	def testSequence(self):
		# resposta esperada para a sequence
		expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
		for x, y in zip(expected_result, [iterative_fibonacci(x) for x	 in self.sequence]):
			print x, y
			self.assert_(x is y)

if __name__ == "__main__":
		unittest.main()