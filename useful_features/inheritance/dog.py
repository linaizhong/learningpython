# -*- coding: utf-8 -*-
from animal import Animal
"""Exemplo do uso de heranca em Python: Dog"""
class Dog(Animal):
	def __init__(self, name, age, breed):
		self.breed = breed
		Animal.__init__(self, name, age)

	def emit_sound(self):
		print 'Bark'	

