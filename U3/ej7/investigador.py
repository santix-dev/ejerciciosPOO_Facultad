from personal import Personal
class Investigador(Personal):
	"""docstring for Investigador"""
	def __init__(self,area,tipo,cuil,apellido,nombre,basico,antig):
		Personal.__init__(self,cuil,apellido,nombre,basico,antig)
		self._area = area
		self._tipo = tipo
		