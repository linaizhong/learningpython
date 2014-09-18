# -*- coding: utf-8 -*-
"""Exemplo do uso MySQL em Python"""
# Execute primeiramente pip install mysql-python
import MySQLdb

"""crie primeiramente o example_db
no mysql faca: CREATE DATABASE example_db;"""

# Cria uma conexao: banco de dados, usuario e senha
connection = MySQLdb.connect(db='example_db', user='root', passwd='')

# cria um cursor
cursor = connection.cursor()
# Comando a ser executado
cursor.execute('SHOW DATABASES')
# Obtem resultados
databases_info = cursor.fetchall()

# imprime todas as bases de dados presentes
for db in databases_info:
	print db

# fecha a conexao
connection.close()
