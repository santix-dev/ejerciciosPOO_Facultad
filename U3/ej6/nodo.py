class Nodo(object):
	def __init__(self, vehiculo):
		self.__vehiculo = vehiculo
		self.__siguiente = None
	def setSiguiente(self,siguiente):
		self.__siguiente=siguiente
	def getSiguiente(self):
		return self.__siguiente
	def vehiculo(self):
		return self.__vehiculo
	def modificarPrecio(self,precio):
		self.__vehiculo.modificarPrecio(precio)
	def toJSON(self):
		return self.__vehiculo.toJSON()
		