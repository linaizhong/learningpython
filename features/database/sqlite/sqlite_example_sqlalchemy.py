# -*- coding: utf-8 -*-
"""Exemplo do uso SQLite em Python com SQLAlchemy"""
from sqlalchemy import *

# Base de dados file.db em memoria
db = create_engine('sqlite:///file.db')

# Acessibilidade aos metadados
metadata = MetaData(db)

# Echo de funcionamento dos metadados
metadata.bind.echo = True

#Table
table = Table('person', metadata, 
	Column('id', Integer, primary_key=True),
	Column('name', String(80)))

# Cria a Table
table.create()

# Carrega a tabela definida
table = Table('person', metadata, autoload=True)

# Insere dados
data = table.insert()
data.execute({'name': 'Bruno'})
data.execute({'name': 'Gabriel'})
data.execute({'name': 'Antonio'})

# Select
select = table.select()
for row in select.execute().fetchall():
	print row

