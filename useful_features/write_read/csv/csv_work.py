# -*- coding: utf-8 -*-
"""
Contem funcoes simples de escrita e leitura de arquivos
CSV
https://docs.python.org/2/library/csv.html
"""
import csv
import sys

# uso write_tuples((('tupla 1', 23.3), ('tupla 2', -34.42)), 'output.csv')
def write_tuples(data, file_name):
	# cria o arquivo
	out = csv.writer(file(file_name, 'w'))
	# salva os dados
	out.writerows(data)

def read_tuple_data(file_name):
	# efetua a leitura do arquivo
	data = csv.reader(file(file_name))
	# Escreve linha a linha: a saida vez em forma de list
	try:
		for register in data:
			print register
	except csv.Error as e:
		sys.exit('File %s, line %d: %s' % (file_name, data.line_num, e))
