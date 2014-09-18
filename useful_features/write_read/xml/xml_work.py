# -*- coding: utf-8 -*-
"""
Contem funcoes simples de escrita e leitura de arquivos
XML
https://docs.python.org/2/library/xml.html
"""

import xml.etree.ElementTree as ET


def read_data_etree():
	# Efetua o parsing usando o metodo etree (supondo que arquivo exista)
	tree = ET.parse('countries.xml')
	# busca a raiz (data)
	root = tree.getroot()
	# escreve a tag 
	print root.tag #data <data>
	# print root.attrib # {} vazio, sem atributos
	for country in root:
		# escreve pais a pais
		print country.attrib.get('name')

	# escreve a vizinhanca
	for neighbor in root.iter('neighbor'):
		print neighbor.attrib.get('name')

def write_data_etree():
	root = ET.Element('data')
	country = ET.SubElement(root, 'country')
	# atributo nome com valor brazil
	country.set('name', 'Brazil')
	rank = ET.SubElement(country, 'rank')
	# valor de rank <rank> 12 </rank>
	rank.text = str(12)
	# escreve o resultado do XML
	ET.dump(root)
