import sys
# volta um diretorio acima
sys.path.append('..')
# importa todas as funcoes do modulo algorithms.fibonacci
from algorithms.fibonacci import *


# Exemplo de modulo de teste
def fibonacci_test(number):
	"""Doctest fibonacci
	Aqui colocamos os testes e na linha seguinte o resultado esperado
	>>> fibonacci_test(1) #teste OK
	1
	>>> fibonacci_test(10) #teste OK
	55
	>>> [fibonacci_test(i) for i in range(11)] #teste OK
	[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	"""
	return iterative_fibonacci(number)

def _doctest():
	"""Chamada do modulo de doctest
	"""
	import doctest
	doctest.testmod()

if __name__== "__main__":
	_doctest()


