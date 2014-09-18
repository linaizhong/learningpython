# -*- coding: utf-8 -*-
""" Leitura e escrita de JSON
"""
import json
from pprint import pprint

# Cria um dicionario JSON
data = {'store': {'countries': [{'name': 'Brazil'}, {'name': 'Germany'}]}}
print json.dumps(data)

# Navegacao dentro do JSON
for country in data["store"]['countries']:
	print country['name']

