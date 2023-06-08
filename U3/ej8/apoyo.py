from personal import Personal
class Apoyo(Personal):
	"""docstring for Apoyo"""
	def __init__(self,categoria,cuil,apellido,nombre,basico,antig):
		Personal.__init__(self,cuil,apellido,nombre,basico,antig)
		self.__categoria = categoria.lower()
	def toJSON(self):
		d={
			"__class__":self.__class__.__name__,
			"__atributos__":{
				"categoria":self.__categoria,
				"cuil":self._cuil,
				"apellido":self._apellido,
				"nombre":self._nombre,
				"basico":self._basico,
				"antig":self._antig,
			}
		}
		# print(d)
		return d
	def clase(self):
		return self.__class__.__name__



if __name__ == '__main__':
	p=Apoyo(1,20443166662,"gimenez","santiago",30000,1)
	p.toJSON()