# -*- coding: utf-8 -*-
"""Exemplo simples do uso de properties em Python"""
class Person(object):
	
	def __init__(self, name, age=1):
		self.__name = name
		self.__age = age

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age):
		self.__age = age if age > 0 and age < 149 else