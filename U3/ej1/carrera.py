class Carrera(object):
	"""docstring for Carrera"""
	def __init__(self, codigo,nombre,titulo,duracion,tipo):
		self.__codigo = codigo
		self.__nombre = nombre.lower()
		self.__titulo = titulo
		self.__duracion = duracion
		self.__tipo = tipo
	def __str__(self):
		return f"""Codigo carrera: {self.__codigo}) {self.__nombre}\ntitulo: {self.__titulo} Duracion: {self.__duracion}"""
	def nombre(self):
		return self.__nombre
	def codigo(self):
		return self.__codigo