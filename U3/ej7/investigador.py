from personal import Personal
class Investigador(Personal):
	"""docstring for Investigador"""
	def __init__(self,area,tipo,cuil,apellido,nombre,basico,antig):
		Personal.__init__(self,cuil,apellido,nombre,basico,antig)
		self._area = area
		self._tipo = tipo
	def toJSON(self):
		d={
			"__class__":self.__class__.__name__,
			"__atributos__":{
				"area":self._area,
				"tipo":self._tipo,
				"cuil":self._cuil,
				"apellido":self._apellido,
				"nombre":self._nombre,
				"basico":self._basico,
				"antig":self._antig,
			}
		}
		# print(d)
		return d