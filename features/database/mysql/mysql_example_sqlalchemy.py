# -*- coding: utf-8 -*-
"""Exemplo do uso MySQL em Python com SQLAlchemy"""
from sqlalchemy import *
db = create_engine('mysql://root:@localhost:3306/example_db', echo=True)
connection = db.connect()
"""
Nota, deve estar criada a base de dados example_db
CREATE DATABASE example_db;
"""

# cria a base de dados
#db.execute('CREATE DATABASE example_db')

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

