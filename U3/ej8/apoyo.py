from personal import Personal
class Apoyo(Personal):
	"""docstring for Apoyo"""
	def __init__(self,categoria,cuil,apellido,nombre,basico,antig):
		Personal.__init__(self,cuil,apellido,nombre,basico,antig)
		self.__categoria = str(categoria).lower()
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
	def sueldo(self):
		if self.__categoria>=1 and self.__categoria<=10:
			porCat=self._basico*0.1
		elif self.__categoria>=11 and self.__categoria<=20:
			porCat=self._basico*0.2
		else:
			porCat=self._basico*0.3
		return Personal.sueldo()+porCat



if __name__ == '__main__':
	p=Apoyo("1","20443166662","gimenez","santiago",30000,1)
	p.toJSON()
	print(p.dni())