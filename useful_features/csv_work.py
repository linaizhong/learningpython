# -*- coding: utf-8 -*-
"""
Contem funcoes simples de escrita e leitura de arquivos
CSV
"""
import csv

# uso write_tuples((('tupla 1', 23.3), ('tupla 2', -34.42)), 'output.csv')
def write_tuples(data, file_name):
	# cria o arquivo
	out = csv.writer(file(file_name, 'w'))
	# salva os dados
	out.writerows(data)

def read_tuple_data(file_name):
	# efetua a leitura do arquivo
	data = csv.reader(file(file_name))
	# Escreve linha a linha em forma de de List
	for register in data:
		print register
