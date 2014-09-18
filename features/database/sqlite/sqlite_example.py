# -*- coding: utf-8 -*-
"""Exemplo do uso SQLITE"""

import sqlite3

# insercao de dados
insert_sentence = 'INSERT INTO person VALUES (null, ?, ?)'
# query
query_sentence = 'SELECT * FROM person'

def connection_sqlite():
	# cria uma base de dados chamada database.db
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	# Cria uma tabela simples com nome e idade
	person_table = 'CREATE TABLE person '\
		'(id INTEGER PRIMARY KEY, '\
		'name VARCHAR(100), '\
		'years_old INTEGER)'

	cursor.execute(person_table)
	return connection, cursor


def insert_data(data, cursor, connection):
	cursor.execute(insert_sentence, data)
	# insere o registro
	connection.commit()


def query(cursor):
	cursor.execute(query_sentence)
	answer = cursor.fetchall()
	for i in answer:
		print '%d: %s %d' % i


connection, cursor = connection_sqlite()
insert_data(('Bruno', 25), cursor, connection)
insert_data(('Bruno Gabriel dos Santos', 25), cursor, connection)
query(cursor)

connection.close()



