# -*- coding: utf-8 -*-
"""Exemplo do uso MySQL em Python"""
# Execute primeiramente pip install mysql-python
import MySQLdb

# crie primeiramente o example_db
# Dentro do mysql CREATE DATABASE example_db;
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
