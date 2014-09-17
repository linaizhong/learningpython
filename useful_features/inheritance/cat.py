# -*- coding: utf-8 -*-
from animal import Animal
"""Exemplo do uso de heranca em Python: Cat"""
class Cat(Animal):
	def __init__(self, name, age, whiskers):
		self.whiskers = whiskers
		Animal.__init__(self, name, age)

	def emit_sound(self):
		print 'Meow'

