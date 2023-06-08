class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, personal):
		self.__personal = personal
		self.__sig=None
	def setSiguiente(self,siguiente):
		self.__siguiente=siguiente
	def getSiguiente(self):
		return self.__siguiente
	def personal(self):
		return self.__personal
	def toJSON(self):
		return self.__personal.toJSON()
		