# -*- coding: utf-8 -*-
"""Exemplo do uso de decorator em Python"""
import time

def decorator_function(cls):
	class Decorator(cls):
		# Parametros
		def __init__(self, *args, **kargs):
			# escreve a data e hora atual
			print 'Time: ', time.asctime()
			# escreve o nome da classe
			print 'Class: ', repr(cls)
			# argumentos
			print 'Arguments: ', args
			print 'Kargs:', kargs
			#inicializa a classe param
			cls.__init__(self, *args, **kargs)
	return Decorator

@decorator_function
class Person(object):
	def __init__(self, name):
		self.name = name

# nome vai ser impresso como Kargs
p = Person(name='Bruno')
