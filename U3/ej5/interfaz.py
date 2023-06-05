from zope.interface import Interface

class InterfazLista(Interface):
	"""docstring for InterfazLista"""
	def insertar(self,elemento,posicion):
		pass
	def agregar(self,elemento):
		pass
	def mostrar(self,posicion):
		pass
