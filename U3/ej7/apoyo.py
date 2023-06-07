from personal import Personal
class Apoyo(Personal):
	"""docstring for Apoyo"""
	def __init__(self,categoria,cuil,apellido,nombre,basico,antig):
		Personal.__init__(self,cuil,apellido,nombre,basico,antig)
		self.__categoria = categoria
		