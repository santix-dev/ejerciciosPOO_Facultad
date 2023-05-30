class Helado(object):
	"""docstring for Helado"""
	def __init__(self,gramos,precio):
		self.__gramos = gramos
		self.__precio = precio
		self.__sabores = []
	def agregarSabor(self,sabor):
		self.__sabores.append(sabor)
	def contarSabores(self,contadores):
		for sabor in self.__sabores:
			contadores[sabor.id()-1]+=1
	def gramos(self):
		return self.__gramos
	def cantSabores(self):
		return len(self.__sabores)
	def tiene(self,id,sabores):
		i=0
		flag=False
		if sabores.sabor(id) in self.__sabores:
			flag=True
		return flag
	def obtenerIDs(self,lista):
		for sabor in self.__sabores:
			if sabor.id() not in lista:
				lista.append(sabor.id())
		
		