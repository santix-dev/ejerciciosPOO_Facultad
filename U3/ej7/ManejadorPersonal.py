from lista import ListaEnlazada
from ObjectEncoder import ObjectEncoder
class ManejadorPersonal():
	"""docstring for ManejadorPersonal"""
	def __init__(self):
		self.__lista = ListaEnlazada()
	def cargar(self):
		decoder=ObjectEncoder()
		d=decoder.leerJSONArchivo()
		self.__lista=decoder.decodificarDiccionario(d)
