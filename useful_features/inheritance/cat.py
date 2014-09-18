# -*- coding: utf-8 -*-
"""
Exemplo do uso de heranca em Python: Cat
"""


from animal import Animal

class Cat(Animal):
	def __init__(self, name, age, whiskers):
		self.whiskers = whiskers
		Animal.__init__(self, name, age)

	def emit_sound(self):
		"""
		printa o som de um gato
		"""
		print 'Meow'

