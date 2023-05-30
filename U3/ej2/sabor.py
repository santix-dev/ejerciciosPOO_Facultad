class Sabor(object):
	"""docstring for Helado"""
	def __init__(self, idsabor,ingredientes,nombre):
		self.__idsabor = int(idsabor)
		self.__ingredientes = ingredientes
		self.__nombre = nombre
	def __str__(self):
		return f"Nombre: {self.__nombre} - ID: {self.__idsabor}"
	def id(self):
		return self.__idsabor