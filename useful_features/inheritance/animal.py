# -*- coding: utf-8 -*-
"""Exemplo do uso de heranca em Python"""
from abc import abstractmethod 
class Animal(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@abstractmethod
	def emit_sound(self):
		# sem implementacao
		pass
