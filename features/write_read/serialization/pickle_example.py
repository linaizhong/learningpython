# -*- coding: utf-8 -*-
""" Utiliza o modo pickle para serializar dados
"""
import pickle

# Classe que contem os dados a serem salvos
class Robot(object):
	def __init__(self, year):
		self.year = year


try:
	# tenta efetuar o loading de um objeto em disco
	robot = pickle.load(file('file.pkl'))
	print robot.year
except:
	# caso o arquivo nao exista cria um novo robo
	robot = Robot(1910)
	pickle.dump(robot, file('file.pkl', 'w'))
	print  'Gerado um robo novo'
	print robot.year



