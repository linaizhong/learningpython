# -*- coding: utf-8 -*-
"""
Exemplo do uso de heranca em Python: Dog
"""


from animal import Animal

class Dog(Animal):
	def __init__(self, name, age, breed):
		self.breed = breed
		Animal.__init__(self, name, age)

	def emit_sound(self):
		"""
		print o som de um cachorro
		"""
		print 'Bark'	

