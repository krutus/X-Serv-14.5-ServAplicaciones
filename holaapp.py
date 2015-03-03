#!/usr/bin/python
import webapp

class holaApp(webapp.webApp):

	def process(self,parsedRequest):
		"""Process the relevant elements of the request.

		Devuelve el codigo HTTP de la respuesta y una pag HTML.
		"""

		return("200 OK", "<html><body><h1>Hola mundo</h1></body></html>")

if __name__=="__main__":
	testWeb=holaApp("localhost",1234)
