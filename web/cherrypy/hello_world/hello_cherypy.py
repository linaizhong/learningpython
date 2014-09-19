# -*- coding: utf-8 -*-
import cherrypy

class HelloWeb(object):
	"""
	O decorador @cherrypy.expose
	indica os metodos a serem publicados na Web.
	Seu retorno sera uma string enviada para o Browser
	"""
	@cherrypy.expose
	def index(self):
		return 'Hello World, welcome to Cherrypy.'


# Inicializa o cherrypy
# Use http://localhost:8080/ como endereco de teste default
cherrypy.quickstart(HelloWeb())

